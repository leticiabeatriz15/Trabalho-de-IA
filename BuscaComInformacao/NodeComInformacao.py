class NodeI:
    def __init__(self, estado, custo, acao, pai, heuristica):
        self.estado = estado
        self.custo = custo
        self.acao = acao 
        self.pai = pai
        self.heuristica = heuristica
        
        
    def __lt__(self, outroEstado):
        return (self.custo + self.heuristica) < (outroEstado.custo + outroEstado.heuristica)