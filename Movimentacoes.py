def sequenciaAcoes (estadoAtual):
    listaAcoes = []
    
    while estadoAtual.pai is not None:
        listaAcoes.append(estadoAtual.acao)
        estadoAtual = estadoAtual.pai
        
    return listaAcoes[::-1] 


def caminhoPercorrido(estadoAtual):
    caminho = []
    while estadoAtual.pai is not None:
        caminho.append(estadoAtual.estado)
        estadoAtual = estadoAtual.pai

    return caminho[::-1] 