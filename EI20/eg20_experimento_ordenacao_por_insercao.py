# -*- coding: utf-8 -*-
"""eg20 experimento ordenacao por insercao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RA1UlaK1fbtSCaDJOFhxplSpaQVaTYd6
"""

'''
    MAC0122 - Princípios de Desenvolvimento de Algoritmos

    Experimento
    Análise de algoritmos de ordenação simples.
    Todos os algoritmos são comparados com o sort nativo do Python.
    
    Tópico: análise dos algoritmos

    - Ordenação por inserção
    - Ordenação por seleção
    - Ordenação por inserção binária

    Data da última atualização:8/11/2021

'''
################################################################
# carrega as coisas do Python

# sys para controlar o tamanho da pilha de recursão
import sys
import random
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
from eg_insercao import *

################################################################
################################################################
# configuração da pilha e constantes do experimento.
# Essas constantes podem ser alteradas para adaptá-las a sua máquina

MAX_PILHA_RECURSAO = 1000000
sys.setrecursionlimit(MAX_PILHA_RECURSAO)  


## Avaliação em pares
## insira/remova/edite os pares de funções na lista para serem avaliadas
PARES_DE_FUNCOES = [
    [ ordene_por_insercao, ordene_por_selecao], 
#    [ ordene_por_insercao_binaria, ordene_por_selecao], 
#   [ ordene_por_insercao_binaria, ordene_por_insercao], 
    ]

## listas de tamanho N
VALOR_N_INICIAL = 100
NUMERO_DE_ITERACOES = 7  # cada iteração dobra o valor de N
REP_POR_ITERACAO = 5     # repetições para analisar o tempo médio

## outras constantes
ESCALA_LOG = True

SEQ_STEP = 100      # passo médio entre elementos da seq
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
        print( '   n   \t | tempo alg_1 \t | tempo alg_2 \t | razão dos tempos alg_2 / alg_1 | ')

        n = VALOR_N_INICIAL
        for i in range( NUMERO_DE_ITERACOES ):
            graf2[0,i] = graf1[0,i] = n

            res1 = experimento(par[0], REP_POR_ITERACAO, n)
            res2 = experimento(par[1], REP_POR_ITERACAO, n)

            print( f"{n:6}\t|", end=' ')
            print( f"({res1:.6f}s\t |", end=' ')
            print( f"({res2:.6f}s\t |", end=' ')
            razao = res2 / res1
            print( f"{razao:10.2f}")

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
    Recebe o nome de uma função de ordenacao.
    Cria rep listas de tamanho n.
    Para cada lista, mede o tempo de ordenação e 
    Retorna o tempo médio.
    '''
    
    t_dif = 0
    for i in range(rep):
        seq = gera_seq(n)

        t_ini = Timer()
        funcao( seq )
        t_fim = Timer()
        t_dif += t_fim - t_ini
        
    return t_dif / rep

# ................................................

def gera_seq( n ):
    
    seq = np.zeros(n, int)
    for i in range (n):
        seq[i] = random.randrange(SEQ_STEP) + i * SEQ_STEP    

    if  OPCAO == ALEATORIA:
        random.shuffle( seq )  
    elif OPCAO == DECRESCENTE:
        seq = seq[::-1]

    if DEBUG:
        print(OPCAO, seq[:10])
    return seq

# ................................................

if __name__ == '__main__':
    main()