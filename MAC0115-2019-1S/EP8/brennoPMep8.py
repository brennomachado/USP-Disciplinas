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
Exercício-Programa EP8
"""


def main():
    """Função Principal."""
    # Impressão do descritivo do programa na tela
    print("###############################################################")
    print("###   Este programa lê um arquivo de texto com uma matriz   ###")
    print("###   e faz operações definidas pelo usuário com a matriz   ###")
    print("###   lida, até que esse decida o fim das operações.        ###")
    print("###############################################################\n")

    matriz = []
    matriz_op = []
    opcao = ""
    listar_operacoes()

    while opcao != "fi" :
        print("________________________________________________________________________________\n")
        opcao = input("Digite o código de uma operação: ")

        if opcao == "li":
            listar_operacoes()
        elif opcao == "fi":
            print()
        else:
            matriz = le_cria_matriz_arq()
            linhas = len(matriz)
            colunas = len(matriz[0])
            print("Matriz com %d linhas e %d colunas: \n" %(linhas, colunas))
            imprime_matriz(matriz)
            if opcao == "rh" :
                matriz_op = rebater_horizontal(matriz)
                print("Transformação realizada: rebater na horizontal\n")
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

            elif opcao == "rv" :
                matriz_op = rebater_vertical(matriz)
                print("Transformação realizada: rebater na vertical\n")
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

            elif opcao == "ro" :
                matriz_op = rotacionar(matriz)
                print("Transformação realizada: rotacionar 90 graus no sentido horário\n")
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

            elif opcao == "tr" :
                matriz_op = transposta(matriz)
                print("Transformação realizada: transposta\n")
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

            elif opcao == "sm" :
                indices = True
                while indices :
                    linSup = int(input("\nDigite o ı́ndice de linha do canto superior esquerdo: "))
                    colSup = int(input("\nDigite o ı́ndice de coluna do canto superior esquerdo: "))
                    linInf = int(input("\nDigite o ı́ndice de linha do canto inferior direito: "))
                    colInf = int(input("\nDigite o ı́ndice de coluna do canto inferior direito: "))
                    if (linSup >= 0 and linSup < linhas) and (linInf >= 0 and linInf < linhas) and (colSup >= 0 and colSup < colunas) and (colInf >= 0 and colInf < colunas) :
                        indices = False
                    else:
                        print("\n\nÍndices digitados inválidos.")
                        print("Os índices para linhas devem ser >= 0 e < %d" %(linhas))
                        print("Os índices para colunas devem ser >= 0 e < %d\n" %(colunas))

                matriz_op = submatriz(matriz, linSup, colSup, linInf, colInf)
                print("\n\nTransformação realizada: extrair uma submatriz de (%d,%d) a (%d,%d)\n" %(linSup, colSup, linInf, colInf))
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

            elif opcao == "re" :
                matriz_op = reduzir(matriz)
                print("Transformação realizada: reduzir pela metade o tamanho\n")
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

            elif opcao == "do" :
                matriz_op = dobrar(matriz)
                print("Transformação realizada: dobrar o tamanho\n")
                print("Matriz resultante com %d linhas e %d colunas: \n" %(len(matriz_op), len(matriz_op[0])))
                imprime_matriz(matriz_op)

    print("________________________________________________________________________________\n")


def cria_matriz(nlinhas, ncolunas, valor):
    """ (int, int, tipo do valor) -> matriz (ou seja, tipo list).
    Cria uma matriz com nlinhas linhas e ncolunas colunas com todos os
    elementos iguais a valor.
    Retorna a matriz criada.
    """
    matriz = []

    for i in range(0, nlinhas, 1):
        linha = []
        for j in range(0, ncolunas, 1):
            linha.append(valor)
        matriz.append(linha)

    return matriz


def le_cria_matriz_arq():
    """ (NoneType) -> matriz
    Lê o nome de um arquivo texto contendo uma matriz; ou seja, cada linha do
    arquivo contém os elementos da linha correspondente da matriz. A função
    abre esse arquivo, lê os elementos da matriz, ao mesmo tempo que cria uma
    estrutura para a matriz com os números lidos; fecha o arquivo e retorna a
    matriz criada.
    Obs.: Os elementos da matriz são números inteiros não negativos.
    """
    matriz = []
    nome_arquivo = input("\nInsira o nome do arquivo txt para leitura da matriz: ")
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')

    for linha in arquivo:
        lista = linha.split()
        matriz_linha = []
        for elemento in lista:
            matriz_linha.append(int(elemento))
        matriz.append(matriz_linha)

    arquivo.close()
    print()

    return matriz


def imprime_matriz(matriz):
    """ (matriz) -> NoneType
    Recebe e imprime uma matriz de inteiros no formato bidimensional de matriz.
    """
    for linha in matriz:
        for elemento in linha:
            print("%8d" %(elemento), end='')
        print()
    print("\n")


def rebater_horizontal(aMat):
    """ (matriz) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e cria a matriz resultante
    da aplicação da transformação correspondente em aMat.
    Retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    nlinhas = len(aMat)
    ncolunas = len(aMat[0])

    matriz_rh = cria_matriz(nlinhas, ncolunas, 0)

    for i in range (0, nlinhas, 1):
        for j in range(0, ncolunas, 1):
            matriz_rh[i][j] = aMat[nlinhas-i-1][j]

    return matriz_rh


def rebater_vertical(aMat):
    """ (matriz) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e cria a matriz resultante
    da aplicação da transformação correspondente em aMat.
    Retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    nlinhas = len(aMat)
    ncolunas = len(aMat[0])

    matriz_rv = cria_matriz(nlinhas, ncolunas, 0)

    for i in range(0, nlinhas, 1):
        for j in range(0, ncolunas, 1):
            matriz_rv[i][j] = aMat[i][ncolunas-j-1]

    return matriz_rv


def rotacionar(aMat):
    """ (matriz) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e cria a matriz resultante
    da aplicação da transformação correspondente em aMat.
    Retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    nlinhas = len(aMat)
    ncolunas = len(aMat[0])

    matriz_ro = cria_matriz(ncolunas, nlinhas, 0)

    for i in range(0, ncolunas, 1):
        for j in range(0, nlinhas, 1):
            matriz_ro[i][j] = aMat[nlinhas-1-j][i]

    return matriz_ro


def transposta(aMat):
    """ (matriz) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e cria a matriz resultante
    da aplicação da transformação correspondente em aMat.
    Retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    nlinhas = len(aMat)
    ncolunas = len(aMat[0])

    matriz_tr = cria_matriz(ncolunas, nlinhas, 0)

    for i in range(0, ncolunas, 1):
        for j in range(0, nlinhas, 1):
            matriz_tr[i][j] = aMat[j][i]

    return matriz_tr


def submatriz(aMat, linSup, colSup, linInf, colInf):
    """(matriz, int, int, int, int) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e quatro inteiros: linSup
    e colSup que são os ı́ndices de linha e de coluna da posição no canto
    superior esquerdo da submatriz desejada; linInf e colInf que são os
    ı́ndices de linha e de coluna da posição no canto inferior direito da
    submatriz desejada. A função cria a matriz resultante da aplicação da
    transformação correspondente em aMat e retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    lin_sm = linInf - linSup + 1
    col_sm = colInf - colSup + 1

    matriz_sm = cria_matriz(lin_sm, col_sm, 0)

    for i in range(0, lin_sm, 1):
        for j in range(0, col_sm, 1):
            matriz_sm[i][j] = aMat[linSup+i][colSup+j]

    return matriz_sm


def reduzir(aMat):
    """(matriz) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e cria a matriz resultante
    da aplicação da transformação correspondente em aMat.
    Retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    nlinhas = len(aMat)
    ncolunas = len(aMat[0])
    lin_re = nlinhas//2
    col_re = ncolunas//2
    matriz_re = cria_matriz(lin_re, col_re, 0)

    for i in range(0, lin_re, 1):
        for j in range(0, col_re, 1):
            matriz_re[i][j] = (aMat[i*2][j*2] + aMat[i*2][j*2+1] + aMat[i*2+1][j*2] + aMat[i*2+1][j*2+1])//4

    return matriz_re


def dobrar(aMat):
    """ (matriz) -> matriz
    Recebe uma matriz de inteiros não negativos aMat e cria a matriz resultante
    da aplicação da transformação correspondente em aMat.
    Retorna a matriz criada.
    Obs.: Utiliza a função cria_matriz.
    """
    nlinhas = len(aMat)
    ncolunas = len(aMat[0])
    matriz_do = cria_matriz(nlinhas*2, ncolunas*2, 0)

    for i in range(0, nlinhas, 1):
        for j in range(0, ncolunas, 1):
            matriz_do[i*2][j*2] = aMat[i][j]
            matriz_do[i*2][j*2+1] = aMat[i][j]
            matriz_do[i*2+1][j*2] = aMat[i][j]
            matriz_do[i*2+1][j*2+1] = aMat[i][j]

    return matriz_do


def listar_operacoes():
    """ (NoneType) -> NoneType
    Escreve na tela os códigos e os significados das operaçẽes que um usuário
    pode escolher.
    """
    print("\nLista dos códigos e das respectivas operações:")
    print("   rh - rebater uma matriz na horizontal")
    print("   rv - rebater uma matriz na vertical")
    print("   ro - rotacionar uma matriz 90 graus no sentido horário")
    print("   tr - obter a transposta de uma matriz")
    print("   sm - extrair uma submatriz de uma matriz")
    print("   re - reduzir pela metade o tamanho de uma matriz")
    print("   do - dobrar o tamanho de uma matriz")
    print("   li - listar todas as possíveis operações com os seus códigos")
    print("   fi - finalizar a interação com o usuário")


main()
