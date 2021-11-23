# -*- coding: utf-8 -*-
"""Copy of Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pCS9zCHO0KL9td4sOXRNzco6cxcN0NHg
"""

'''
    MAC0122 - Princípios de Desenvolvimento de Algoritmos

    EXPERIMENTO: Análise de algoritmos de ordenação.

    TÓPICO: análise dos algoritmos

    - quicksortI X heapsort 
    - list.sort  X heapsort
    - list.sort  X quicksortI

    DATA DA ÚLTIMA ATUALIZAÇÃO: 21/11/2021
'''
#------------------------------------------------------------
# carrega as coisas do Python

# random.shuffle()
import random

# timer para medir tempos de execução
from timeit import default_timer as Timer

# GERA gráficos usando pyplot
# Para saber mais sobre pyplot: 
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#logarithmic-and-other-nonlinear-axes
import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------------------
# CARREGA
#   - heapsort
#   - quicksortI
#   - mergesortI
from eg_heap import *

#-----------------------------------------------------------
# escolha os pares de funções a serem avaliadas
PARES_DE_FUNCOES = [
    [ quicksortI, heapsort  ],
    [  list.sort, heapsort  ],
    [  list.sort, quicksortI],
]

# listas de tamanho N
VALOR_N_INICIAL     = 1000
NUMERO_DE_ITERACOES = 10  # cada iteração dobra o valor de N
REP_POR_ITERACAO    = 4   # repetições para analisar o tempo médio

# outras constantes
ESCALA_LOG = False # True
SEQ_STEP = 100     # passo médio entre elementos da seq

#-----------------------------------------------------------
ALEATORIA   = 'aleatoria'
CRESCENTE   = 'crescente'
DECRESCENTE = 'decrescente'
#OPCAO = CRESCENTE
#OPCAO = DECRESCENTE
OPCAO = ALEATORIA

################################################################
#
# não deve ser necessário alterar mais nada daqui para baixo...
#
################################################################

DEBUG = False

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

        print('\n<<<   =======  ALGORITMOS DE ORDENAÇÃO =======   >>>\n')

        print(f"   Análise usando lista: *** {OPCAO} ***\n")
        print(f"   alg_1 = {nome1} " )
        print(f"   alg_2 = {nome2} \n")
        print( '       n |   alg_1 (s)\t|   alg_2 (s)\t| alg_1/alg_2  ')

        n = VALOR_N_INICIAL
        for i in range( NUMERO_DE_ITERACOES ):
            graf2[0,i] = graf1[0,i] = n

            res1 = experimento(par[0], REP_POR_ITERACAO, n)
            res2 = experimento(par[1], REP_POR_ITERACAO, n)

            print( f"{n:8} |", end=' ')
            print( f"{res1:10.6f}\t|", end=' ')
            print( f"{res2:10.6f}\t|", end=' ')
            razao = res1 / res2
            print( f"{razao:8.2f}")

            graf1[1,i] = res1
            graf2[1,i] = res2
            n = 2 * n

        print("Feche a janela do gráfico para continuar e avaliar o próximo par de funções ...")
     
        if ESCALA_LOG:
            plt.yscale('log')
        plt.grid(True)
        plt.title(f'{nome1} (azul) x {nome2} (vermelho)')
        plt.plot( graf1[0], graf1[1], 'b') # blue 
        plt.plot( graf2[0], graf2[1], 'r') # red  
        plt.plot( graf1[0], graf1[1], 'b+') # blue +  
        plt.plot( graf2[0], graf2[1], 'r*') # red  *
        plt.show()

# ................................................

def experimento(funcao, rep, n):
    ''' ( func, int, int ) -> float
    RECEBE uma função funcao e inteiros rep e n.
    CRIA rep listas com n elementos. Para cada lista, cronometra
        o tempo gasto pela função tendo a lista como argumento.
    RETORNA o tempo médio.
    '''
    t_dif = 0
    for i in range(rep):
        # cria uma sequência com n elementos
        seq = gera_seq(n)
        # inicie o cronômetro
        t_ini = Timer()
        # execute a função
        funcao( seq )
        # pare o cronômetro
        t_fim = Timer()
        t_dif += t_fim - t_ini
        
        if DEBUG: 
            for i in range(n-1):
                if seq[i] > seq[i+1]:
                    print(f"SOCORRO! A função {funcao} não ordenou a lista! (҂◡_◡)")
    # retorne o tempo médio consumo por ordenação        
    return t_dif / rep

# ................................................

def gera_seq( n ):
    '''(int) -> list
    RECEBE um inteiro n.
    RETORNA uma lista com n números inteiros.
    '''
    seq = [random.randrange(SEQ_STEP)+i*SEQ_STEP  for i in range(n)]
    if  OPCAO == ALEATORIA:
        random.shuffle(seq)  
    elif OPCAO == DECRESCENTE:
        seq.reverse()
    if DEBUG: print(OPCAO, seq[:10])
    return seq


# ................................................

if __name__ == '__main__':
    main()