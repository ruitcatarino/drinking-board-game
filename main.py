from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return "Welcome to the perfect drinking board-game!"


@app.get("/azar")
def get_azar():
    return {}


@app.get("/sorte")
def get_sorte():
    return {}


@app.get("/misterio")
def get_misterio():
    return {}
