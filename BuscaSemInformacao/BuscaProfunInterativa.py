from Node import Node
from ArvoreBusca import ArvoreBusca
from Movimentacoes import caminhoPercorrido, sequenciaAcoes

import time

nodeEstadoInicial = Node([3,1,2,4,0,5,6,7,8], 0, None, None, 0, 3) #Busca 3*3

nodeEstadoObjetivo = Node([0,1,2,3,4,5,6,7,8], 0, None, None, 0, 0)


arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)
def sequenciaAcoes (estadoAtual):
    listaAcoes = []
    
    while estadoAtual.pai is not None:
        listaAcoes.append(estadoAtual.acao)
        estadoAtual = estadoAtual.pai
        
    return listaAcoes[::-1]

def caminhoPercorrido(estadoAtual):
    caminho = []
    custo = 0
    while estadoAtual.pai is not None:
        caminho.append(estadoAtual.estado)
        custo += 1
        estadoAtual = estadoAtual.pai
      

    # for elemento in caminho[::-1]:
    #     textoOrganizado = ""
    #     for i in elemento:
    #         if i == 0:
    #             textoOrganizado += "\033[32m" + str(i) + "\033[0m"
    #         else:
    #             textoOrganizado += str(i)
    #     print(textoOrganizado)

    print("Custo total: ", custo)
    return caminho[::-1]

def buscaProfundidadeIterativa(problema, limite):
    
    for profundidade in range(0, limite):
        node = problema
        listaNosExplorados = set()
        pilha_nos = []
        pilha_nos.append(node)
        listaNosExplorados.add(tuple(node.estado))  
    
        while pilha_nos:
            node = pilha_nos.pop()
            
            # if tuple(node.estado) in listaNosExplorados:
            #     continue

            if arvore.isNoObjetivo(node):
                print("Ações:", sequenciaAcoes(node))
                print("Estado objetivo encontrado!")
                print('Caminho percorrido: ', caminhoPercorrido(node))
                print('Nós explorados: ', len(listaNosExplorados))
                return listaNosExplorados
                
                
               
                
            
            if node.profundidade < limite:
                expande(node, pilha_nos, listaNosExplorados)    
                
               
        
    print('Solução não encontrada dentro do limite estabelecido!')          
    return None

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
            pilha_nos.append(Node(novo_estado, 0, "para baixo", problema, problema.profundidade + 1))
            listaNosExplorados.add(tuple(novo_estado))

    if y > 0:
        novoIndice = x * raiz + (y - 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para a esquerda", problema, problema.profundidade + 1))
            listaNosExplorados.add(tuple(novo_estado))

    
    if y < raiz - 1:
        novoIndice = x * raiz + (y + 1)
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para direita", problema, problema.profundidade + 1))
            listaNosExplorados.add(tuple(novo_estado))

    if x > 0:
        novoIndice = (x - 1) * raiz + y
        novo_estado = estado_atual[:]
        novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
        
        if tuple(novo_estado) not in listaNosExplorados:
            pilha_nos.append(Node(novo_estado, 0, "para cima", problema, problema.profundidade + 1))
            listaNosExplorados.add(tuple(novo_estado))

tempo_inicio = time.time()
buscaProfundidadeIterativa(nodeEstadoInicial, 2)
tempo_fim = time.time()
duracao = tempo_fim - tempo_inicio


print(f"Tempo de execução: {duracao:.4f} segundos")