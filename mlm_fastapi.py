import uvicorn
from typing import Dict
from fastapi import FastAPI
from transformers import pipeline
from dataclasses import dataclass

# pre-load pipelines
xlm_roberta_base = pipeline('fill-mask', model='xlm-roberta-base')
xlm_roberta_large = pipeline('fill-mask', model='xlm-roberta-large')

# define type hints
@dataclass
class Request:
    text: str
    model: str
    
@dataclass
class Response:
    text: str
    model: str
    predictions: Dict

# declaring FastAPI instance
app = FastAPI()
 
@app.post('/predict')
def predict(request: Request) -> Response:
    preds = {}
    
    outputs = xlm_roberta_large(request.text) if request.model.endswith("large") else xlm_roberta_base(request.text)

    for output in outputs:
        preds[output["token_str"]] = output["score"] 

    return Response(
        text = request.text, 
        model = request.model, 
        predictions = preds
        )

