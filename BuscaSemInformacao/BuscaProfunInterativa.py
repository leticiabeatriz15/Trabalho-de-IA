from BuscaSemInformacao.Node import Node
from ArvoreBusca import ArvoreBusca
from Movimentacoes import caminhoPercorrido, sequenciaAcoes

class BuscaProfundidadeIterativa:
    def __init__(self, nodeEstadoInicial, nodeEstadoObjetivo, limite):
        self.nodeEstadoInicial = nodeEstadoInicial
        self.nodeEstadoObjetivo = nodeEstadoObjetivo
        self.arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)
        self.limite = limite
        self.nosExpandidos = 0

    def buscaProfundidadeIterativa(self):
        for profundidade in range(0, self.limite):
            node = self.nodeEstadoInicial
            listaNosExplorados = set()
            pilhaNos = []
            pilhaNos.append(node)
            listaNosExplorados.add(tuple(node.estado))  

            while pilhaNos:
                node = pilhaNos.pop()

                if self.arvore.isNoObjetivo(node):
                    print("Ações:", sequenciaAcoes(node))
                    print("Estado objetivo encontrado!")
                    # print('Caminho percorrido: ', (caminhoPercorrido(node)))
                    print('Total de passos: ', len(caminhoPercorrido(node)))
                    print('Nós expandidos: ', len(listaNosExplorados))
                    print('Estados expandidos: ', self.nosExpandidos)
                    print('Profundidade da solução: ', len(caminhoPercorrido(node)) - 1)
                    return listaNosExplorados
                            
                if node.profundidade < self.limite:
                    self.expande(node, pilhaNos, listaNosExplorados)    
                    
                    
                
        print('Solução não encontrada dentro do limite estabelecido!')          
        return None

    def expande(self, problema, pilhaNos, listaNosExplorados):
        self.nosExpandidos += 1
        estadoAtual = problema.estado
        indice = estadoAtual.index(0)
        tamanhoLista = len(estadoAtual)
        raiz = int(tamanhoLista ** 0.5)
        x = indice // raiz
        y = indice % raiz 

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            if tuple(novoEstado) not in listaNosExplorados:
                pilhaNos.append(Node(novoEstado, 0, "para baixo", problema, problema.profundidade + 1))
                listaNosExplorados.add(tuple(novoEstado))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            if tuple(novoEstado) not in listaNosExplorados:
                pilhaNos.append(Node(novoEstado, 0, "para a esquerda", problema, problema.profundidade + 1))
                listaNosExplorados.add(tuple(novoEstado))

        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            
            if tuple(novoEstado) not in listaNosExplorados:
                pilhaNos.append(Node(novoEstado, 0, "para direita", problema, problema.profundidade + 1))
                listaNosExplorados.add(tuple(novoEstado))

        if x > 0:
            novoIndice = (x - 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            
            if tuple(novoEstado) not in listaNosExplorados:
                pilhaNos.append(Node(novoEstado, 0, "para cima", problema, problema.profundidade + 1))
                listaNosExplorados.add(tuple(novoEstado))
