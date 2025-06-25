# from importlib import util
from Node import Node
from queue import Queue
from ArvoreBusca import ArvoreBusca

nodeEstadoInicial = Node([1,2,3,4,0,5,6,7,8], 0, None, None)
nodeEstadoObjetivo = Node([0, 1, 2, 3, 4, 5, 6, 7, 8], 0, None, None)



arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)




listaNosExplorados = []

def sequenciaAcoes (estadoAtual):
    listaAcoes = []
    
    while estadoAtual.pai is not None:
        listaAcoes.append(estadoAtual.acao)
        estadoAtual = estadoAtual.pai
        
    return listaAcoes
    

# def verificaFilhosEmFila(filhosExpandidos, fila):
    
#     for i in range(len(filhosExpandidos)):
#         if filhosExpandidos[i] in fila.queue:
#             continue
        
#         fila.put(Node(filhosExpandidos[i], 0, None, None))


      
def buscaEmLargura(problema):
    node = problema
    
    fila_nos = Queue()
    # controle_fila = []
    
    fila_nos.put(node)
    
    while not fila_nos.empty():
        node = fila_nos.get()
        
        if node.estado in listaNosExplorados:
            continue
        # if node.estado in listaNosExplorados:
        #     continue
        
        listaNosExplorados.append(node.estado)
        
        if arvore.isNoObjetivo(node):
            print("Estado objetivo encontrado!")
            print("Ações:", sequenciaAcoes(node))
            return sequenciaAcoes(node)
        
        expande(node, fila_nos)
        
        # print("Fila: ")
        # for item in fila_nos.queue:
        #     print(item.estado)
        # print('Nós explorados', listaNosExplorados)
        
    


def expande(problema, fila_nos):
    estado_atual = problema.estado
    indice = estado_atual.index(0)
    tamanhoLista = len(estado_atual)
    raiz = int(tamanhoLista ** 0.5)
    x = indice // raiz
    y = indice % raiz 
    # print(f"X: {x}, Y: {y}")

    filhos = []  # lista de novos estados gerados

    # movimento para cima
    if x > 0:
        novoIndice = (x - 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para cima", problema))

    # movimento para baixo
    if x < raiz - 1:
        novoIndice = (x + 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para baixo", problema))

    # movimento para a esquerda
    if y > 0:
        novoIndice = x * raiz + (y - 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para a esquerda", problema))

    # movimento para a direita
    if y < raiz - 1:
        novoIndice = x * raiz + (y + 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        fila_nos.put(Node(novo_estado, 0, "para direita", problema))

    return filhos


buscaEmLargura(nodeEstadoInicial)


    # indice == 0 (0,1...)
    #indice > 0 and indice < problema.len() - 1 (...,0,...)
    # indice == problema.len() - 1 (..., 0)        

# node0 = Node(0, 0)    
# node1 = Node(0, 1)
# node2 = Node(0, 2)

# node3 = Node(1, 0)    
# node4 = Node(1, 1)
# node5 = Node(1, 2)

# node6 = Node(2, 0)    
# node7 = Node(2, 1)
# node8 = Node(2, 2)

# estado_inicial = [[node7, node2, node3],[node6, node1, node5],[node4, node8, node0]]


# for i,j in estado_inicial:
#     breadthFirstSearch()


# leitura(estado_inicial, 0,0)


            

    # if(estado_inicial[x][y] is not None):
    #     lista_nos.append(Node(x, y))
    #     estado_inicial[x][y] = estado_inicial[x+1]
    #     # if(estado_inicial[x+1])
        
        
        # retorna 0, cria função, se 0 do tamanho da lista, se tá no lugar ou se ta no meio
        # Se tiver no lugar, proximo numeto
        # 0 no meio, todas posições
        # 0 no ultimo
        
    



# def breadthFirstSearch(problem):
#     node = search_tree.getStartNode(problem) 
    
#     frontier = util.Queue()
    
    
#     frontier.push(node)
   
#     explored = set()
    
#     while not frontier.isEmpty():
#         node = frontier.pop()
        
#         if node['STATE'] in explored:
            
#             continue
        
#         explored.add(node['STATE'])
        
#         if problem.isGoalState(node['STATE']):
            
#             return search_tree.getActionSequence(node)
        
#         for sucessor in problem.expand(node['STATE']):
#             child_node = search_tree.getChildNode(sucessor, node)
#             frontier.push(child_node)
            
#     return[]



# estado_objetivo = [[node0, node1, node2], [node3, node4, node5], [node6, node7, node8]]

# Dicionário com lista como valor
# dicionario_lista = {
#     "frutas": ["maçã", "banana", "laranja"],
#     "numeros": [1, 2, 3, 4, 5]
# }
#[[231],[234]] 



# 1,2,3
# 4,0,5
# 7,8,6         