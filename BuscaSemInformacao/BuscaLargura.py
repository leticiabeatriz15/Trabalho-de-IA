
from BuscaSemInformacao.Node import Node
from queue import Queue
from ArvoreBusca import ArvoreBusca
from Movimentacoes import sequenciaAcoes, caminhoPercorrido

class BuscaLargura:
    def __init__(self, nodeEstadoInicial, nodeEstadoObjetivo):
        self.nodeEstadoInicial = nodeEstadoInicial
        self.nodeEstadoObjetivo = nodeEstadoObjetivo
        self.arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)
        self.nosExpandidos = 0
        
    def buscaLargura(self):
        node = self.nodeEstadoInicial
        listaNosExplorados = []
        
        filaNos = Queue()
        filaNos.put(node)
        
        while not filaNos.empty():
            node = filaNos.get()

            if node.estado in listaNosExplorados:
                continue

            listaNosExplorados.append(node.estado)
            
            if self.arvore.isNoObjetivo(node):
                print("\033[35mEstado objetivo encontrado!\033[0m")
                print("Ações:", sequenciaAcoes(node))
                print('Caminho percorrido:', caminhoPercorrido(node))
                print('Total de passos: ', len(caminhoPercorrido(node)))
                print('Nós expandidos: ', len(listaNosExplorados))
                print('Estados expandidos: ', self.nosExpandidos)
                print('Profundidade da solução: ', len(caminhoPercorrido(node)) - 1)
            
                return sequenciaAcoes(node)
            
            self.expande(node, filaNos)
            

    def expande(self, problema, filaNos):
        self.nosExpandidos += 1
        estadoAtual = problema.estado
        indice = estadoAtual.index(0)
        tamanhoLista = len(estadoAtual)
        raiz = int(tamanhoLista ** 0.5)
        x = indice // raiz
        y = indice % raiz 

        if x > 0:
            novoIndice = (x - 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            filaNos.put(Node(novoEstado, 0, "para cima", problema, None))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            filaNos.put(Node(novoEstado, 0, "para baixo", problema, None))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            filaNos.put(Node(novoEstado, 0, "para esquerda", problema, None))
        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            filaNos.put(Node(novoEstado, 0, "para direita", problema, None))