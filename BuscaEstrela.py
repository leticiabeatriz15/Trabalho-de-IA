import heapq
from NodeComInformacao import NodeI
from ArvoreBusca import ArvoreBusca
from Movimentacoes import sequenciaAcoes, caminhoPercorrido
import time



# nodeEstadoInicial = NodeI([1, 2, 3, 4, 0, 5, 6, 7, 8], 0, None, None, None) #Busca 3*3
# nodeEstadoObjetivo = NodeI([0,1,2,3,4,5,6,7,8], 0, None, None, None)


nodeEstadoInicial = NodeI([1, 2, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0, None, None, None) #Busca 4*4
nodeEstadoObjetivo = NodeI([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0, None, None, None)

# nodeEstadoInicial = NodeI([1,2,3,4,0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], 0, None, None, None)
# nodeEstadoObjetivo = NodeI([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], 0, None, None, None)

arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)

limite_profundidade = 30

def heuristica (estado_atual, objetivo):
    
    custo_restante = 0
    for i in range(len(estado_atual)):
        if estado_atual[i] != 0 and estado_atual[i] != objetivo[i]:
            custo_restante += 1
    
    return custo_restante
    
        
    
def buscaEstrela(estadoInicial, estadoObjetivo):
    # nosExpandidos = 0
    fronteira = []
    listaNosExplorados = set()
    limite_atingido = False
    
    heuristica_inicial = heuristica(estadoInicial.estado, estadoObjetivo.estado)
    heapq.heappush(fronteira, (estadoInicial.custo + heuristica_inicial, estadoInicial))
    
    while fronteira:
        
        prioridade, estado_atual = heapq.heappop(fronteira)
        
        if tuple(estado_atual.estado) in listaNosExplorados:
            continue
        
        
        
        if arvore.isNoObjetivo(estado_atual):
            print('Estado objetivo encontrado!')
            print('Ações: ', sequenciaAcoes(estado_atual))
            print('Caminho percorrido: ', caminhoPercorrido(estado_atual))
            print('Total de passos: ', len(caminhoPercorrido(estado_atual)))
            print('Nós expandidos', len(listaNosExplorados))
            # print('Estados expandidos: ', nosExpandidos)
            print('Profundidade da solução: ', len(caminhoPercorrido(estado_atual)) - 1)
            return 
        
        listaNosExplorados.add(tuple(estado_atual.estado))
        
        filhos = expande(estado_atual)
        
        for filho in filhos:
            if (tuple(filho.estado)) not in listaNosExplorados:
                if filho.custo <= limite_profundidade:
                    fx = filho.custo + filho.heuristica
                    heapq.heappush(fronteira, (fx, filho))
                else:
                    limite_atingido = True
                    
    if limite_atingido:
         print('Limite de profundidade atingido!')
         
         
def expande(problema):
        # global nosExpandidos 
        # nosExpandidos += 1
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
            filhos.append(NodeI(novo_estado, problema.custo + 1, "para cima", problema, heuristicaNo))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, problema.custo + 1, "para baixo", problema, heuristicaNo))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, problema.custo + 1, "para esquerda", problema, heuristicaNo))
        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, problema.custo + 1, "para direita", problema, heuristicaNo))

        return filhos

tempo_inicio = time.time()
buscaEstrela(nodeEstadoInicial, nodeEstadoObjetivo)
tempo_fim = time.time()
duracao = tempo_fim - tempo_inicio

print(f'Tempo de execução da busca estrela: {duracao:.4f} segundos')
