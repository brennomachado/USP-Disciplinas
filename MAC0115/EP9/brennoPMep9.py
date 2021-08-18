# -*- coding: utf-8 -*-
"""
DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
TODAS AS PARTES ORIGINAIS DESSE EP FORAM DESENVOLVIDAS E
IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES DESSE EP.
DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
SERÃO SEVERAMENTE PUNIDOS.
Nome do aluno: Brenno Pereira Machado
Número USP: 6434401
Curso: Licenciatura em Física
Disciplina: MAC0115 Introdução à Computação
Exercício-Programa EP9
"""

#-----------------------------------------------------------------------
# DEFINIÇÃO DAS CONSTANTES
#-----------------------------------------------------------------------

TAMANHO =  8  # Há exemplos com tabuleiros 4x4 e 6x6, não ficou especificado no
              # PDF, mas acho que para esses exemplos será mudado essa constante.
              # Ficou muito vaga a instrução do EP e contraditória com a parte que
              # diz que a saída deve ser "idêntica" a desses exemplos.
BOLA    = 'O'
XIS     = 'X'
VAZIA   = '.'
MOLDURA = '*'

#-----------------------------------------------------------------------

def main():
    '''  Função principal do programa que joga Reversi com o usuário
    '''

    print()
    print("###############################################################")
    print("###                     REVERSI / OTELO                     ###")
    print("###   Esse programa joga Reversi/Otelo com você.            ###")
    print("###   Você é o jogador 'X' e computador é o jogador 'O'     ###")
    print("###############################################################\n")

    print("A configuração inicial do tabuleiro é:")

    tabuleiro = inicializa_tabuleiro()
    jogador = XIS
    existeMovXis = True
    existeMovBola = True
    numXis = 2
    numBola = 2

    exibe_tabuleiro(tabuleiro)
    print("\n'X' tem 2 marca(s) no tabuleiro")
    print("'O' tem 2 marca(s) no tabuleiro")


    while existeMovXis or existeMovBola:

        print("\n--->  Jogador da vez é '%c'.\n" %(jogador))

        if existe_movimento(tabuleiro, jogador):
            if jogador == XIS:
                linha = int(input("\nDigite a linha da posição em que pretende jogar: "))
                coluna = int(input("\nDigite a coluna da posição em que pretende jogar: "))
                reversoes = numero_reversoes(tabuleiro, jogador, linha, coluna)
            else:
                reversoes, linha, coluna = estrategia_jogo(tabuleiro, jogador)

            if reversoes > 0:
                coloca_reverte_marca(tabuleiro, jogador, linha, coluna)
                print("\nJogador '%c' colocou sua marca na posição (%d, %d)." %(jogador, linha, coluna))
                if jogador == XIS:
                    print("%d '0'(s) revertido(s) para 'X'(s)." %(reversoes))
                    numXis = numXis + reversoes + 1
                    numBola = numBola - reversoes
                else:
                    print("%d 'X'(s) revertido(s) para '0'(s)." %(reversoes))
                    numXis = numXis - reversoes
                    numBola = numBola + reversoes + 1
            else:
                print("\nJogador '%c' nao pode jogar na posição (%d, %d)." %(jogador, linha, coluna))
        else:
            print("Não há movimento válido para o jogador '%c'." %(jogador))

        print()
        exibe_tabuleiro(tabuleiro)
        print("\n'X' tem %d marca(s) no tabuleiro" %(numXis))
        print("'O' tem %d marca(s) no tabuleiro" %(numBola))

        existeMovXis = existe_movimento(tabuleiro, XIS)
        existeMovBola = existe_movimento(tabuleiro, BOLA)

        jogador = troca_jogador(jogador) #Alternando o jogador da vez


    #Terminando o jogo
    print("\n\n  PARTIDA TERMINADA.\n")
    if numXis > numBola:
        print("Jogador 'X' venceu!!!\n")
    elif numBola > numXis:
        print("Jogador 'O' venceu!!!\n")
    else:
        print("Jogadores 'X' e 'O' empataram.\n")


#-----------------------------------------------------------------------
#............ Definição das outras funções do programa .................
#-----------------------------------------------------------------------

def cria_matriz(nlinhas, ncolunas, valor):
    ''' (int, int, tipo do valor) -> matriz

    Cria uma matriz com nlinhas linhas e ncolunas colunas,
    sendo que cada elemento é igual a valor.
    Retorna a matriz criada.
    '''

    matriz = []

    for i in range(0, nlinhas, 1):
        linha = []
        for j in range(0, ncolunas, 1):
            linha.append(valor)
        matriz.append(linha)

    return matriz


#-----------------------------------------------------------------------

def inicializa_tabuleiro():
    ''' (NoneType) -> matriz

    Cria e retorna uma matriz (com uma moldura) com a configuração
    inicial de um tabuleiro para o jogo Otelo.
    '''

    matriz = cria_matriz(TAMANHO+2, TAMANHO+2, MOLDURA)

    for i in range(1, TAMANHO+1, 1):
        for j in range(1, TAMANHO+1, 1):
            matriz[i][j] = VAZIA

    matriz[TAMANHO//2][TAMANHO//2] = BOLA
    matriz[TAMANHO//2 + 1][TAMANHO//2 + 1] = BOLA
    matriz[TAMANHO//2][TAMANHO//2 + 1] = XIS
    matriz[TAMANHO//2 + 1][TAMANHO//2] = XIS

    return matriz


#-----------------------------------------------------------------------

def exibe_tabuleiro(tabuleiro):
    ''' (matriz) -> NoneType

    Recebe uma matriz representando um tabuleiro do jogo Otelo
    e imprime esse tabuleiro com as linhas e colunas numeradas
    e tracejadas para facilitar a visualização do usuário.
    '''

    print()
    print('      ', end='')
    for i in range(1, TAMANHO+1, 1):
        print('   %d  ' %i, end='')
    print()

    print('      ', end='')
    for i in range(1, TAMANHO+1, 1):
        print('+-----', end='')
    print('+')

    for i in range(1, TAMANHO+1, 1):
        print('%5d ' %i, end='')
        for j in range(1, TAMANHO+1, 1):
            print("|  %s  " %(tabuleiro[i][j]), end='')
        print('|')

        print('      ', end='')
        for j in range(1, TAMANHO+1, 1):
            print('+-----', end='')
        print('+')
    print()

#----------------------------------------------------------------------

def numero_reversoes(tabuleiro, jogador, indlin, indcol):
    ''' (matriz, str, int, int) -> int

    Recebe uma matriz tabuleiro, uma marca jogador e uma posição
    (indlin, indcol).
    A função retorna 0 (zero), se (indlin, indcol) é uma posição
    fora do tabuleiro ou se esta posição já tiver alguma marca
    ou se o jogador não puder colocar a sua marca nessa posição.
    Em caso contrário, a função retorna o número total de
    reversões que serão realizadas se o jogador puder colocar
    a sua marca na posição (indlin, indcol).
    '''

    if tabuleiro[indlin][indcol] == XIS or tabuleiro[indlin][indcol] == BOLA:
        return 0
    if (indlin < 1 or indlin > TAMANHO) or (indcol < 1 or indcol > TAMANHO):
        return 0

    if jogador == XIS:
        adversario = BOLA
    else:
        adversario = XIS

    qntRev = 0
    auxRev = 0

    #Movimento para direita
    i = 1
    prox = tabuleiro[indlin][indcol+i]
    while prox == adversario:
        auxRev += 1
        i += 1
        prox = tabuleiro[indlin][indcol+i]
    if prox == jogador:
        qntRev += auxRev

    #Movimento para esquerda
    i = -1
    auxRev = 0
    prox = tabuleiro[indlin][indcol+i]
    while prox == adversario:
        auxRev += 1
        i -= 1
        prox = tabuleiro[indlin][indcol+i]
    if prox == jogador:
        qntRev += auxRev

    #Movimento para baixo
    i = 1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol]
    while prox == adversario:
        auxRev += 1
        i += 1
        prox = tabuleiro[indlin+i][indcol]
    if prox == jogador:
        qntRev += auxRev

    #Movimento para cima
    i = -1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol]
    while prox == adversario:
        auxRev += 1
        i -= 1
        prox = tabuleiro[indlin+i][indcol]
    if prox == jogador:
        qntRev += auxRev

    #Movimento Diagonal Sup Direita
    i = -1
    j = 1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i -= 1
        j += 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        qntRev += auxRev

    #Movimento Diagonal Sup Esquerda
    i = -1
    j = -1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i -= 1
        j -= 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        qntRev += auxRev

    #Movimento Diagonal Inf Direita
    i = 1
    j = 1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i += 1
        j += 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        qntRev += auxRev

    #Movimento Diagonal Inf Esquerda
    i = 1
    j = -1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i += 1
        j -= 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        qntRev += auxRev

    return qntRev


#----------------------------------------------------------------------

def existe_movimento(tabuleiro, jogador):
    ''' (matriz, str) -> bool

    Recebe uma matriz tabuleiro e uma marca jogador.
    A função retorna True, se existir algum movimento válido para o
    jogador; em caso contrário, retorna False.
    '''

    movimento = False

    for i in range(1, TAMANHO+1, 1):
        for j in range(1, TAMANHO+1, 1):
            if numero_reversoes(tabuleiro, jogador, i, j) > 0:
                movimento = True
                i = TAMANHO
                j = TAMANHO

    return movimento

#----------------------------------------------------------------------

def estrategia_jogo(tabuleiro, jogador):
    ''' (matriz, str) -> int, int, int

    Recebe uma matriz tabuleiro e uma marca jogador.
    Nesta função, supõe-se que jogador é o programa.
    A função determina uma posição (indlin, indcol) para o jogador colocar
    a sua marca, de modo que o número de reversões resultante seja o
    maior possível, e retorna o número de reversões, indlin e indcol.
    Obs.: A função pode supor que, quando ela é chamada, existe algum
    movimento válido para jogador.
    '''
    revMax = 0

    for i in range(1, TAMANHO+1, 1):
        for j in range(1, TAMANHO+1, 1):
            aux = numero_reversoes(tabuleiro, jogador, i, j)
            if aux > revMax:
                revMax = aux
                imax = i
                jmax = j

    return revMax, imax, jmax

#----------------------------------------------------------------------

def coloca_reverte_marca(tabuleiro, jogador, indlin, indcol):
    ''' (matriz, str, int, int) -> Nonetype

    Recebe uma matriz tabuleiro, uma marca jogador e uma posição
    (indlin, indcol) em que o jogador pode colocar a sua marca.
    A função coloca a marca do jogador na posição (indlin, indcol)
    do tabuleiro e faz todas as reversões necessárias.
    '''

    if jogador == XIS:
        adversario = BOLA
    else:
        adversario = XIS

    #Trocar peças à direita
    i = 1
    auxRev = 0
    prox = tabuleiro[indlin][indcol+i]
    while prox == adversario:
        auxRev += 1
        i += 1
        prox = tabuleiro[indlin][indcol+i]
    if prox == jogador:
        for j in range(indcol+1, auxRev+indcol+1, 1):
            tabuleiro[indlin][j] = jogador

    #Trocar peças à esquerda
    i = -1
    auxRev = 0
    prox = tabuleiro[indlin][indcol+i]
    while prox == adversario:
        auxRev += 1
        i -= 1
        prox = tabuleiro[indlin][indcol+i]
    if prox == jogador:
        for j in range(indcol-1, indcol-auxRev-1, -1):
            tabuleiro[indlin][j] = jogador

    #Trocar peças à baixo
    i = 1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol]
    while prox == adversario:
        auxRev += 1
        i += 1
        prox = tabuleiro[indlin+i][indcol]
    if prox == jogador:
        for j in range(indlin+1, indlin+auxRev+1, 1):
            tabuleiro[j][indcol] = jogador

    #Trocar peças à cima
    i = -1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol]
    while prox == adversario:
        auxRev += 1
        i -= 1
        prox = tabuleiro[indlin+i][indcol]
    if prox == jogador:
        for j in range(indlin-1, indlin-auxRev-1, -1):
            tabuleiro[j][indcol] = jogador

    #Trocar peças na Diagonal Sup Direita
    i = -1
    j = 1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i -= 1
        j += 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        k = indlin-1
        l = indcol+1
        while tabuleiro[k][l]==adversario:
            tabuleiro[k][l] = jogador
            k -= 1
            l += 1

    #Trocar peças na Diagonal Sup Esquerda
    i = -1
    j = -1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i -= 1
        j -= 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        k = indlin-1
        l = indcol-1
        while tabuleiro[k][l]==adversario:
            tabuleiro[k][l] = jogador
            k -= 1
            l -= 1

    #Trocar peças na Diagonal Inf Direita
    i = 1
    j = 1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i += 1
        j += 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        k = indlin+1
        l = indcol+1
        while tabuleiro[k][l]==adversario:
            tabuleiro[k][l] = jogador
            k += 1
            l += 1

    #Trocar peças na Diagonal Inf Esquerda
    i = 1
    j = -1
    auxRev = 0
    prox = tabuleiro[indlin+i][indcol+j]
    while prox == adversario:
        auxRev += 1
        i += 1
        j -= 1
        prox = tabuleiro[indlin+i][indcol+j]
    if prox == jogador:
        k = indlin+1
        l = indcol-1
        while tabuleiro[k][l]==adversario:
            tabuleiro[k][l] = jogador
            k += 1
            l -= 1

    tabuleiro[indlin][indcol] = jogador

#----------------------------------------------------------------------

def troca_jogador(jogador):
    ''' (str) -> str
    Recebe uma marca jogador e retorna a marca de seu adversário.
    '''

    if jogador == XIS:
        return BOLA
    elif jogador == BOLA:
        return XIS

#----------------------------------------------------------------------
main()
