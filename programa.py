import funcoes as fn

grid = [[0] * 10 for i in range(10)]

frota = {
   'porta-aviões': [],
   'navio-tanque': [],
   'contratorpedeiro': [],
   'submarino': [], 
}

tamanho = [4,3,2,1]
quantidade = [1,2,3,4]
i = 0

for nome_navio in frota:
    j = 0
    tamanho_navio =  tamanho[i]
    while j < quantidade[i]:
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho_navio}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if tamanho_navio > 1:
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
        valida = fn.posicao_valida(frota, linha, coluna, orientacao, tamanho_navio)
        while valida ==  False:
            print("Esta posição não está válida!")
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho_navio}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if tamanho_navio > 1:
                orientacao = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao == 1:
                    orientacao = "vertical"
                elif orientacao == 2:
                    orientacao = "horizontal"
            valida = fn.posicao_valida(frota, linha, coluna, orientacao, tamanho_navio)
        fn.define_posicoes(linha, coluna, orientacao, tamanho_navio)
        fn.preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho_navio)
        j += 1
    i+=1

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],

    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],

    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],

    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = fn.posiciona_frota(frota)
tabuleiro_oponente = fn.posiciona_frota(frota_oponente)
lista_jogadas = []
jogando = True

# Mostra os tabuleiros antes da primeira jogada.
print(fn.monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
while jogando:
    linha = int(input("Jogador, qual linha deseja atacar? "))
    while linha < 0 or linha > 9:
        print("Linha inválida!")
        linha = int(input("Jogador, qual linha deseja atacar? "))
    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while coluna < 0 or coluna > 9:
        print("Coluna inválida!")
        coluna = int(input("Jogador, qual coluna deseja atacar? "))

    # Uma posição repetida não pode executar faz_jogada.
    if [linha, coluna] in lista_jogadas:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue
    lista_jogadas.append([linha, coluna])
    tabuleiro_oponente = fn.faz_jogada(tabuleiro_oponente, linha, coluna)
    quantidade_afundados = fn.afundados(frota_oponente, tabuleiro_oponente)

    if quantidade_afundados == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

    else:
        print(fn.monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))