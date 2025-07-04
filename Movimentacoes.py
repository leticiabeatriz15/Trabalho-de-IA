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
        
        # for elemento in caminho:
        #     textoOrganizado = ""
        #     for i in elemento:
        #         if i == 0:
        #             textoOrganizado += "\033[32m"+ str(i) + "\033[0m"
        #         else:
        #             textoOrganizado += str(i)
            
        # print(textoOrganizado)
        
    return caminho[::-1] 