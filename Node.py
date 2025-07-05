class Node:
    def __init__(self, estado, custo, acao, pai, heuristica):
        self.estado = estado
        self.custo = custo
        self.acao = acao 
        self.pai = pai
        self.heuristica = heuristica
        
    def __lt__(self, outro_estado):
        return (self.custo + self.heuristica) < (outro_estado.custo + outro_estado.heuristica)