from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"hello": "world"}

@app.get("/name")
def names():
    return {"name": "Abraham"}