import random
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

sorte = [
    {
        "item": "SORTE",
        "probability": 0.3,
        "description": "Estas livre da prisao!\nGuarda esta carta para uso proprio ou podes oferecer/vender a outro jogar por goles.",
    },
    {
        "item": "IMUNIDADE",
        "probability": 0.2,
        "description": "A partir de este momento estas safo de um desafio a tua escolha.",
    },
    {
        "item": "REVERSO",
        "probability": 0.2,
        "description": "Usa esta carta para te livrares de um desafio e escolhe outro jogador para faze-lo por ti.",
    },
    {
        "item": "SORTE GRANDE",
        "probability": 0.3,
        "description": "Avanca tres casas!",
    },
]

azar = []

misterio = []


@app.get("/")
def welcome():
    return "Welcome to the perfect drinking board-game!"


@app.get("/azar")
def get_azar():
    return {}


@app.get("/sorte")
def get_sorte():
    choice = return_dict_rand(sorte)
    return {choice["item"]: choice["description"]}


@app.get("/misterio")
def get_misterio():
    return {}


def return_dict_rand(dicty):
    probabilities = [item["probability"] for item in dicty]
    random_index = random.choices(range(len(dicty)), weights=probabilities)[0]
    chosen_item_dicty = dicty[random_index]
    return chosen_item_dicty
