# Masked Language Modeling


## Setup
```bash
pip3 install -r requirements.txt
```

# FastAPI

``` bash
uvicorn fastAPI:app 
```
#### You could either try the API at <ins>http://127.0.0.1:8000/docs</ins> or use the curl command as shown below -
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hello <mask>",
  "model": "xlm-roberta-base"
}'
```

# Gradio

``` bash
python3 Gradio.py
```
#### You could try the web application at <ins>http://127.0.0.1:7860</ins>
