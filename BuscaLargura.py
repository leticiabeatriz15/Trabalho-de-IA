from Node import Node
from queue import Queue
from ArvoreBusca import ArvoreBusca

nodeEstadoInicial = Node([1,2,3,4,0,5,6,7,8], 0, None, None) #Busca 3*3
nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None)

# nodeEstadoInicial = Node([4,1,2,3,0,5,6,7,8,9,10,11,12,13,14,15], 0, None, None) #Busca 4*4
# nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0, None, None)

# nodeEstadoInicial = Node([5,1,2,3,4,0,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], 0, None, None) #Busca 5*5
# nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], 0, None, None)

arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)

listaNosExplorados = []

def sequenciaAcoes (estadoAtual):
    listaAcoes = []
    
    while estadoAtual.pai is not None:
        listaAcoes.append(estadoAtual.acao)
        estadoAtual = estadoAtual.pai
        
    return listaAcoes
      
def buscaEmLargura(problema):
    node = problema
    
    fila_nos = Queue()
    fila_nos.put(node)
    
    while not fila_nos.empty():
        node = fila_nos.get()
        
        if node.estado in listaNosExplorados:
            continue

        listaNosExplorados.append(node.estado)
        
        if arvore.isNoObjetivo(node):
            print("Ações:", sequenciaAcoes(node))
            print("Estado objetivo encontrado!")
            
            return sequenciaAcoes(node)
        
        expande(node, fila_nos)
        print("Nós explorados até agora:", len(listaNosExplorados))
        print("Estado atual:", node.estado)

def expande(problema, fila_nos):
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
        fila_nos.put(Node(novo_estado, 0, "para cima", problema))

    if x < raiz - 1:
        novoIndice = (x + 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para baixo", problema))

    if y > 0:
        novoIndice = x * raiz + (y - 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para a esquerda", problema))

    
    if y < raiz - 1:
        novoIndice = x * raiz + (y + 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para direita", problema))

    return filhos


buscaEmLargura(nodeEstadoInicial)