import sys

def dijkstra(grafo, cidade_origem, cidade_destino, cidades):
    # Número total de cidades
    num_cidades = len(cidades)
    
    # Converter nomes de cidades para índices
    origem_idx = cidades.index(cidade_origem)
    destino_idx = cidades.index(cidade_destino)
    
    # Inicializar distâncias com infinito
    distancias = [sys.maxsize] * num_cidades
    visitados = [False] * num_cidades
    anteriores = [-1] * num_cidades
    
    # Distância da cidade de origem para ela mesma é 0
    distancias[origem_idx] = 0
    
    # Algoritmo de Dijkstra
    for _ in range(num_cidades):
        # Encontrar o vértice com a menor distância entre os não visitados
        min_distancia = sys.maxsize
        min_indice = -1
        
        for v in range(num_cidades):
            if not visitados[v] and distancias[v] < min_distancia:
                min_distancia = distancias[v]
                min_indice = v
        
        # Se não encontramos nenhuma cidade acessível
        if min_indice == -1:
            break
        
        # Marcar o vértice como visitado
        visitados[min_indice] = True
        
        # Se chegamos ao destino, podemos parar
        if min_indice == destino_idx:
            break
        
        # Atualizar distâncias para cidades vizinhas
        for v in range(num_cidades):
            # Verificar se há uma conexão direta entre min_indice e v
            if grafo[min_indice][v] > 0:
                # Se encontramos um caminho mais curto para v através de min_indice
                if distancias[min_indice] + grafo[min_indice][v] < distancias[v]:
                    distancias[v] = distancias[min_indice] + grafo[min_indice][v]
                    anteriores[v] = min_indice
    
    # Reconstruir o caminho
    if distancias[destino_idx] == sys.maxsize:
        return None, None  # Não há caminho
    
    caminho = []
    atual = destino_idx
    while atual != -1:
        caminho.append(cidades[atual])
        atual = anteriores[atual]
    
    # Inverter o caminho (do início ao fim)
    caminho.reverse()
    
    return distancias[destino_idx], caminho

def main():
    # Lista de cidades
    cidades = ["Berlim", "Viena", "Bruxelas", "Praga", "Copenhague", "Paris", "Atenas", "Budapeste", "Roma", "Lisboa", "Madrid"]
    
    # Criar grafo - matriz de adjacência para as cidades conectadas
    # Valor 0 significa nenhuma conexão direta
    # Os valores positivos representam as distâncias em km
    grafo = [
        # Berlim  Viena  Bruxelas  Praga  Copenhague  Paris  Atenas  Budapeste  Roma  Lisboa  Madrid
        [0,       680,   770,      350,   620,        1050,  0,      870,       0,    0,      0],      # Berlim
        [680,     0,     0,        300,   0,          0,     0,      220,       1100, 0,      0],      # Viena
        [770,     0,     0,        0,     0,          320,   0,      0,         0,    0,      0],      # Bruxelas
        [350,     300,   0,        0,     0,          0,     0,      450,       0,    0,      0],      # Praga
        [620,     0,     0,        0,     0,          0,     0,      0,         0,    0,      0],      # Copenhague
        [1050,    0,     320,      0,     0,          0,     0,      0,         1400, 1700,   1300],   # Paris
        [0,       0,     0,        0,     0,          0,     0,      1200,      1300, 0,      0],      # Atenas
        [870,     220,   0,        450,   0,          0,     1200,   0,         800,  0,      0],      # Budapeste
        [0,       1100,  0,        0,     0,          1400,  1300,   800,       0,    2400,   1950],   # Roma
        [0,       0,     0,        0,     0,          1700,  0,      0,         2400, 0,      630],    # Lisboa
        [0,       0,     0,        0,     0,          1300,  0,      0,         1950, 630,    0]       # Madrid
    ]
    
    print("Cidades disponíveis:")
    for i, cidade in enumerate(cidades):
        print(f"{i+1}. {cidade}")
    
    while True:
        try:
            # Solicitar entrada do usuário
            origem = input("\nDigite o nome da cidade de origem (ou 'sair' para encerrar): ")
            if origem.lower() == 'sair':
                break
                
            if origem not in cidades:
                print(f"Cidade '{origem}' não encontrada na lista. Tente novamente.")
                continue
                
            destino = input("Digite o nome da cidade de destino: ")
            if destino not in cidades:
                print(f"Cidade '{destino}' não encontrada na lista. Tente novamente.")
                continue
            
            if origem == destino:
                print("Origem e destino são iguais.")
                continue
            
            # Calcular o caminho mais curto
            distancia, caminho = dijkstra(grafo, origem, destino, cidades)
            
            if distancia is None:
                print(f"Não há caminho entre {origem} e {destino}.")
            else:
                print(f"\nCaminho mais curto de {origem} para {destino}:")
                print(" -> ".join(caminho))
                print(f"Distância total: {distancia} km")
                
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()