import heapq

from Node import Node

from ArvoreBusca import ArvoreBusca
from Movimentacoes import sequenciaAcoes, caminhoPercorrido

arvore = ArvoreBusca()

nodeEstadoInicial = Node([1,2,5,3,4,8,6,0,7], 0, None, None, None) #Busca 3*3
nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None, None)


def heuristica (estado_atual, objetivo):
    
    custo_restante = 0
    for i in range(len(estado_atual)):
        if estado_atual[i] != 0 and estado_atual[i] != objetivo[i]:
            custo_restante += 1
    
    return custo_restante
    
        
    
def buscaEstrela(estadoInicial, estadoObjetivo):
    fronteira = []
    listaNosExplorados = set()
    
    heuristica = heuristica(estadoInicial.estado, estadoObjetivo.estado)
    heapq.heappush(fronteira, (estadoInicial.custo + heuristica, estadoInicial))
    
    while fronteira:
        
        estado_atual = heapq.heappop(fronteira)
        
        if tuple(estado_atual.estado) in listaNosExplorados:
            continue
        
        
        
        if arvore.isNoObjetivo(estado_atual):
            print('Estado objetivo encontrado!')
            print('Ações: ', sequenciaAcoes(estado_atual))
            print('Caminho percorrido: ', caminhoPercorrido(estado_atual))
            print('Total de passos: ', len(caminhoPercorrido(estado_atual)))
            return 
        
        listaNosExplorados.add(tuple(estado_atual.estado))
        filhos = expande(estado_atual)
        
        for filho in filhos:
            if (tuple(filho.estado)) not in listaNosExplorados:
                fx = filho.custo + filho.heuristica
                heapq.heappush(fronteira, (fx, filho))
        
        
def expande(problema):
        estado_atual = problema.estado
        indice = estado_atual.index(0)
        tamanhoLista = len(estado_atual)
        raiz = int(tamanhoLista ** 0.5)
        x = indice // raiz
        y = indice % raiz 

        filhos = []

        if x > 0:
            novoIndice = (x - 1) * raiz + y
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(Node(novo_estado, 0, "para cima", problema, heuristicaNo))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(Node(novo_estado, 0, "para baixo", problema, heuristicaNo))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(Node(novo_estado, 0, "para esquerda ", problema, heuristicaNo))
        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(Node(novo_estado, 0, "para direita", problema, heuristicaNo))

        return filhos
