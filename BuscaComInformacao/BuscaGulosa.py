from BuscaComInformacao.NodeComInformacao import NodeI
from Movimentacoes import sequenciaAcoes, caminhoPercorrido
from ArvoreBusca import ArvoreBusca
import time 

class BuscaGulosa:
    def __init__(self, nodeEstadoInicial, nodeEstadoObjetivo):
        self.nodeEstadoInicial = nodeEstadoInicial
        self.nodeEstadoObjetivo = nodeEstadoObjetivo
        self.arvore = ArvoreBusca(nodeEstadoInicial, nodeEstadoObjetivo)

    def buscaGulosa(self):
        estadoAtual = self.nodeEstadoInicial
        listaNosExplorados = set()
        
        
        while True:
            if self.arvore.isNoObjetivo(estadoAtual):
                print('Estado objetivo encontrado!')
                print('Ações: ', sequenciaAcoes(estadoAtual))
                print('Caminho percorrido: ', caminhoPercorrido(estadoAtual))
                print('Total de passos: ',len(caminhoPercorrido(estadoAtual)))
                print('Nós expandidos: ', len(listaNosExplorados))
                # print('Estados expandidos: ', nosExpandidos)
                print('Profundidade da solução: ', len(caminhoPercorrido(estadoAtual)) - 1)
                return 
            
            listaNosExplorados.add(tuple(estadoAtual.estado))
            filhos = self.expande(estadoAtual)
        
            melhor = None
            melhorValor = float('inf')

            for filho in filhos:
                if (tuple(filho.estado) in listaNosExplorados):
                    continue
                valor = self.heuristicaPecas(filho.estado, self.nodeEstadoObjetivo.estado)
                if valor < melhorValor:
                    melhor = filho
                    melhorValor = valor
            
            
            if melhor is None:
                print('Sem caminhos disponíveis')
                return 
            
            estadoAtual = melhor

    def expande(self, problema):
        # nosExpandidos += 1
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
            heuristicaNo = self.heuristicaPecas(novoEstado, self.nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, 0, "para cima", problema, heuristicaNo))

        if x < raiz - 1:
            novoIndice = (x + 1) * raiz + y
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristicaPecas(novoEstado, self.nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, 0, "para baixo", problema, heuristicaNo))

        if y > 0:
            novoIndice = x * raiz + (y - 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristicaPecas(novoEstado, self.nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, 0, "para esquerda ", problema, heuristicaNo))
        
        if y < raiz - 1:
            novoIndice = x * raiz + (y + 1)
            novoEstado = estadoAtual[:]
            novoEstado[indice], novoEstado[novoIndice] = novoEstado[novoIndice], novoEstado[indice]
            heuristicaNo = self.heuristicaPecas(novoEstado, self.nodeEstadoObjetivo.estado)
            filhos.append(NodeI(novoEstado, 0, "para direita", problema, heuristicaNo))

        return filhos

    # nosExpandidos = 0
    def heuristicaPecas(self, estadoAtual, objetivo):
        pecasForaDoLugar = 0
        for i in range(len(estadoAtual)):
            if estadoAtual[i] != 0 and estadoAtual[i] != objetivo[i]:
                pecasForaDoLugar += 1
                
        return pecasForaDoLugar