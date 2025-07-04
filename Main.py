from Node import Node 
from BuscaLargura import BuscaLargura
from BuscaProfundidade import BuscaProfundidade


import time

nodeEstadoInicial = Node([3,1,2,4,0,5,6,7,8], 0, None, None, None) #Busca 3*3
nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None, None)

# nodeEstadoInicial = Node([4,1,2,3,0,5,6,7,8,9,10,11,12,13,14,15], 0, None, None, None) #Busca 4*4
# nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0, None, None, None)

# nodeEstadoInicial = Node([1, 2, 3, 4, 5,6, 7, 8, 9, 10,11, 12, 13,14, 15,16, 17, 18, 0, 19,20, 21, 22,23, 24], 0, None, None, None) #Busca 5*5
# nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], 0, None, None, None)

print("\033[33mBusca em Largura:\033[0m")
tempo_inicio = time.time()
buscaLargura = BuscaLargura(nodeEstadoInicial, nodeEstadoObjetivo)
buscaLargura.buscaLargura(),
tempo_fim = time.time()
duracao = tempo_fim - tempo_inicio

print(f"Tempo de execução da busca em largura: {duracao:.4f} segundos")

print("\n\033[33mBusca em Profundidade:\033[0m")
tempo_inicio = time.time()
buscaProfundidade = BuscaProfundidade(nodeEstadoInicial, nodeEstadoObjetivo)
buscaProfundidade.buscaProfundidade()
tempo_fim = time.time()
duracao = tempo_fim - tempo_inicio 
print(f"Tempo de execução da busca em profundidade: {duracao:.4f} segundos")