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
Exercício-Programa EP4
"""

def main():
    print("_________________________________________________________")
    n = int(input("\n Digite o número de pares de inteiros a serem testados:"))
    i=0
    while (i < n):
        pertence = False
        a = int(input("\n Digite um inteiro positivo para a:"))
        b = int(input("\n Digite um inteiro positivo para b:"))
        cp_a = a
        cp_b = b
        j=1
        while (b > 0) and (a > 0):

            if (b%10 == a%10) :
                b = b//10
                a = a//10
            else:
                a = cp_a
                b = cp_b//(10**j)
                j=j+1

        if (a == 0):
            pertence = True
        else:
            pertence = False
        i = i + 1

        if (pertence):
            print("\n %d é um segmento de %d." %(cp_a, cp_b))
        else:
            print("\n %d não é um segmento de %d." %(cp_a, cp_b))
        print("_________________________________________________________")
main()
