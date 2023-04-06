import uvicorn
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# pre-load pipelines
xlm_roberta_base = pipeline('fill-mask', model='xlm-roberta-base')
xlm_roberta_large = pipeline('fill-mask', model='xlm-roberta-large')

class Request(BaseModel):
    text: str
    model: str
    
class Response(BaseModel):
    text: str
    model: str
    predictions: Dict

# declaring FastAPI instance
app = FastAPI()

@app.get("/")
def status():
    return {"api_status": "OK"}

@app.get("/models")
def list_models():
    return {"models": ["xlm-roberta-base", "xlm-roberta-large"]}
 
@app.post('/predict', response_model=Response)
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

