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

def afundados(frota, tabuleiro):
    afundado = 0
    for lista_navios in frota.values():
        for navio in lista_navios:
            navio_afundado =  True
            for i, j in navio:
                if tabuleiro[i][j] != 'X':
                    navio_afundado =  False
                    break
            if navio_afundado == True:
                afundado += 1
    return afundado

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    for lista_navios in frota.values():
        for navio in lista_navios:
            for i, j in define_posicoes(linha, coluna, orientacao, tamanho):
                if i < 0 or i >= 10 or j < 0 or j >= 10:
                    return False
                elif [i, j] in navio:
                    return False
    if orientacao == 'horizontal' and (coluna + tamanho) > 10:
        return False
    elif orientacao == 'vertical' and (linha + tamanho) > 10:
        return False            
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

   