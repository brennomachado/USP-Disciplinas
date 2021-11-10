 # -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: 6434401
    ### Acabei fazendo sozinho pois não estava bem para fazer em grupo hoje.###

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
import numpy as np

def main():
    '''
        Testes das suas funções
    '''
    for i in range(10):
            
        lista = list(np.random.randint(low = -200,high=200,size=15))
        print(f"Teste nº {i+1}")
        print(f"Lista antes da ordenação:  {lista}")
        ordene_por_selecao(lista)
        print(f"Lista depois da ordenação: {lista}\n")


def main2():
    '''
        Testes das suas funções
    '''
    for i in range(30):
            
        lista = list(np.random.randint(low = -200,high=200,size=15))
        print(f"Teste nº {i+1}")
        print(f"Lista antes da ordenação:  {lista}")
        ordene_por_insercao(lista)
        print(f"Lista depois da ordenação: {lista}\n")

## ==================================================================

def insira_ultimo(seq, n):
    ''' (list, int) -> None

    Essa função é a base para o algoritmo de ordenação 
    por inserção, que veremos em uma próxima aula e 
    não se trata de um algoritmo completo de ordenação.

    Essa função considerar apenas a porção da lista seq 
    no intervalo [0:n].

    A ideia é visitar cada elemento, a partir do fim da 
    porção, ou seja, do elemento de índice n-1.
    Caso o elemento anterior seja maior, os elementos são
    trocados de posição, fazendo o elemento visitado "descer"
    na lista. A varredura deve persistir enquanto o elemento 
    visitado for menor que o seu anterior.

    Por exemplo,  para seq = [4, 7, 11, 5, 3] e n = 3 a
    função não precisa fazer nada pois o elemento anterior
    ao 11 já é menor. 

    Para seq = [4, 7, 11, 5, 3] e n = 4 a
    função deve deslocar o 5 até que seq se torne 
    [4, 5, 7, 11, 3]. 

    Outro exemplo, para seq = [4, 5, 7, 11, 3] e n = 5 a
    função deve deslocar o 3 até que seq se torne 
    [3, 4, 5, 7, 11]. 

    DICA: não use outras listas, nem fatias. Basta
    varrer seq, comparar com seu vizinho anterior
    e trocar enquanto necessário.

    '''
    if n < 2: return None
    indice_atual = n-1
    indice_anterior = n-2
    while indice_atual >= 1:
        if seq[indice_atual] < seq[indice_anterior]:
            seq[indice_atual],seq[indice_anterior] = seq[indice_anterior],seq[indice_atual]
            indice_atual = indice_anterior
            indice_anterior -= 1
        else: indice_atual = -1
                     
## ==================================================================

def ordene_por_insercao(seq):
    ''' (list) -> None

    A ideia de ordenação por inserção (insertion sort)
    é considerar porções da lista, a partir de 2 elementos até n.
    Para cada porção, apenas o último elemento precisa ser 
    deslocado até sua posição correta.

    Exemplo para a lista [4, 7, 5, 3]
    - inicio com a porção da lista de tamanho 2 contendo [4, 7, ? , ?]. 
        O último elemento já está na posição correta. 
    - a ordenação continua com a porção de tamanho 3 com [4, 7, 5, ?]
        O último elemento da porção, o 5, precisa ser deslocado até
        sua posição final [4, 5, 7, ?]
    - a ordenação continua com a porção de tamanho 4, agora com 
        [4, 5, 7, 3]. O último elemento da porção, o 3, precisa ser
        deslocado até sua posição final [3, 4, 5, 7].
    - fim, pois já tratamos todas as porções até o tamanho n.

    O que você deve fazer: 

    A função recebe uma sequência de números em ordem aleatória. 
    e retorna None. Ao terminar, seq deve estar em ordem
    crescente aplicando a ideia de ordenação por inserção.

    Essa função DEVE usar a função insira_ultimo().

    '''
    tamanho_maximo = len(seq)
    n = 2
    
    while n <= tamanho_maximo:
        insira_ultimo(seq, n)
        n+=1

## ==================================================================
 
def maior_elemento(seq , n):
    ''' (lista, int) -> int 

    Essa função é a base para o algoritmo de ordenação 
    por seleção.

    RECEBE uma sequência de números em ordem aleatória. 
    A função deve considerar apenas a porção de [0:n] de seq

    RETORNA o índice do maior elemento nessa porção.
    Em caso de empate deve retornar o maior índice.

    Exemplos:

    > maior_elemento([4,7,1,7,3], 5)  - retorna 3, índice do maior
    > maior_elemento([4,7,1,7,3], 3)  - retorna 1
    > maior_elemento([4,7,1,7,3], 1)  - retorna 0

    DICA: varra seq até n, procurando pelo elemento de maior valor.
    ''' 
    maior = 0      
    for i in range(n):
        if seq[i] > seq[maior]:
            maior = i
    return maior

 ## ==================================================================

def ordene_por_selecao(seq):
    ''' (list) -> None

    A ideia de ordenação por seleção (selection sort) é considerar
    porções inicialmente de tamanho n, selecionar um elemento máximo
    e colocá-lo no final dessa porção. A ordenação deve continuar
    decrementando o tamanho da porção até chegar em uma porção 
    de tamanho 1. Uma lista de tamanho 1 já está ordenada e assim
    o processo termina.

    A função recebe uma sequência de números em ordem aleatória. 
    e retorna None. Ao terminar, seq deve estar em ordem
    crescente aplicando a ideia de ordenação por seleção.

    Essa função DEVE usar a função maior_elemento().

    '''
    num_elementos = len(seq)
    for i in range(num_elementos-1, 0, -1):
        indice_maior_elemento = maior_elemento(seq, i+1)
        seq[indice_maior_elemento],seq[i] = seq[i], seq[indice_maior_elemento]

def ordene_por_insercao_binaria(seq):
    '''(list) -> None
    RECEBE uma lista `seq`.
    REARRANJA os itens de `seq` para que fiquem em ordem
    crescente.

    A função é uma implementação de ordenação por inserção
    binária.
    '''
    n = len(seq)
    for i in range(1, n):
        x = seq[i]
        # encontre posição de x 
        j = busca_binaria(seq, lo=0, hi=i, x=x)
        # print(f"{seq}, i={i}, x={x}, j={j}")
        for k in range(i, j, -1):
            seq[k] = seq[k-1]
        # coloque x na sua posição    
        seq[j] = x

    # fim
    

def busca_binaria(seq, lo, hi, x):
    '''(list, int, obj) -> int
    RECEBE uma lista crescente `seq[lo:hi]` e um valor `x`.

    RETORNA um índice j no intervalo [lo:hi+1]. 

    Caso lo <= j < hi então
        seq[j] <= x < seq[j+1]    # qdo seq[j+1] existir

    Note que, caso j == hi, então x é maior que todos os 
    elementos de seq.
    '''
    
    #juro que não entendi ainda, vou fazer depois
        
        
    
     
## ==================================================================

if __name__ == '__main__':
    main()