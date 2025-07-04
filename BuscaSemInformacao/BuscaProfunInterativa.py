from Node import Node
from ArvoreBusca import ArvoreBusca
from Movimentacoes import caminhoPercorrido, sequenciaAcoes

class BuscaProfundidadeIterativa:
    def __init__(self, nodeEstadoInicial, nodeEstadoObjetivo, limite):
        self.nodeEstadoInicial = nodeEstadoInicial
        self.nodeEstadoObjetivo = nodeEstadoObjetivo
        self.arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)
        self.limite = limite

    def buscaProfundidadeIterativa(self):
        for profundidade in range(0, self.limite):
            node = self.nodeEstadoInicial
            listaNosExplorados = set()
            pilha_nos = []
            pilha_nos.append(node)
            listaNosExplorados.add(tuple(node.estado))  

            while pilha_nos:
                node = pilha_nos.pop()

                if self.arvore.isNoObjetivo(node):
                    print("Ações:", sequenciaAcoes(node))
                    print("Estado objetivo encontrado!")
                    print('Caminho percorrido: ', caminhoPercorrido(node))
                    print('Nós explorados: ', len(listaNosExplorados))
                    return listaNosExplorados
                            
                if node.profundidade < self.limite:
                    self.expande(node, pilha_nos, listaNosExplorados)    
                    
                    
                
            print('Solução não encontrada dentro do limite estabelecido!')          
        return None

    def expande(self, problema, pilha_nos, listaNosExplorados):
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
