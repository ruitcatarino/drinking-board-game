import random
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

sorte = [
    {
        "item": "SORTE",
        "probability": 0.1,
        "description": "Estás livre da prisão! Guarda esta carta para uso próprio ou podes oferecer/vender a outro jogar por goles.",
    },
    {
        "item": "IMUNIDADE",
        "probability": 0.1,
        "description": "A partir de este momento estás safo de um desafio à tua escolha.",
    },
    {
        "item": "REVERSO",
        "probability": 0.3,
        "description": "Usa esta carta para te livrares de um desafio e escolhe outro jogador para fazê-lo por ti.",
    },
    {
        "item": "SORTE GRANDE",
        "probability": 0.2,
        "description": "Avança três casas!",
    },
    {
        "item": "PASSA À FRENTE",
        "probability": 0.3,
        "description": "Nos próximos dois desafios, caso o teu parceiro de jogo tenha de beber, tu não precisas de o fazer!",
    },
]

azar = [
    {
        "item": "ESTÁS COM SEDE",
        "probability": 0.1,
        "description": "Pede aos outros jogadores para te trazerem um shot de uma bebida alcoólica à escolha deles.",
    },
    {
        "item": "TICK TACK",
        "probability": 0.1,
        "description": "A partir deste momento tens exatamente dois minutos para terminares o teu copo. Boa sorte!",
    },
    {
        "item": "VAIS DENTRO",
        "probability": 0.2,
        "description": "Vai diretamente para a casa da prisão. Azarito!",
    },
    {
        "item": "GRANDE AZAR",
        "probability": 0.3,
        "description": "Volta três casas atrás.",
    },
    {
        "item": "ROLA OUTRA VEZ",
        "probability": 0.3,
        "description": "Joga os dados de novo. O número que sair são as casas que tens de voltar atrás!",
    },
]

misterio = [
    {
        "item": "MONARQUIA",
        "probability": 0.1,
        "description": "Podes eliminar todas as regras existentes e substituir pelas que quiseres.",
    },
    {
        "item": "ÉS TU QUE MANDAS",
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
        "description": "Avança duas casas.",
    },
    {
        "item": "A ESCOLHA É TUA",
        "probability": 0.2,
        "description": "Caso tenhas parceiro(s) de jogo, tens a opção de sair do grupo.",
    },
]


@app.get("/")
def welcome():
    return "Welcome to the perfect drinking board-game!"


@app.get("/azar")
def get_azar():
    html_content = return_dict_parse(azar)
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/sorte")
def get_sorte():
    html_content = return_dict_parse(sorte)
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/misterio")
def get_misterio():
    html_content = return_dict_parse(misterio)
    return HTMLResponse(content=html_content, status_code=200)


def return_dict_parse(dicty):
    probabilities = [item["probability"] for item in dicty]
    random_index = random.choices(range(len(dicty)), weights=probabilities)[0]
    chosen_item_dicty = dicty[random_index]
    return html_parse(chosen_item_dicty["item"], chosen_item_dicty["description"])


def html_parse(item, description):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>The Greates Drinking Game</title>

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body>
        <div class="d-flex justify-content-center align-items-center vh-100">
            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="https://i.ibb.co/gr90HJJ/sorte.png" alt="Symbol">
                <div class="card-body">
                <h5 class="card-title">{item}</h5>
                <p class="card-text">{description}</p>
                </div>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """