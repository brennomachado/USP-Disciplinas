# -*- coding: utf-8 -*-
"""eg15_experimento'''     MAC0122 - Princípios de Desenvolvimento de Algoritmos      Tópico: análise dos algoritmos      - fibonacci iterativo     - fibonacci recursivo     - fibonacci recursivo com memoização          Data da última atualização: 16/10/20.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/197Rm6Ywp5iJ4o9rC0hZthXrh_GOSI_i3
"""

'''
    MAC0122 - Princípios de Desenvolvimento de Algoritmos

    Tópico: análise dos algoritmos

    - fibonacci iterativo
    - fibonacci recursivo
    - fibonacci recursivo com memoização    

    Data da última atualização: 16/10/2021
'''
################################################################
# carrega as coisas do Python

# sys para controlar o tamanho da pilha de recursão
import sys
# timer para medir tempos de execução
from timeit import default_timer as Timer
# 
# para ver gráficos vamos usar pyplot
# Para saber mais sobre pyplot: 
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#logarithmic-and-other-nonlinear-axes
import numpy as np
import matplotlib.pyplot as plt

################################################################
# carrega todas suas funções, iterativas e recursivas
from eg_fibonacci import *

################################################################
# configuração da pilha e constantes do experimento.
# Essas constantes podem ser alteradas para adaptá-las a sua máquina

MAX_PILHA_RECURSAO = 100000
sys.setrecursionlimit(MAX_PILHA_RECURSAO)  

VALOR_N_INICIAL = 4
NUMERO_DE_ITERACOES = 5  # cada iteração dobra o valor de N

################################################################
################################################################
'''
main()
    essa função roda o experimento que compara os
    tempos de execução das versões iterativa e
    recursiva de cada função.
'''
def main():

    ## lista com os pares de funções a serem comparadas
    funcoes = [[fibonacciI, fibonacciR2]]  

    for par in funcoes:
        graf1 = np.zeros((2,NUMERO_DE_ITERACOES))
        graf2 = np.zeros((2,NUMERO_DE_ITERACOES))

        nome1 = str(par[0]).split()[1]
        nome2 = str(par[1]).split()[1]
        print('\n<<<   ===========   >>>\n')
        print(f"Experimento: alg_1 = {nome1} x alg_2 = {nome2}\n")
        print(f'n\t | {nome1}: (res) x tempo \t | {nome2}: (res) x tempo \t | razão dos tempos alg_2 / alg_1 | ')

        n = VALOR_N_INICIAL
        for i in range( NUMERO_DE_ITERACOES ):
            graf2[0,i] = graf1[0,i] = n

            resultados = experimento(par, n)
            s = f'{n}\t | '
            for res in resultados:
                s += f"({res[0]:10d}) x {res[1]:.6f}s\t | "
            razao = resultados[1][1]/resultados[0][1]
            graf1[1,i] = resultados[0][1]
            graf2[1,i] = resultados[1][1]
            print(f"{s} {razao:10.2f}")
            n = 2 * n

        print("Feche a janela do gráfico para continuar ...")
        plt.yscale('log')
        plt.grid(True)
        plt.title(f'{nome1} x {nome2}')
        plt.plot( graf1[0], graf1[1], 'b+') # blue +
        plt.plot( graf2[0], graf2[1], 'ro') # red o 
        plt.show()


# ................................................

def experimento(funcoes, dados):
    ''' (list, obj) -> list
    Recebe um objeto dados que é usado como entrada para as
    funções na lista funcoes. 
    Retorna uma lista com os valores e tempos de cada função.
    '''
    tempos = []
    for f in funcoes:
        t_ini = Timer()
        val = f( dados )
        t_fim = Timer()
        t_dif = t_fim - t_ini
        tempos.append( (val, t_dif) )

    return tempos

# ................................................
if __name__ == '__main__':
    main()