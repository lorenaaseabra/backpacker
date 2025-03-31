import sys

cidades = ["Berlim", "Viena", "Bruxelas", "Praga", "Copenhague", "Paris", "Atenas", "Budapeste", "Roma", "Lisboa", "Madrid"]

grafo = [
    [0, 680, 770, 350, 620, 1050, 0, 870, 0, 0, 0],
    [680, 0, 0, 300, 0, 0, 0, 220, 1100, 0, 0],
    [770, 0, 0, 0, 0, 320, 0, 0, 0, 0, 0],
    [350, 300, 0, 0, 0, 0, 0, 450, 0, 0, 0],
    [620, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1050, 0, 320, 0, 0, 0, 0, 0, 1400, 1700, 1300],
    [0, 0, 0, 0, 0, 0, 0, 1200, 1300, 0, 0],
    [870, 220, 0, 450, 0, 0, 1200, 0, 800, 0, 0],
    [0, 1100, 0, 0, 0, 1400, 1300, 800, 0, 2400, 1950],
    [0, 0, 0, 0, 0, 1700, 0, 0, 2400, 0, 630],
    [0, 0, 0, 0, 0, 1300, 0, 0, 1950, 630, 0]
]

def dijkstra(grafo, cidade_origem, cidade_destino, cidades):
    num_cidades = len(cidades)
    origem_idx = cidades.index(cidade_origem)
    destino_idx = cidades.index(cidade_destino)
    
    distancias = [sys.maxsize] * num_cidades
    visitados = [False] * num_cidades
    anteriores = [-1] * num_cidades
    
    distancias[origem_idx] = 0
    
    for _ in range(num_cidades):
        min_distancia = sys.maxsize
        min_indice = -1
        for v in range(num_cidades):
            if not visitados[v] and distancias[v] < min_distancia:
                min_distancia = distancias[v]
                min_indice = v
        
        if min_indice == -1:
            break
        
        visitados[min_indice] = True
        
        if min_indice == destino_idx:
            break
        
        for v in range(num_cidades):
            if grafo[min_indice][v] > 0:
                if distancias[min_indice] + grafo[min_indice][v] < distancias[v]:
                    distancias[v] = distancias[min_indice] + grafo[min_indice][v]
                    anteriores[v] = min_indice
    
    if distancias[destino_idx] == sys.maxsize:
        return None, None
    
    caminho = []
    atual = destino_idx
    while atual != -1:
        caminho.append(cidades[atual])
        atual = anteriores[atual]
    
    caminho.reverse()
    
    return distancias[destino_idx], caminho
