from ArvoreBusca import ArvoreBusca
# from BuscaProfundidade import expande

from Node import Node

nodeEstadoInicial = Node([3,1,2,4,0,5,6,7,8], 0, None, None) #Busca 3*3

nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None)


arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)

def buscaProfundidadeIterativa(problema, limite):
    print("Iniciando busca em profundidade iterativa...")
    node = problema
    listaNosExplorados = set()
    pilha_nos = []
    pilha_nos.append(node)
    listaNosExplorados.add(tuple(node.estado))  
    
    contador = 0
    while pilha_nos:
        node = pilha_nos.pop()
        contador += 1

        if contador == limite and arvore.isNoObjetivo(node) is False:
            print("Limite de profundidade atingido. Expandindo nós...", limite, contador)
            limite += 1
            continue
        
        elif arvore.isNoObjetivo(node):
            # print("Ações:", sequenciaAcoes(node))
            print("Estado objetivo encontrado!")
            # print('Caminho percorrido: ', caminhoPercorrido(node))
            return listaNosExplorados
        
        expande(node, pilha_nos, listaNosExplorados)
#         # print('Nó: ', node.estado)

    return listaNosExplorados
    # while True:
    #     resultado = buscaEmProfundidade(problema, limite)
    #     if resultado != limite:
    #         return resultado
    #     limite += 1

def expande(problema, pilha_nos, listaNosExplorados):
    estado_atual = problema.estado
    indice = estado_atual.index(0)
    tamanhoLista = len(estado_atual)
    raiz = int(tamanhoLista ** 0.5)
    x = indice // raiz
    y = indice % raiz 


    

    if x < raiz - 1:
        novoIndice = (x + 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para baixo", problema))
            listaNosExplorados.add(tuple(novo_estado))

    if y > 0:
        novoIndice = x * raiz + (y - 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para a esquerda", problema))
            listaNosExplorados.add(tuple(novo_estado))

    
    if y < raiz - 1:
        novoIndice = x * raiz + (y + 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para direita", problema))
            listaNosExplorados.add(tuple(novo_estado))

    if x > 0:
        novoIndice = (x - 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para cima", problema))
            listaNosExplorados.add(tuple(novo_estado))

buscaProfundidadeIterativa(nodeEstadoInicial, 2)


