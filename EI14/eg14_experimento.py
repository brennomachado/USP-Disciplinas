# carrega as suas funções iterativas e recursivas
from eg_recursao import somaR, maxR, somaI, maxI

## talvez seja necessário alterar o tamanho da pilha de recursão.
MAX_PILHA = 100000
import sys
sys.setrecursionlimit(MAX_PILHA)  

import random
from timeit import default_timer as Timer

MAX_VAL = 1

# ................................................
'''
main()
    essa função roda o experimento que compara os
    tempos de execução das versões iterativa e
    recursiva de cada função.
'''
def main():

    ## lista com os pares de funções a serem comparadas
    funcoes = [[somaI, somaR], [maxI, maxR]]  

    for par in funcoes:
        print('\n<<<   ===========   >>>\n')
        print(f"Experimento: {par[0]} x {par[1]}\n")
        print(f"n\t | (res I) - tempo I\t |  (res R) - tempo R\t |  tempo R / tempo I | ")

        n = 500
        for i in range(7):
            lista = sorteia_lista(n)
            tmp = experimento( lista, par )
            s = f'{n}\t | '
            for t in tmp:
                s += f"({t[0]}) - {t[1]}\t | "
            razao = tmp[1][1]/tmp[0][1]
            print(s+str(razao))
            #n+=1
            n = 2 * n

# ................................................

def experimento( lista, funcoes ):
    ''' (list, list) -> list
    Recebe uma lista com inteiros que é usada como entrada para as
    funções na lista funcoes. 
    Retorna uma lista com os valores e tempos de cada função.
    '''
    tempos = []
    for f in funcoes:
        t_ini = Timer()
        print(f"FUNÇÂO: {f}")
        val = f( lista )
        print("Fiz")
        t_fim = Timer()
        t_dif = t_fim - t_ini
        tempos.append( (val, t_dif) )
    
    
    return tempos

# ................................................
def sorteia_lista( n ):
    ''' int -> list
    Recebe um inteiro n e retorna uma  
    uma lista com n valores inteiros aleatórios no intervalo MAX_VAL
    '''
    lista = []
    for i in range(n):
        lista+=[random.randint(1, MAX_VAL)]
        #lista.append( random.randrange(1, MAX_VAL))
    print("Sorteado")
    return lista

# ................................................
if __name__ == '__main__':
    main()
