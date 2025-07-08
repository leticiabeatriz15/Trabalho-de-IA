from BuscaComInformacao.NodeComInformacao import NodeI
from Movimentacoes import sequenciaAcoes, caminhoPercorrido
from ArvoreBusca import ArvoreBusca
import heapq

class BuscaEstrela:
    def __init__(self, NodeEstadoInicial, NodeEstadoObjetivo):
        self.NodeEstadoInicial = NodeEstadoInicial
        self.NodeEstadoObjetivo = NodeEstadoObjetivo
        self.arvore = ArvoreBusca(NodeEstadoInicial, NodeEstadoObjetivo)
        self.limiteProfundidade = 30
        self.nosExpandidos = 0

    def buscaEstrela(self):
        fronteira = []
        listaNosExplorados = set()
        limiteAtingido = False
        
        heuristicaInicial = self.heuristica(self.NodeEstadoInicial.estado, self.NodeEstadoObjetivo.estado)
        heapq.heappush(fronteira, (self.NodeEstadoInicial.custo + heuristicaInicial, self.NodeEstadoInicial))
        
        while fronteira:
            prioridade, estadoAtual = heapq.heappop(fronteira)
            
            if tuple(estadoAtual.estado) in listaNosExplorados:
                continue
    
            if self.arvore.isNoObjetivo(estadoAtual):
                print('\033[35mEstado objetivo encontrado!\033[0m')
                print('Ações: ', sequenciaAcoes(estadoAtual))
                print('Caminho percorrido: ', caminhoPercorrido(estadoAtual))
                print('Total de passos: ', len(caminhoPercorrido(estadoAtual)))
                print('Nós expandidos', len(listaNosExplorados))
                print('Estados expandidos: ', self.nosExpandidos)
                print('Profundidade da solução: ', len(caminhoPercorrido(estadoAtual)) - 1)
                return 
            
            listaNosExplorados.add(tuple(estadoAtual.estado))
            
            filhos = self.expande(estadoAtual)
            
            for filho in filhos:
                if (tuple(filho.estado)) not in listaNosExplorados:
                    if filho.custo <= self.limiteProfundidade:
                        fx = filho.custo + filho.heuristica
                        heapq.heappush(fronteira, (fx, filho))
                    else:
                        limiteAtingido = True
                        
        if limiteAtingido:
            print('Limite de profundidade atingido!')
            

    def expande(self, problema):
        self.nosExpandidos += 1
        estadoAtual = problema.estado
        indice = estadoAtual.index(0)
        tamanhoLista = len(estadoAtual)
        raiz = int(tamanhoLista ** 0.5)
        x = indice // raiz
        y = indice % raiz 

        filhos = []

        if x > 0:
            novoIndice = (x - 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristica(novoEstado, self.NodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, problema.custo + 1, "para cima", problema, heuristicaNo))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristica(novoEstado, self.NodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, problema.custo + 1, "para baixo", problema, heuristicaNo))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristica(novoEstado, self.NodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, problema.custo + 1, "para esquerda", problema, heuristicaNo))
        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristica(novoEstado, self.NodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, problema.custo + 1, "para direita", problema, heuristicaNo))

        return filhos


    def heuristica (self, estadoAtual, objetivo):
        custoRestante = 0
        for i in range(len(estadoAtual)):
            if estadoAtual[i] != 0 and estadoAtual[i] != objetivo[i]:
                custoRestante += 1
        
        return custoRestante