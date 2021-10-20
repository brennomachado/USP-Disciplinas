# -*- coding: utf-8 -*-
"""eg_fibonacci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yZ3a45odewmdLrW8OF4DS8QGBklqavq8
"""

# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: 6434401

    Nome: Joao Victor Passos Goncalves
    NUSP: 12557716

    Nome: Marcio Martins Jacob
    NUSP: 10801127

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
        - 

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''
## ==================================================================
from timeit import default_timer as timer

def main():
    
    for i in [128]:
        start = timer()
        fibo = fibonacciR2(i)
        end = timer()
        print(f"FibonacciR2({i}) = {fibo}   =>   Tempo = {end - start}s")

        start = timer()
        fibo = fibonacciI(i)
        end = timer()

        print(f"FibonacciI({i}) = {fibo}   =>   Tempo = {end - start}s\n")

def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''

    if n == 0: return 0
    elif n == 1: return 1
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''

    termo1, termo2 = 0, 1
    for i in range(n):
        termo1, termo2 = termo2, termo1 + termo2
    return termo1

def fibonacciR2(n):
    ''' (int) -> int
    interface para que possamos usar a função fibonacciRM da mesma forma
    que a função fibonacciR, ou seja, com apenas um parâmetro n.
    A função cria uma lista onde os valores intermediários são armazenados e, dessa forma, evita que um mesmo valor
    precise ser recalculado várias vezes.
    '''
    ## Vamos usar None para indicar que o valor ainda não foi calculado
    rascunho = [None] * (n+1)
    rascunho[0] = 0  # caso base
    rascunho[1] = 1  # caso base
    return fibonacciRM(n, rascunho)

def fibonacciRM(n, rascunho):
    '''(int, list) -> int

    Recebe um inteiro não negativo n e uma lista rascunho para armazenar os valores intermediários. A função primeiro verifica se o valor já está calculado no rascunho e, caso esteja, retorna esse valor. Caso contrário, calcula o valor de forma recursiva, armazena 
    o valor no rascunho e retorna o valor.
    '''

    if rascunho[n] != None:
        return rascunho[n]
    else:
        rascunho[n] = fibonacciRM(n-1,rascunho) + fibonacciRM(n-2,rascunho)
        return rascunho[n]

## ------------------------------------------------------------------
if __name__ == '__main__':
    main()