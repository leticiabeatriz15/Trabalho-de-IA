from BuscaSemInformacao.Node import Node
from ArvoreBusca import ArvoreBusca
from Movimentacoes import sequenciaAcoes, caminhoPercorrido


class BuscaProfundidade:
    def __init__(self, nodeEstadoInicial, nodeEstadoObjetivo):
        self.nodeEstadoInicial = nodeEstadoInicial
        self.nodeEstadoObjetivo = nodeEstadoObjetivo
        self.arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)
        self.nosExpandidos = 0

    def buscaProfundidade(self):
        node = self.nodeEstadoInicial
        listaNosExplorados = set()
        pilhaNos = []
        pilhaNos.append(node)
    
        
        while pilhaNos:
            node = pilhaNos.pop()
            
            
            if (tuple(node.estado) in listaNosExplorados):
                continue
            
            listaNosExplorados.add(tuple(node.estado))
            
            if self.arvore.isNoObjetivo(node):
                # print("Ações:", sequenciaAcoes(node))
                print("\033[35mEstado objetivo encontrado!\033[0m")
                # print('Caminho percorrido: ', caminhoPercorrido(node))
                print('Total de passos: ', len(caminhoPercorrido(node)))
                print('Nós expandidos: ', len(listaNosExplorados))
                print('Estados expandidos: ', self.nosExpandidos)
                print('Profundidade da solução: ', len(caminhoPercorrido(node)) - 1)
            
                return listaNosExplorados
            
                
            self.expande(node, pilhaNos)
            
        print('Nenhuma solução encontrada!')
        return listaNosExplorados

    def expande(self, problema, pilhaNos):
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
            pilhaNos.append(Node(novoEstado, 0, "para baixo", problema, None))
                

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            pilhaNos.append(Node(novoEstado, 0, "para a esquerda", problema, None))
                

        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            pilhaNos.append(Node(novoEstado, 0, "para direita", problema, None))
                

        if x > 0:
            novoIndice = (x - 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            pilhaNos.append(Node(novoEstado, 0, "para cima", problema, None))
    