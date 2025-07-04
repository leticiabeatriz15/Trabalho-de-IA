class Node:
    def __init__(self, estado, custo, acao, pai, heuristica):
        self.estado = estado
        self.custo = custo
        self.acao = acao 
        self.pai = pai
        self.heuristica = heuristica
        