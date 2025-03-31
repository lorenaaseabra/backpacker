from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algoritmo import cidades, grafo, dijkstra

app = FastAPI()

# Habilita CORS para integração com o frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Altere "*" pelo domínio do seu frontend em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RotaRequest(BaseModel):
    origem: str
    destino: str

@app.get("/cidades")
def obter_cidades():
    return cidades

@app.post("/rota")
def calcular_rota(dados: RotaRequest):
    if dados.origem not in cidades or dados.destino not in cidades:
        raise HTTPException(status_code=400, detail="Cidade inválida!")

    distancia, caminho = dijkstra(grafo, dados.origem, dados.destino, cidades)

    if distancia is None:
        raise HTTPException(status_code=404, detail="Rota não encontrada!")

    return {
        "distancia": distancia,
        "caminho": caminho
    }
