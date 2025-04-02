import sys

cidades = ["Berlim", "Viena", "Bruxelas", "Praga", "Paris", "Atenas", "Budapeste", "Roma", "Lisboa", "Madrid"]


# Matriz de adj 11x11 -> n x n -> o(n²)
grafo = [
    [0, 680, 770, 350, 1050, 0, 870, 0, 0, 0],   # Berlim
    [680, 0, 0, 300, 0, 0, 220, 1100, 0, 0],     # Viena
    [770, 0, 0, 0, 320, 0, 0, 0, 0, 0],          # Bruxelas
    [350, 300, 0, 0, 0, 0, 450, 0, 0, 0],        # Praga
    [1050, 0, 320, 0, 0, 0, 0, 1400, 1700, 1300],# Paris
    [0, 0, 0, 0, 0, 0, 1200, 1300, 0, 0],        # Atenas
    [870, 220, 0, 450, 0, 1200, 0, 800, 0, 0],   # Budapeste
    [0, 1100, 0, 0, 1400, 1300, 800, 0, 2400, 1950], # Roma
    [0, 0, 0, 0, 1700, 0, 0, 2400, 0, 630],      # Lisboa
    [0, 0, 0, 0, 1300, 0, 0, 1950, 630, 0]       # Madrid
]


def dijkstra(grafo, cidade_origem, cidade_destino, cidades):
    num_cidades = len(cidades)
    origem_idx = cidades.index(cidade_origem)
    destino_idx = cidades.index(cidade_destino)
    
    distancias = [sys.maxsize] * num_cidades 
    visitados = [False] * num_cidades
    anteriores = [-1] * num_cidades
    
    distancias[origem_idx] = 0
    
    #nó com menor distancia ainda n visitado 
    for _ in range(num_cidades): # roda n vezes → o(n)
        min_distancia = sys.maxsize
        min_indice = -1
        for v in range(num_cidades): #passa por todas as cidades p encontrar a n visitada -> o(n)
            if not visitados[v] and distancias[v] < min_distancia:
                min_distancia = distancias[v]
                min_indice = v
        # se não tiver distancia menor ai termina
        if min_indice == -1:
            break
        #marca como visitado
        visitados[min_indice] = True
        #se chega no destino ele termina
        if min_indice == destino_idx:
            break
        #att as distancias p/ os vizinhos
        for v in range(num_cidades): # passa p todas as iteração do loop principal, o(n) p/ cada if -> o(n²) 
            if grafo[min_indice][v] > 0:
                if distancias[min_indice] + grafo[min_indice][v] < distancias[v]:
                    distancias[v] = distancias[min_indice] + grafo[min_indice][v]
                    anteriores[v] = min_indice
    
    if distancias[destino_idx] == sys.maxsize:
        return None, None
    #reconstroi de tras p frente e printa o caminho todo
    caminho = []
    atual = destino_idx
    while atual != -1:
        caminho.append(cidades[atual])
        atual = anteriores[atual]
    
    caminho.reverse()
    
    return distancias[destino_idx], caminho
