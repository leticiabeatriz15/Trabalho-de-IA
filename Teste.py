# from importlib import util
from Node import Node
from queue import Queue

# node = {
#     "STATE": [x, y],
#     "VALUE": v
# }

node0 = Node(0, 0)    
node1 = Node(0, 1)
node2 = Node(0, 2)

node3 = Node(1, 0)    
node4 = Node(1, 1)
node5 = Node(1, 2)

node6 = Node(2, 0)    
node7 = Node(2, 1)
node8 = Node(2, 2)

estado_inicial = [[node7, node2, node3],[node6, node1, node5],[node4, node8, node0]]


# for i,j in estado_inicial:
#     breadthFirstSearch()

fila_nos = Queue()
# leitura(estado_inicial, 0,0)

def leitura (lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            # fila_nos.put(Node[i][j])
            noAtual = Node(lista[i][j].getX(), lista[i][j].getY())
            if(noAtual.getX() == 0 and noAtual.getY() == 0):
                 return i,j
            
            

coordenadasNode0 = leitura(estado_inicial)
print(coordenadasNode0[0], "<--- X\n", coordenadasNode0[1], "<--- Y")
listaDePosicoes = []

def posicaoPossivel(coordenadasNode0, lista):
    x = coordenadasNode0[0]
    y = coordenadasNode0[1]
    if(coordenadasNode0[0] == len(lista) - 1):
        if(coordenadasNode0[1] == len(lista)-1):
            listaDePosicoes.append(estado_inicial[x - 1] [y])
            listaDePosicoes.append(estado_inicial[x][y - 1])
        elif(coordenadasNode0[1] < len(lista)-1 and coordenadasNode0[1] > 0):
            listaDePosicoes.append(estado_inicial[x - 1] [y])
            listaDePosicoes.append(estado_inicial[x][y + 1])
            listaDePosicoes.append(estado_inicial[x][y - 1])
        else:
            listaDePosicoes.append(estado_inicial[x - 1] [y])
            listaDePosicoes.append(estado_inicial[x][y + 1])

    elif(coordenadasNode0[0] < len(lista) - 1 and coordenadasNode0[0] > 0):
        if(coordenadasNode0[1] == len(lista)-1):
            listaDePosicoes.append(estado_inicial[x + 1] [y])
            listaDePosicoes.append(estado_inicial[x][y - 1])
            listaDePosicoes.append(estado_inicial[x - 1] [y])
        elif(coordenadasNode0[1] < len(lista)-1 and coordenadasNode0[1] > 0):
            listaDePosicoes.append(estado_inicial[x + 1] [y])
            listaDePosicoes.append(estado_inicial[x][y + 1])
            listaDePosicoes.append(estado_inicial[x][y - 1])
            listaDePosicoes.append(estado_inicial[x - 1] [y])
        else:
            listaDePosicoes.append(estado_inicial[x + 1] [y])
            listaDePosicoes.append(estado_inicial[x][y + 1])
            listaDePosicoes.append(estado_inicial[x - 1] [y])
    else:
        if(coordenadasNode0[1] == len(lista)-1):
            listaDePosicoes.append(estado_inicial[x + 1] [y])
            listaDePosicoes.append(estado_inicial[x][y - 1])
        elif(coordenadasNode0[1] < len(lista)-1 and coordenadasNode0[1] > 0):
            listaDePosicoes.append(estado_inicial[x + 1] [y])
            listaDePosicoes.append(estado_inicial[x][y + 1])
            listaDePosicoes.append(estado_inicial[x][y - 1])
        else:
            listaDePosicoes.append(estado_inicial[x + 1] [y])
            listaDePosicoes.append(estado_inicial[x][y + 1])    


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
    # Função de getStartNode 
    # search_tree
    
    # frontier = util.Queue()
    # Criando uma fila
    
#     frontier.push(node)
#     # Adicionando nó inicial
#     explored = set()
    
#     while not frontier.isEmpty():
#         node = frontier.pop()
        
#         if node['STATE'] in explored:
#             # STATE?
#             continue
        
#         explored.add(node['STATE'])
        
#         if problem.isGoalState(node['STATE']):
#             # Funcão
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
