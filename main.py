import random
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

sorte = [
    {
        "item": "SORTE",
        "probability": 0.1,
        "description": "Estas livre da prisao! Guarda esta carta para uso proprio ou podes oferecer/vender a outro jogar por goles.",
    },
    {
        "item": "IMUNIDADE",
        "probability": 0.1,
        "description": "A partir de este momento estas safo de um desafio a tua escolha.",
    },
    {
        "item": "REVERSO",
        "probability": 0.3,
        "description": "Usa esta carta para te livrares de um desafio e escolhe outro jogador para faze-lo por ti.",
    },
    {
        "item": "SORTE GRANDE",
        "probability": 0.2,
        "description": "Avanca tres casas!",
    },
    {
        "item": "PASSA A FRENTE",
        "probability": 0.3,
        "description": "Nos proximos dois desafios, caso o teu parceiro de jogo tenha de beber, tu nao precisas de o fazer!",
    },
]

azar = [
    {
        "item": "ESTAS COM SEDE",
        "probability": 0.1,
        "description": "Pede aos outros jogadores para te trazerem um shot de uma bebida alcoolica a escolha deles.",
    },
    {
        "item": "TICK TACK",
        "probability": 0.1,
        "description": "A partir deste momento tens exatamente dois minutos para terminares o teu copo. Boa sorte!",
    },
    {
        "item": "VAIS DENTRO",
        "probability": 0.2,
        "description": "Vai diretamente para a casa da prisao. Azarito!",
    },
    {
        "item": "GRANDE AZAR",
        "probability": 0.3,
        "description": "Volta tres casas atras!",
    },
    {
        "item": "ROLA OUTRA VEZ",
        "probability": 0.3,
        "description": "Joga os dados de novo. O numero que sair sao as casas que tens de voltar atras!",
    },
]

misterio = [
    {
        "item": "MONARQUIA",
        "probability": 0.1,
        "description": "Podes eliminar todas as regras existentes e substituir pelas que quiseres.",
    },
    {
        "item": "ES TU QUE MANDAS",
        "probability": 0.2,
        "description": "Tens a possibilidade de criar uma regra e eliminar outra!",
    },
    {
        "item": "QUE CHATICE",
        "probability": 0.3,
        "description": "Recua duas casas!",
    },
    {
        "item": "NEM QUERIAS",
        "probability": 0.2,
        "description": "Avanca duas casas.",
    },
    {
        "item": "A ESCOLHA E TUA",
        "probability": 0.2,
        "description": "Caso tenhas parceiro(s) de jogo, tens a opcao de sair do grupo.",
    },
]


@app.get("/")
def welcome():
    return "Welcome to the perfect drinking board-game!"


@app.get("/azar")
def get_azar():
    return return_dict_rand(azar)


@app.get("/sorte")
def get_sorte():
    return return_dict_rand(sorte)


@app.get("/misterio")
def get_misterio():
    return return_dict_rand(misterio)


def return_dict_rand(dicty):
    probabilities = [item["probability"] for item in dicty]
    random_index = random.choices(range(len(dicty)), weights=probabilities)[0]
    chosen_item_dicty = dicty[random_index]
    return {chosen_item_dicty["item"]: chosen_item_dicty["description"]}
