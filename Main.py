from BuscaSemInformacao.Node import Node 
from BuscaSemInformacao.BuscaLargura import BuscaLargura
from BuscaSemInformacao.BuscaProfundidade import BuscaProfundidade
from BuscaSemInformacao.BuscaProfunInterativa import BuscaProfundidadeIterativa

import time

# nodeEstadoInicial = Node([1, 2, 3, 4, 0, 5, 6, 7, 8], 0, None, None, 0) #Busca 3*3
# nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None, 0)

nodeEstadoInicial = Node([5,1, 2, 3, 4, 0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0, None, None, 0) #Busca 4*4
nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0, None, None, 0)

# print("\033[33mBusca em Largura:\033[0m")
# tempo_inicio = time.time()
# buscaLargura = BuscaLargura(nodeEstadoInicial, nodeEstadoObjetivo)
# buscaLargura.buscaLargura(),
# tempo_fim = time.time()
# duracao = tempo_fim - tempo_inicio

# print(f"Tempo de execução da busca em largura: {duracao:.4f} segundos")


print("\n\033[33mBusca em Profundidade:\033[0m")
tempo_inicio = time.time()
buscaProfundidade = BuscaProfundidade(nodeEstadoInicial, nodeEstadoObjetivo)
buscaProfundidade.buscaProfundidade()
tempo_fim = time.time()
duracao = tempo_fim - tempo_inicio 
print(f"Tempo de execução da busca em profundidade: {duracao:.4f} segundos")


# print("\n\033[33mBusca em Profundidade Iterativa:\033[0m")
# tempo_inicio = time.time()
# buscaProfundidadeIterativa = BuscaProfundidadeIterativa(nodeEstadoInicial, nodeEstadoObjetivo, 30)
# buscaProfundidadeIterativa.buscaProfundidadeIterativa()
# tempo_fim = time.time()
# duracao = tempo_fim - tempo_inicio 
# print(f"Tempo de execução da busca em profundidade iterativa: {duracao:.4f} segundos")

