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
        - 

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''



## ==================================================================

import numpy as np
import random
 
def teste_vazios():
    # lista = list(np.random.randint(low = -20,high=30,size=5))
    lista = []
    print("\n\n   Teste somaR() para lista = []")
    print(f"     {lista} = {somaR(lista)}")

    print("   Teste maxR() para lista = []")
    print(f"     {lista} = {maxR(lista)}")

def main():

    n = random.randint(100,100)
    testes_soma = []
    testes_maximo = []

    for i in range(1,101):
        print()
        lista = list(np.random.randint(low = -30,high=30,size=10))
        
        soma_python = sum(lista)
        maximo_python = max(lista) # max() do python não funciona para [], ver teste_vazios()
        soma_recursiva = somaR(lista)
        maximo_recursivo = maxR(lista)

        testes_soma.append(True if soma_python == soma_recursiva else False)
        teste_soma = "CERTO" if testes_soma[-1] else "ERRADO"

        testes_maximo.append(True if maximo_python == maximo_recursivo else False)
        teste_maximo = "CERTO" if testes_maximo[-1] else "ERRADO"
        
        print(f"### Teste {i}/{n} - Soma: {teste_soma} | Máximo: {teste_maximo}")
        print(f"    lista = {lista}")
        print(f"      somaR(lista) = {soma_python} | maxR(lista)  = {maximo_python}")
        print(f"      sum(lista)   = {soma_recursiva} | max(lista)   = {maximo_recursivo}")
        
    #Contabilização dos acertos e rros das funções countruídas com base nas built-in
    acertos_soma, erros_soma = 0, 0
    for i in testes_soma:
        if i:
            acertos_soma += 1
        else:
            erros_soma += 1
    acertos_maximo, erros_maximo = 0, 0
    for i in testes_maximo:
        if i:
            acertos_maximo += 1
        else:
            erros_maximo += 1

    #Impressão dos Resultados
    print(f"\n\n###### RESULTADO DOS TESTES DE SOMA ######")
    print(f"  - Foram feitos {n} testes.\n    -> {acertos_soma} Certos\n    -> {erros_soma} Errados")
    print(f"\n###### RESULTADO DOS TESTES DE MAXIMO ####")
    print(f"  - Foram feitos {n} testes.\n    -> {acertos_maximo} Certos\n    -> {erros_maximo} Errados")

    
## ------------------------------------------------------------------

def maxR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
        Exemplos: 
        - para a entrada [12, 15, 7], a funcao deve retornar 15.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar None.

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa max() do Python para resolver esse exercício.
    '''
    if lista == []: return None
    if len(lista) == 1: return lista[0]

    temp = maxR(lista[1:])

    if lista[0] > temp:
        return lista[0]
    else:
        return temp


## ------------------------------------------------------------------

def somaR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna a soma de todos os elementos da lista.
        Exemplo: 
        - para a entrada [12, -15, 7], a funcao deve retornar 4.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar 0 (zero).

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa sum() do Python para resolver esse exercício.
    '''

    if len(lista) == 0:
        return 0
    else:
        return lista[-1] + somaR(lista[:-1])

## ------------------------------------------------------------------

if __name__ == '__main__':
    main()
    teste_vazios()