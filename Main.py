from BuscaSemInformacao.Node import Node
from BuscaSemInformacao.BuscaLargura import BuscaLargura
from BuscaSemInformacao.BuscaProfundidade import BuscaProfundidade
from BuscaSemInformacao.BuscaProfunInterativa import BuscaProfundidadeIterativa
from BuscaComInformacao.NodeComInformacao import NodeI
from BuscaComInformacao.BuscaGulosa import BuscaGulosa
from BuscaComInformacao.BuscaEstrela import BuscaEstrela

import time

nodeEstadoInicial = Node([1, 2, 3, 4, 0, 5, 6, 7, 8], 0, None, None, 0) #Busca 3*3
nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None, 0)

# nodeEstadoInicial = Node([1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0, None, None, 0) #Busca 4*4
# nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0, None, None, 0)

# nodeEstadoInicial = NodeI([1, 2, 3, 4, 0, 5, 6, 7, 8], 0, None, None, None) #Busca 3*3
# nodeEstadoObjetivo = NodeI([0,1,2,3,4,5,6,7,8], 0, None, None, None)


# nodeEstadoInicialComInfo = NodeI([1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0, None, None, None) #Busca 4*4
# nodeEstadoObjetivoComInfo = NodeI([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0, None, None, None)


nodeEstadoInicialComInfo = NodeI([1, 2, 3, 4, 0, 5, 6, 7, 8], 0, None, None, 0) #Busca 3*3
nodeEstadoObjetivoComInfo = NodeI([0,1,2,3,4,5,6,7,8], 0, None, None, 0)

print("\033[1m\033[33mBusca em Largura:\033[0m")
tempoInicio = time.time()
buscaLargura = BuscaLargura(nodeEstadoInicial, nodeEstadoObjetivo)
buscaLargura.buscaLargura(),
tempoFim = time.time()
duracao = tempoFim - tempoInicio

print(f"Tempo de execução da busca em largura: {duracao:.4f} segundos")


print("\033[1m\n\033[33mBusca em Profundidade:\033[0m")
tempoInicio = time.time()
buscaProfundidade = BuscaProfundidade(nodeEstadoInicial, nodeEstadoObjetivo)
buscaProfundidade.buscaProfundidade()
tempoFim = time.time()
duracao = tempoFim - tempoInicio 
print(f"Tempo de execução da busca em profundidade: {duracao:.4f} segundos")


print("\033[1m\n\033[33mBusca em Profundidade Iterativa:\033[0m")
tempoInicio = time.time()
buscaProfundidadeIterativa = BuscaProfundidadeIterativa(nodeEstadoInicial, nodeEstadoObjetivo, 30)
buscaProfundidadeIterativa.buscaProfundidadeIterativa()
tempoFim = time.time()
duracao = tempoFim - tempoInicio 
print(f"Tempo de execução da busca em profundidade iterativa: {duracao:.4f} segundos")


print("\033[1m\n\033[33mBusca Gulosa:\033[0m")
tempoInicio = time.time()
buscaGulosa = BuscaGulosa(nodeEstadoInicialComInfo, nodeEstadoObjetivoComInfo)
buscaGulosa.buscaGulosa()
tempoFim = time.time()
duracao = tempoFim - tempoInicio
print(f"Tempo de execução da busca gulosa: {duracao:.4f} segundos")


print("\033[1m\n\033[33mBusca Estrela:\033[0m")
tempoInicio = time.time()
buscaEstrela = BuscaEstrela(nodeEstadoInicialComInfo, nodeEstadoObjetivoComInfo)
buscaEstrela.buscaEstrela()
tempoFim = time.time()
duracao = tempoFim - tempoInicio
print(f"Tempo de execução da busca estrela: {duracao:.4f} segundos")