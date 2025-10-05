import heapq

def BuscaGulosaGrafo(grafo, inicio, objetivo, heuristico):

  # Fronteira
  fronteira = []
  heapq.heappush(fronteira, (heuristico[inicio], inicio, [inicio]))

  # Registro de passagem
  visitados = set()

  # Loop
  while fronteira:

    
    h_atual, no_atual, caminho = heapq.heappop(fronteira)

    if no_atual == objetivo:
        return caminho # Caminho encontrado

    for vizinho in grafo[no_atual]:
        if vizinho not in visitados:
          novo_caminho = caminho + [vizinho]
          heapq.heappush(fronteira, (heuristico[vizinho], vizinho, novo_caminho))

  return None

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['D', 'E'],
    'D': ['E', 'F'],
    'E': ['F'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

heuristica = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 1,
    'F': 5,
    'G': 3,
    'H': 0
}

inicio = input('Digite o nó inicial: ').upper()
objetivo = input('Digite o nó de objetivo: ').upper()

caminho_encontrado = BuscaGulosaGrafo(grafo, inicio, objetivo, heuristica)

if caminho_encontrado:
  print("Caminho encontrado:", caminho_encontrado)
else:
  print("Caminho não encontrado.")
