from NodeComInformacao import NodeI
from Movimentacoes import sequenciaAcoes, caminhoPercorrido
from ArvoreBusca import ArvoreBusca
import time 

nodeEstadoInicial = NodeI([1, 2, 3, 4, 0, 5, 6, 7, 8],0, None, None, 3) #Busca 3*3

nodeEstadoObjetivo = NodeI([0,1,2,3,4,5,6,7,8], 0, None, None, 0)

arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)

def heuristica_pecas(estado_atual, objetivo):
    pecas_fora_do_lugar = 0
    for i in range(len(estado_atual)):
        if estado_atual[i] != 0 and estado_atual[i] != objetivo[i]:
            pecas_fora_do_lugar += 1
            
    return pecas_fora_do_lugar
            
def buscaGulosa(estadoInicial, estadoObjetivo):
    estado_atual = estadoInicial
    listaNosExplorados = set()
    
    
    while True:
        if arvore.isNoObjetivo(estado_atual):
            
            print('Estado objetivo encontrado!')
            print('Ações: ', sequenciaAcoes(estado_atual))
            print('Caminho percorrido: ', caminhoPercorrido(estado_atual))
            print('Total de passos: ',len(caminhoPercorrido(estado_atual)))
            print('Nós explorados: ', len(listaNosExplorados))
            return 
        
        listaNosExplorados.add(tuple(estado_atual.estado))
        filhos = expande(estado_atual)
        
        
     
        melhor = None
        melhor_valor = float('inf')
        
       

        for filho in filhos:
            valor = heuristica_pecas(filho.estado, estadoObjetivo.estado)
            if valor < melhor_valor:
                melhor = filho
                melhor_valor = valor
        
        
        if melhor is None:
            print('Sem caminhos disponíveis')
            return 
        
        estado_atual = melhor
        
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
            heuristicaNo = heuristica_pecas(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, 0, "para cima", problema, heuristicaNo))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica_pecas(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, 0, "para baixo", problema, heuristicaNo))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica_pecas(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, 0, "para esquerda ", problema, heuristicaNo))
        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            heuristicaNo = heuristica_pecas(novo_estado, nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novo_estado, 0, "para direita", problema, heuristicaNo))

        return filhos
            
       
tempo_inicio = time.time()
buscaGulosa(nodeEstadoInicial, nodeEstadoObjetivo)
tempo_fim = time.time()

duracao = tempo_fim - tempo_inicio

print(f"Tempo de execução da busca gulosa: {duracao:.4f} segundos")
