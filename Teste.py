# from importlib import util
from Node import Node
from queue import Queue
from ArvoreBusca import ArvoreBusca

# node = {
#     "STATE": [x, y],
#     "VALUE": v
# }

# Esses node serão peças de um nó
# A estrutura será chamada de nó

nodeEstadoInicial = Node([7,2,3,6,1,5,4,8,0], 0, None, None)
nodeEstadoObjetivo = Node([0, 1, 2, 3, 4, 5, 6, 7, 8], 0, None, None)


listaNosExplorados = []

arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)



def sequenciaAcoes (estadoAtual):
    listaAcoes = []
    
    while estadoAtual.pai is not None:
        listaAcoes.append(estadoAtual.acao)
        estadoAtual = estadoAtual.pai
        
    return listaAcoes
    

      
      
def buscaEmLargura(problema):
    node = problema
    fila_nos = Queue()
    
    fila_nos.push(node)
    
    while not fila_nos.isEmpty():
        node = fila_nos.pop()
        
        if node.estado in listaNosExplorados:
            continue
        
        listaNosExplorados.append(node.estado)
        
        if arvore.isNoObjetivo(node.estado):
            return sequenciaAcoes(node.estado)


def expande(problema):
    indice = problema.estado.index(0)
    tamanhoLista = len(problema)
    raiz = int(tamanhoLista ** 0.5)
    x = indice // raiz
    y = indice % raiz 
    print(f"X: {x}, Y: {y}")

    # movimento para cima
    if x > 0:
        novoIndice = (x - 1) * raiz + y
        print("Movimento para cima")
    # movimento para baixo
    if x < raiz - 1:
        novoIndice = (x + 1) * raiz + y
        print("Movimento para baixo")
    # movimento para a esquerda
    if y > 0:
        novoIndice = x * raiz + (y - 1)
        print("Movimento para a esquerda")
    # movimento para a direita
    if y < raiz - 1:
        novoIndice = x * raiz + (y + 1)
        print("Movimento para a direita")
 
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


            

# coordenadasNode0 = leitura(estado_inicial)


# print(coordenadasNode0[0], "<--- X\n", coordenadasNode0[1], "<--- Y")


# def posicaoPossivel(coordenadasNode0, lista):
#     x = coordenadasNode0[0]
#     y = coordenadasNode0[1]
#     if(coordenadasNode0[0] == len(lista) - 1):
#         if(coordenadasNode0[1] == len(lista)-1):
#             fila_nos.push(estado_inicial[x - 1] [y])
#             fila_nos.push(estado_inicial[x][y - 1])
            
#         elif(coordenadasNode0[1] < len(lista)-1 and coordenadasNode0[1] > 0):
#             fila_nos.push(estado_inicial[x - 1] [y])
#             fila_nos.push(estado_inicial[x][y + 1])
#             fila_nos.push(estado_inicial[x][y - 1])
#         else:
#             fila_nos.push(estado_inicial[x - 1] [y])
#             fila_nos.push(estado_inicial[x][y + 1])

#     elif(coordenadasNode0[0] < len(lista) - 1 and coordenadasNode0[0] > 0):
#         if(coordenadasNode0[1] == len(lista)-1):
#             fila_nos.push(estado_inicial[x + 1] [y])
#             fila_nos.push(estado_inicial[x][y - 1])
#             fila_nos.push(estado_inicial[x - 1] [y])
#         elif(coordenadasNode0[1] < len(lista)-1 and coordenadasNode0[1] > 0):
#             fila_nos.push(estado_inicial[x + 1] [y])
#             fila_nos.push(estado_inicial[x][y + 1])
#             fila_nos.push(estado_inicial[x][y - 1])
#             fila_nos.push(estado_inicial[x - 1] [y])
#         else:
#             fila_nos.push(estado_inicial[x + 1] [y])
#             fila_nos.push(estado_inicial[x][y + 1])
#             fila_nos.push(estado_inicial[x - 1] [y])
#     else:
#         if(coordenadasNode0[1] == len(lista)-1):
#             fila_nos.push(estado_inicial[x + 1] [y])
#             fila_nos.push(estado_inicial[x][y - 1])
#         elif(coordenadasNode0[1] < len(lista)-1 and coordenadasNode0[1] > 0):
#             fila_nos.push(estado_inicial[x + 1] [y])
#             fila_nos.push(estado_inicial[x  ][y + 1])
#             fila_nos.push(estado_inicial[x][y - 1])
#         else:
#             fila_nos.push(estado_inicial[x + 1] [y])
#             fila_nos.push(estado_inicial[x][y + 1])    


    # if(estado_inicial[x][y] is not None):
    #     lista_nos.append(Node(x, y))
    #     estado_inicial[x][y] = estado_inicial[x+1]
    #     # if(estado_inicial[x+1])
        
        
        # retorna 0, cria função, se 0 do tamanho da lista, se tá no lugar ou se ta no meio
        # Se tiver no lugar, proximo numeto
        # 0 no meio, todas posições
        # 0 no ultimo
        
    



def breadthFirstSearch(problem):
    node = search_tree.getStartNode(problem) 
    
    frontier = util.Queue()
    
    
    frontier.push(node)
   
    explored = set()
    
    while not frontier.isEmpty():
        node = frontier.pop()
        
        if node['STATE'] in explored:
            
            continue
        
        explored.add(node['STATE'])
        
        if problem.isGoalState(node['STATE']):
            
            return search_tree.getActionSequence(node)
        
        for sucessor in problem.expand(node['STATE']):
            child_node = search_tree.getChildNode(sucessor, node)
            frontier.push(child_node)
            
    return[]



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