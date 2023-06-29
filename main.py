from fastapi import FastAPI
from typing import Union
from prueba.api.openai.py import Document, convertidor

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/convertidor', status_code = 200)
def convertidor_endpoint(doc: Document):
    response= convertidor(doc.prompt)
    return{
        'convertidor': response[0],
        'usage': response[1]
    }

