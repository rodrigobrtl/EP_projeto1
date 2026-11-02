def define_posicoes(linha, coluna, orientacao, tamanho):
    L = []
    k = 0
    if orientacao == 'vertical':
        while k < tamanho:
            L.append([linha + k, coluna])
            k += 1
    elif orientacao == 'horizontal':
        while k < tamanho:
            L.append([linha, coluna + k])
            k += 1
    return L

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio not in frota:
        frota[nome_navio] = []
    
    frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
       tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    grid = [[0] * 10 for i in range(10)]
    
    for lista in frota.values():
        for sublista in lista:
            for i, j in sublista:
                grid[i][j] = 1
    return grid
