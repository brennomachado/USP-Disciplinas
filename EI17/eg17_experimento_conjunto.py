# -*- coding: utf-8 -*-
"""eg17_experimento_conjunto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13jBIFvqnr0NGKBv6GlSUS8Vn1-bA7neg
"""

'''
    MAC0122 - Princípios de Desenvolvimento de Algoritmos

    Experimento
    Análise de algoritmos recursivos para segmentação de blobs
    usando sets, listas e arrays.
    
    Tópico: análise dos algoritmos

    - segmente_blob      -> usa conjunto (set)
    - segmente_blob_list -> usa lista
    - segmente_blob_array -> usa numpy array

    Data da última atualização: 25/10/2021

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
from eg_blobs import *

################################################################
################################################################
# configuração da pilha e constantes do experimento.
# Essas constantes podem ser alteradas para adaptá-las a sua máquina

MAX_PILHA_RECURSAO = 1000000
sys.setrecursionlimit(MAX_PILHA_RECURSAO)  

VALOR_N_INICIAL = 2
NUMERO_DE_ITERACOES = 7  # cada iteração dobra o valor de N

## Avaliação em pares
## insira/remova/edite os pares de funções na lista para serem avaliadas
PARES_DE_FUNCOES = [[segmente_blob, segmente_blob_array]]

################################################################
#
# não deve ser necessário alterar mais nada daqui para baixo...
#
################################################################
'''
main()
    essa função roda o experimento que compara os
    tempos de execução de pares de funções.
'''
def main():

    ## lista com os pares de funções a serem comparadas

    for par in PARES_DE_FUNCOES:
        graf1 = np.zeros((2,NUMERO_DE_ITERACOES))
        graf2 = np.zeros((2,NUMERO_DE_ITERACOES))

        nome1 = str(par[0]).split()[1]
        nome2 = str(par[1]).split()[1]
        print('\n<<<   =======  Experimento Binomial =======   >>>\n')
        print(f"   alg_1 = {nome1} " )
        print(f"   alg_2 = {nome2}\n")
        print(f'   n   x  n \t | tempo alg_1 \t | tempo alg_2 \t | razão dos tempos alg_2 / alg_1 | ')

        n = VALOR_N_INICIAL
        for i in range( NUMERO_DE_ITERACOES ):
            graf2[0,i] = graf1[0,i] = n

            imagem = np.full( (n,n), 55 )
            resultados = experimento(par, (imagem, (0,0)))
            print(f'{n:4} x {n:4}\t |', end=' ')
            for res in resultados:
                print( f"({res[1]:.6f}s\t |", end=' ')
            razao = resultados[1][1]/resultados[0][1]
            graf1[1,i] = resultados[0][1]
            graf2[1,i] = resultados[1][1]
            print(f" {razao:10.2f}")
            n = 2 * n

        print("Feche a janela do gráfico para continuar e avaliar o próximo par de funções ...")
        plt.yscale('log')
        plt.grid(True)
        plt.title(f'{nome1} (azul) x {nome2} (vermelho)')
        plt.plot( graf1[0], graf1[1], 'b') # blue 
        plt.plot( graf2[0], graf2[1], 'r') # red  
        plt.plot( graf1[0], graf1[1], 'b+') # blue +  
        plt.plot( graf2[0], graf2[1], 'r*') # red  *
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
        val = f( *dados )
        t_fim = Timer()
        t_dif = t_fim - t_ini
        tempos.append( (val, t_dif) )

    return tempos

# ................................................
if __name__ == '__main__':
    main()