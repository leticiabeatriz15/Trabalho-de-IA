class ArvoreBusca:
    def __init__ (self, noInicial, noObjetivo):
        self.noInicial = noInicial
        self.noObjetivo = noObjetivo
        
    def getNoInicial(self):
        return self.noInicial
    
    def isNoObjetivo(self, estadoAtual):
        return self.noObjetivo.estado == estadoAtual.estado
    
    
    