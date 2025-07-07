
from BuscaSemInformacao.Node import Node
from queue import Queue
from ArvoreBusca import ArvoreBusca
from Movimentacoes import sequenciaAcoes, caminhoPercorrido

class BuscaLargura:
    def __init__(self, nodeEstadoInicial, nodeEstadoObjetivo):
        self.nodeEstadoInicial = nodeEstadoInicial
        self.nodeEstadoObjetivo = nodeEstadoObjetivo
        self.arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)
        
    def buscaLargura(self):
        node = self.nodeEstadoInicial
        listaNosExplorados = []
        
        fila_nos = Queue()
        fila_nos.put(node)
        
        while not fila_nos.empty():
            node = fila_nos.get()

            if node.estado in listaNosExplorados:
                continue

            listaNosExplorados.append(node.estado)
            
            if self.arvore.isNoObjetivo(node):
                print("Ações:", sequenciaAcoes(node))
                print("\033[35mEstado objetivo encontrado!\033[0m")
                print('Caminho percorrido:', caminhoPercorrido(node))
                print('Total de passos: ', len(caminhoPercorrido(node)))
                print('Nós explorados: ', len(listaNosExplorados))
            
                return sequenciaAcoes(node)

            
            self.expande(node, fila_nos)
            
    def expande(self, problema, fila_nos):
        estado_atual = problema.estado
        indice = estado_atual.index(0)
        tamanhoLista = len(estado_atual)
        raiz = int(tamanhoLista ** 0.5)
        x = indice // raiz
        y = indice % raiz 


        if x > 0:
            novoIndice = (x - 1) * raiz + y
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            fila_nos.put(Node(novo_estado, 0, "para cima", problema, None))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            fila_nos.put(Node(novo_estado, 0, "para baixo", problema, None))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            fila_nos.put(Node(novo_estado, 0, "para a esquerda", problema, None))

        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novo_estado = estado_atual[:]
            novo_estado[indice], novo_estado[novoIndice] = novo_estado[novoIndice], novo_estado[indice]
            fila_nos.put(Node(novo_estado, 0, "para direita", problema, None))



