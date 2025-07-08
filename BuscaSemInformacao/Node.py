class Node:
    def __init__(self, estado, custo, acao, pai, profundidade):
        self.estado = estado
        self.custo = custo
        self.acao = acao 
        self.pai = pai
        self.profundidade = profundidade