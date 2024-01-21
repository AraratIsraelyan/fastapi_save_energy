from fastapi import FastAPI, Form
from fastapi.params import Depends
from fastapi.responses import FileResponse
from pydantic import BaseModel


class Person(BaseModel):
    name: str = Form()
    age: int = Form()


app = FastAPI()


@app.get("/")
def root():
    return FileResponse("public/1.html")


@app.post("/hello")
def hello(person: Person = Depends()):
    return person