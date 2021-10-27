# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: -

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que trabalhos sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    
    Estou ciente que os casos de plágio e desonestidade acadêmica
    estarão sujeitos às penalidades descritas na página da disciplina
    na seção "Sobre colaboração em MAC0122".

    Reconheço que utilizei as seguintes fontes externas ao conteúdo 
    utilizado e recomendado em MAC0122, ou recebi auxílio das pessoas
    listadas abaixo.

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - Triângulo de Pascal: https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Pascal

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''

import numpy as np

## CONSTANTES

DEBUG = False

## ==================================================================

def main():

    for n,k in [(0,0),(3,2),(5,1),(1,5),(4,2),(3,6), (6,3)]:
        print(f"BinomialR ({n},{k}) = {binomialR(n,k)}")
        print(f"BinomialI ({n},{k}) = {binomialI(n,k)}\n")


def binomialI(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialI(3,2)  -> deve retornar 3
    b) binomialI(5,1)  -> deve retornar 5
    c) binomialI(1,5)  -> deve retornar 0
    d) binomialI(4,2)  -> deve retornar 6

    NOTA. Está função é iterativa.
    '''
    triangulo = np.zeros((n+1, k+1), int) 

    triangulo[:,0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            triangulo[i][j] = triangulo[i-1][j] + triangulo[i-1][j-1]

    return triangulo[n][k]


## ==================================================================

def binomialR(n, k):
    '''(int,int) -> int

    RECEBE inteiros não-negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialR(3,2)  -> deve retornar 3
    b) binomialR(5,1)  -> deve retornar 5
    c) binomialR(1,5)  -> deve retornar 0
    d) binomialR(4,2)  -> deve retornar 6

    NOTA. Está função é uma interface para a função 
          binomialRM() e não deve ser alterada.
    '''
    # cria um array de dimensão (n+1)x(k+1) para ser usado como rascunho
    rascunho = np.zeros((n+1, k+1), int) 
    rascunho[:,0] = 1

    bin = binomialRM(n, k, rascunho)
    if DEBUG:
        print("Debug ligado.")
        print(f"bin({n}, {k}) = {bin}")
        print(f"   Rascunho:\n{rascunho}")

    return bin

## ==================================================================

def binomialRM(n, k, rascunho):
    '''(int, int, array) -> int

    RECEBE inteiros não negativos n e k e um array bidimensional rascunho.
    RETORNA o valor de binomial(n,k).

    NOTA. Está função é recursiva.
        Ela usa as posições do array rascunho para  guardar os valores dos 
        binomiais já calculado: 
           - rascunho[i][j] armazenará o valor de binomial(i, j).
        Com isso a função evita que um mesmo número binomial seja recalculado 
        várias vezes.
    '''
    if rascunho[n][k] != 0:
        return rascunho[n][k]
    elif n == 0 and k == 0: return 1
    elif n < 1 or k < 1: return 0
    else:
        rascunho[n][k] = binomialRM(n-1, k, rascunho) + binomialRM(n-1, k-1, rascunho)
        return rascunho[n][k] 

if __name__ == '__main__':
    main()