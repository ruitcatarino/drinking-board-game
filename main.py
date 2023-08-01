import random
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

sorte = [
    {
        "item": "SORTE",
        "probability": 0.05,
        "description": "Estás livre da prisão! Guarda esta carta para uso próprio ou podes oferecer/vender a outro jogar por goles.",
    },
    {
        "item": "IMUNIDADE",
        "probability": 0.1,
        "description": "A partir de este momento estás safo de um desafio à tua escolha.",
    },
    {
        "item": "REVERSO",
        "probability": 0.185,
        "description": "Usa esta carta para te livrares de um desafio e escolhe outro jogador para fazê-lo por ti.",
    },
    {
        "item": "SORTE GRANDE",
        "probability": 0.185,
        "description": "Avança três casas!",
    },
    {
        "item": "PASSA À FRENTE",
        "probability": 0.185,
        "description": "Nos próximos dois desafios, caso o teu parceiro de jogo tenha de beber, tu não precisas de o fazer!",
    },
    {
        "item": "AMIGO SORTUDO",
        "probability": 0.11,
        "description": "Escolhe um jogador para beber o dobro nesta rodada.",
    },
    {
        "item": "ÉS O ESCOLHIDO",
        "probability": 0.185,
        "description": "Todos os jogadores bebem um gole extra durante esta ronda, mas tu não.",
    },
]

azar = [
    {
        "item": "ESTÁS COM SEDE",
        "probability": 0.05,
        "description": "Pede aos outros jogadores para te trazerem um shot de uma bebida alcoólica à escolha deles.",
    },
    {
        "item": "TICK TACK",
        "probability": 0.05,
        "description": "A partir deste momento tens exatamente dois minutos para terminares o teu copo. Boa sorte!",
    },
    {
        "item": "VAIS DENTRO",
        "probability": 0.18,
        "description": "Vai diretamente para a casa da prisão. Azarito!",
    },
    {
        "item": "GRANDE AZAR",
        "probability": 0.18,
        "description": "Volta três casas atrás.",
    },
    {
        "item": "ROLA OUTRA VEZ",
        "probability": 0.18,
        "description": "Joga os dados de novo. O número que sair são as casas que tens de voltar atrás!",
    },
    {
        "item": "AZAR NO BARALHO",
        "probability": 0.18,
        "description": "Bebe dois goles e tira outa carta!",
    },
    {
        "item": "DISCURSO AZARADO",
        "probability": 0.18,
        "description": "Inventa uma catchphrase que terás de dizer sempre antes de beber (durante duas rondas)!",
    },
]

misterio = [
    {
        "item": "MONARQUIA",
        "probability": 0.04,
        "description": "Podes eliminar todas as regras existentes e substituir pelas que quiseres.",
    },
    {
        "item": "ÉS TU QUE MANDAS",
        "probability": 0.15,
        "description": "Tens a possibilidade de criar uma regra e eliminar outra!",
    },
    {
        "item": "QUE CHATICE",
        "probability": 0.15,
        "description": "Recua duas casas!",
    },
    {
        "item": "NEM QUERIAS",
        "probability": 0.15,
        "description": "Avança duas casas.",
    },
    {
        "item": "A ESCOLHA É TUA",
        "probability": 0.15,
        "description": "Caso tenhas parceiro(s) de jogo, tens a opção de sair do grupo.",
    },
    {
        "item": "MISTÉRIO DO DESTINO",
        "probability": 0.15,
        "description": "Atira uma moeda ao ar. Se sair cara escolhe alguem para beber, se sair coroa bebes tu.",
    },
    {
        "item": "SORTE ENCANTADA",
        "probability": 0.06,
        "description": "Ganha um bônus de sorte: escolhe a bebida que quiseres (sim pode ser água) para beber durante esta ronda.",
    },
    {
        "item": "PENA ESCONDIDA",
        "probability": 0.15,
        "description": "Escolhe uma pessoa e pensa num número de 1 a 5. A pessoa terá de beber penalidades e no fim dizer quantas bebeu, se acertar acabou se não volta a beber até adivinhar o número.",
    },
]


@app.get("/")
def welcome():
    return HTMLResponse(content=html_main(), status_code=200)


@app.get("/azar")
def get_azar():
    html_content = return_dict_parse(azar,"https://i.ibb.co/9h1v5LK/bad-luck-1176087376.jpg")
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/sorte")
def get_sorte():
    html_content = return_dict_parse(sorte,"https://i.ibb.co/gr90HJJ/sorte.png")
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/misterio")
def get_misterio():
    html_content = return_dict_parse(misterio,"https://i.ibb.co/1msVT88/mistery.png")
    return HTMLResponse(content=html_content, status_code=200)


def return_dict_parse(dicty,icon_url):
    probabilities = [item["probability"] for item in dicty]
    random_index = random.choices(range(len(dicty)), weights=probabilities)[0]
    chosen_item_dicty = dicty[random_index]
    return html_parse(chosen_item_dicty["item"], chosen_item_dicty["description"],icon_url)


def html_parse(item, description,icon_url):
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
        <div class="d-flex justify-content-center align-items-center flex-column vh-100">
            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="{icon_url}" alt="Symbol">
                <div class="card-body">
                    <h5 class="card-title">{item}</h5>
                    <p class="card-text">{description}</p>
                </div>
            </div>
            <div class="d-flex justify-content-center mt-3">
                <a href="https://boardgame-1-s6567828.deta.app/" class="btn btn-secondary btn-lg active" role="button" aria-pressed="true">Go Back</a>
            </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

def html_main():
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
        <div class="d-flex justify-content-center align-items-center flex-column vh-100">
            <div class="container" style="min-height: 100%;">
                <h2 class="my-4">Welcome to the best Drinking Game, Pitos!</h2>
                <div class="row justify-content-center">
                    <div class="col-lg-4 col-md-6 col-sm-6 col-12" style="margin-bottom: 1rem;">
                        <div class="card text-center border-success mb-3" style="width: 18rem;">
                            <a href="https://boardgame-1-s6567828.deta.app/sorte">
                                <img class="card-img-top" src="https://i.ibb.co/gr90HJJ/sorte.png" alt="Sorte">
                            </a>
                            <div class="card-body">
                                <h5 class="card-title">Sorte</h5>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6 col-12" style="margin-bottom: 1rem;">
                        <div class="card text-center border-danger mb-3" style="width: 18rem;">
                            <a href="https://boardgame-1-s6567828.deta.app/azar">
                                <img class="card-img-top" src="https://i.ibb.co/9h1v5LK/bad-luck-1176087376.jpg" alt="Azar">
                            </a>
                            <div class="card-body">
                                <h5 class="card-title">Azar</h5>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-sm-6 col-12" style="margin-bottom: 1rem;">
                        <div class="card text-center border-dark mb-3" style="width: 18rem;">
                            <a href="https://boardgame-1-s6567828.deta.app/misterio">
                                <img class="card-img-top" src="https://i.ibb.co/1msVT88/mistery.png" alt="Mistério">
                            </a>
                            <div class="card-body">
                                <h5 class="card-title">Mistério</h5>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """