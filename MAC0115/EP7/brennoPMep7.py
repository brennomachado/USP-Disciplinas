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
Exercício-Programa EP7
"""


def main():
    """ (NoneType) -> NoneType """
    #Impressão do descritivo do programa na tela
    print("############################################################################")
    print("### Este programa lê um arquivo de texto com uma sequência de nomes,     ###")
    print("### e cria outro arquivo com os nomes lidos em ordem alfabética          ###")
    print("############################################################################\n")

    listaEntrada = leArqEntrada()
    qntNomes = len(listaEntrada)

    saida = input("\nInsira um nome de arquivo txt para que a lista de nomes em ordem alfabética seja salva: ")
    arqSaida = open(saida, 'w', encoding='utf-8')

    #Impressão do descritivo do programa no arquivo de saída
    arqSaida.write("############################################################################\n")
    arqSaida.write("### Este programa lê um arquivo de texto com uma sequência de nomes,     ###\n")
    arqSaida.write("### e cria outro arquivo com os nomes lidos em ordem alfabética          ###\n")
    arqSaida.write("############################################################################\n")

    print("\n-- FORAM LIDOS %d NOMES" %(qntNomes))
    arqSaida.write("\n-- FORAM LIDOS %d NOMES\n" %(qntNomes))

    #Impressão da lista como foi lida
    print("\n\n-- A SEQUÊNCIA INICIAL DE NOMES É:")
    arqSaida.write("\n\n-- A SEQUÊNCIA INICIAL DE NOMES É:\n")
    for i in range(0, qntNomes, 1):
        print("%s" %(listaEntrada[i]), end="")  #impressão na tela
        arqSaida.write(listaEntrada[i])         #impressão no arquivo de saída

    ordenacaoAlfabetica(listaEntrada) #ordenação da lista

    #Impressão da lista em já em ordem alfabética
    print("\n\n-- A SEQUÊNCIA DE NOMES EM ORDEM ALFABÉTICA É:")
    arqSaida.write("\n\n-- A SEQUÊNCIA DE NOMES EM ORDEM ALFABÉTICA É:\n")
    for i in range(0, qntNomes, 1):
        print("%s" %(listaEntrada[i]), end="")  #impressão na tela
        arqSaida.write(listaEntrada[i])         #impressão no arquivo de saída

    arqSaida.close()
    print("")


def leArqEntrada():
    """ (NoneType) -> list
        Lê o nome de um arquivo texto contendo os nomes a serem ordenados
        e na forma como foi descrito anteriormente.
        A função abre esse arquivo, lê todos os nomes, ao mesmo tempo que cria
        uma lista com os nomes lidos; fecha o arquivo e retorna a lista criada.
    """

    nome_arquivo = input("Insira o nome do arquivo txt para leitura: ")
    arquivo = open(nome_arquivo, 'r', encoding = 'utf-8')
    lista = []
    linha = arquivo.readline()

    while linha:
        lista.append(linha)
        linha = arquivo.readline()
    arquivo.close()

    return lista


def maiuscula(carac):
    """ (str) -> str
        Recebe um caractere carac e se carac é uma letra minúscula, retorna
        a letra maiúscula correspondente; em caso contrário, retorna carac.
    """
    minusculas = "abcdefghijklmnopqrstuvwxyzáàãâéêíóôúç"
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZAAAAEEIOOUC"

    for i in range(0, len(minusculas), 1):
        if carac[0] == minusculas[i]:
            return maiusculas[i]
    return carac


def criaStringMaiuscula(s):
    """ (str) -> str
        Recebe um string s e cria um novo string, a partir de s, substituindo
        todas as letras minúsculas por letras maiúsculas correspondentes.
        Retorna o string criado.
        Observação: Esta função utiliza a função maiúscula.
    """
    frase = ""
    comp = len(s)
    for i in range(0, comp, 1):
        frase = frase + maiuscula(s[i])

    return frase


def comparaDoisNomes(nome1, nome2):
    """ (str, str) -> int
        Recebe dois strings, representando dois nomes completos, e retorna 0,
        se os dois nomes forem iguais; retorna -1, se nome1 deve vir antes do nome2
        (na ordem alfabética) e retorna 1, se nome2 deve vir antes do nome1.
        Observação: A partir de nome1 e nome2, a função cria dois novos strings
        com todas as letras maiúsculas, utilizando a função criaStringMaiuscula,
        e compara esses novos strings, sı́mbolo por sı́mbolo, para decidir se são
        iguais ou qual deles "é menor".
    """
    nome1_maiusculo = criaStringMaiuscula(nome1)
    nome2_maiusculo = criaStringMaiuscula(nome2)

    comp1 = len(nome1_maiusculo)
    comp2 = len(nome2_maiusculo)
    if comp1 < comp2:
        comp = comp1
    else:
        comp = comp2

    for i in range(0, comp, 1):
        if nome1_maiusculo[i] < nome2_maiusculo[i]:
            return -1
        elif nome1_maiusculo[i] > nome2_maiusculo[i]:
            return 1

    return 0


def ordenacaoAlfabetica(listaNomes):
    """ (list) -> NoneType
        Recebe uma lista de strings, onde cada string representa um nome completo.
        Rearranja os nomes de listaNomes de modo que fiquem em ordem alfabética.
        Observação: Esta função utiliza o algoritmo de ordenaçãao por seleção visto
        em aula e, para comparar dois nomes, utiliza a função comparaDoisNomes.
    """

    comp = len(listaNomes)

    for i in range(0, comp-1, 1):
        indice_menorNome = i
        for j in range(i+1, comp, 1):
            if comparaDoisNomes(listaNomes[indice_menorNome], listaNomes[j]) == 1:
                indice_menorNome = j
        if indice_menorNome != i:
            aux = listaNomes[i]
            listaNomes[i] = listaNomes[indice_menorNome]
            listaNomes[indice_menorNome] = aux


main()
