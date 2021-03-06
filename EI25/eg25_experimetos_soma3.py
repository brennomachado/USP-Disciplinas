# -*- coding: utf-8 -*-
"""EG25: experimetos Soma3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KNd71KVhhDCIKqBDy-iKrr460t8IDGvG
"""

'''
    MAC0122 - Princípios de Desenvolvimento de Algoritmos

    PROBLEMA: dada uma lista de números inteiros, determinar o 
          número de trios que somam zero.

    TÓPICO: análise dos algoritmos

    - Soma3.forca_bruta() 
    - Soma3.busca_binaria()
    - Soma3.dicionario()
    - Soma3.misterio()

    DATA DA ÚLTIMA ATUALIZAÇÃO: 22/11/2021
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
# CARREGA: classe Soma3
from eg_soma3 import *

# coordenadas
X = 0
Y = 1

# outras constantes
ESCALA_LOG = False # True

# para reprodutibilidade
SEMENTE = 0

#-----------------------------------------------------------
# ESCOLHA 1: escolha apenas 1 método
# METODO = Soma3.forca_bruta
# METODO = Soma3.busca_binaria
# METODO = Soma3.dicionario
METODO = Soma3.misterio

#-----------------------------------------------------------
# ESCOLHA 2: escolha, como moderação, o número de pontos
#    no gráfico (= número de tamanhos de listas)
NO_PONTOS = 12

#---------------------------------------------------------
# Não precisa mexer em mais nada
POT_MIN = 4
POT_MAX = POT_MIN+NO_PONTOS-1
MIN = 2**POT_MIN
MAX = 2**POT_MAX

#--------------------------------------------------------
STR_METODO = f"{METODO}".split()[1][6:] # Que horror!
CABECALHO  = f"         n {STR_METODO:>15}      cont"

def main():
    print(f"Testes para 3SUM")
    print(CABECALHO)
    pontos = np.zeros((2,NO_PONTOS))
    k = 0
    i = MIN
    random.seed(SEMENTE)
    while i <= MAX:
        # sorteio de uma lista com i inteiros DISTINTOS
        # os inteiros estão no intervalo range(-i, i+1)
        v = random.sample(range(-i, i+1), i)

        #----------------------------------------
        # 3SUM versão {METODO}
        t, cont = cronometre(METODO, v) 

        #--------------------------------------
        # registre o ponto
        pontos[X,k], pontos[Y,k] = i, t
        k += 1
        
        # exiba resultados
        print(f"{i:10} {t:12.2f} {cont:12}")
        
        # dobre o tamanho da entrada
        i *= 2

    print("tempos em segundos\n")    
    print("Para encerra feche a janela...")
    if ESCALA_LOG: plt.yscale('log')
    plt.grid(True)
    plt.title(f'{STR_METODO}')
    plt.plot( pontos[X], pontos[Y], 'b') # blue 
    plt.plot( pontos[X], pontos[Y], 'b+') # blue +  
    plt.show()
    print("Fui!")

#-------------------------------------------              
def cronometre(f, v):
    '''(callable, list) -> float
    RECEBE uma método f da classe Soma3 e uma lista v.
    RETORNA o tempo gasto e valor retornado pela execução de f(s3)
        em que s3 = Soma3(v).
    '''
    # crie objeto
    s3 = Soma3(v)
    # cronometre o tempo
    t_ini = Timer()
    valor = f(s3)
    t_fim = Timer()
    elapsed = t_fim-t_ini
    return elapsed, valor

#---------------------------------------------------
if __name__ == '__main__':
    main()