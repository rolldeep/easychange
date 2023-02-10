from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/currencies/{currency}")
def get_currency(currency: str):
    return {"currency": currency}


