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
Exercício-Programa EP6
"""


def main():
    """(NoneType) -> NoneType
    """
    print("\nEste programa utiliza o algoritmo Crivo de Eratóstenes para determinar \n todos os números primos até um dado número inteiro positivo.")
    print("_____________________________________________________________________________\n")
    n = int(input("Digite um número inteiro positivo para n: "))
    lista = []
    lista = criaListaCrivoEratostenes(n)

    primos = criaListaPrimos(lista)
    print("\nOs %d números primos menores ou iguais a %d são:\n" %(len(primos), n))
    j=1
    for i in range(0, len(primos), 1):
        print("%4d" %(primos[i]), end=" ")
        if j == 10:
            print("")
            j = 0
        j += 1

    print("\n")
    print("_____________________________________________________________________________\n")


def riscarMultiplos(k, crivo):
    """(int, list) -> NoneType
    Recebe um inteiro positivo k e uma lista crivo.
    Altera a lista crivo atribuindo False a toda posição dessa lista
    cujo índice é um múltiplo de k, maior do que k.
    Obs.: No exemplo, corresponde a riscar todos os múltiplos de k,
    maiores do que k.
    """
    for i in range(k-1, len(crivo), 1):
        if crivo[i] == True:        #para reduzir o nº de operações de cálculo de resto de divisão quando o elemento já tiver sido excluído da lista crivo
            if ((i + 2) % k) == 0:
                crivo[i] = False


def criaListaCrivoEratostenes(n):
    """(int) -> list
    Recebe um inteiro positivo n e cria uma lista crivo tal que
    para cada i, 0 <= i <= n, crivo[i] armazena True ou False,
    dependendo se i é primo ou não, respectivamente.
    A lista crivo é criada implementando o algoritmo do Crivo
    de Eratóstenes e utiliza a função riscarMultiplos.
    Esta função retorna a lista crivo.
    """
    crivo = []
    for i in range(0, n-1, 1):
        crivo.append(True)

    for i in range(0, len(crivo), 1):
        if crivo[i] == True:
            riscarMultiplos(i+2, crivo)

    return crivo


def criaListaPrimos(crivo):
    """(list) -> list
    Recebe uma lista crivo que é resultante de uma chamada da função
    criaListaCrivoEratostenes.
    Esta função cria e retorna uma lista primos com todos os
    números primos
    """
    primos = []
    for i in range(0, len(crivo), 1):
        if crivo[i] == True:
            primos.append(i+2)

    return primos

main()
