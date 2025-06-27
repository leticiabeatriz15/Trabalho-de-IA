from Node import Node

from ArvoreBusca import ArvoreBusca

nodeEstadoInicial = Node([3,1,2,0,4,5,6,7,8], 0, None, None) #Busca 3*3
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
        
    return listaAcoes[::-1]

def caminhoPercorrido(estadoAtual):
    caminho = []
    while estadoAtual.pai is not None:
        caminho.append(estadoAtual.estado)
        estadoAtual = estadoAtual.pai
        
        for elemento in caminho:
            textoOrganizado = ""
            for i in elemento:
                if i == 0:
                    textoOrganizado += "\033[32m"+ str(i) + "\033[0m"
                else:
                    textoOrganizado += str(i)
            
        print(textoOrganizado)# print (elemento[i])
    return caminho[::-1] 
      
def buscaEmProfundidade(problema):
    node = problema
    
    pilha_nos = []
    pilha_nos.append(node)
    
    while pilha_nos:
        
        if node.estado in listaNosExplorados:
            continue

        listaNosExplorados.append(node.estado)
        print('Nó: ', node.estado)
        
        if arvore.isNoObjetivo(node):
            print("Ações:", sequenciaAcoes(node))
            print("Estado objetivo encontrado!")
            print('Caminho percorrido: ', caminhoPercorrido(node))
            
            return sequenciaAcoes(node)
        
        expande(node, pilha_nos)
        node = pilha_nos.pop()
    
      
def expande(problema, pilha_nos):
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
        
        if novo_estado not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para cima", problema))

    if x < raiz - 1:
        novoIndice = (x + 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        if novo_estado not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para baixo", problema))

    if y > 0:
        novoIndice = x * raiz + (y - 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        if novo_estado not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para a esquerda", problema))

    
    if y < raiz - 1:
        novoIndice = x * raiz + (y + 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        
        if novo_estado not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para direita", problema))

    return filhos


buscaEmProfundidade(nodeEstadoInicial)
print("Quantidade de nós explorados:", len(listaNosExplorados))