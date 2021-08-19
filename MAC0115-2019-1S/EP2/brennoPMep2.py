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
Exercício-Programa EP2
"""
def main():
    print("Este programa determina o IMC - Índice de Massa Corporal.")
    print()
    nome = str(input("Digite o nome de uma pessoa: "))
    print()
    idade = int(input("Digite a idade (em anos): "))
    print()
    peso = float(input("Digite o peso (em quilogramas): "))
    print()
    altura = float(input("Digite a altura (em metros): "))

    imc = peso/(altura*altura)
    print()
    print(nome,"tem",idade,"anos e seu IMC é",imc)
    print()
    print(nome,"está abaixo do peso normal? (",imc < 18.5,")")
    print(nome,"está acima do peso normal? (",imc > 25,")")
    print(nome,"está com o peso normal? (",(imc >= 18.5) and (imc < 25),")")

main()
