
# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: 6434401

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

TAMANHO_MAX_DAS_LISTAS = 15
NUM_TESTE_EM_CADA_TAMANHO = 1
LIMITE_INFERIOR_DA_LISTA = -50
LIMITE_SUPERIOR_DA_LISTA = 200

def main():
    
    seq = [7, 4, 11, 5, 3]
    
    print(f"Lista original: {seq}")
    t, c = ordene_por_borbulhagemX(seq)
    print(f"trocas: {t}  comparações: {c}")
    print(f"Lista ordenada: {seq}\n")
    
    
    seq = [5, 3, 11, 4, 7]
    print(f"Lista original: {seq}")
    t, c = ordene_por_borbulhagemX(seq)
    print(f"trocas: {t}  comparações: {c}")
    print(f"Lista ordenada: {seq}\n")
    
    
    seq = [5, 3, 4, 7, 11]
    print(f"Lista original: {seq}")
    t, c = ordene_por_borbulhagemX(seq)
    print(f"trocas: {t}  comparações: {c}")
    print(f"Lista ordenada: {seq}\n")

    # for k in range(1, TAMANHO_MAX_DAS_LISTAS+1):
    #     print(f"## Listas de tamanho: {k} ##")
    #     for i in range(NUM_TESTE_EM_CADA_TAMANHO):
    #         print(f"   Teste nº {i+1} para tamanho {k}:")
    #         lista = list(np.random.randint(low = LIMITE_INFERIOR_DA_LISTA,high=LIMITE_SUPERIOR_DA_LISTA,size=k))
    #         print(f"      Lista: {lista}")
    #         print(f"      Lista ordenada em {ordene_por_borbulhagem(lista)} passos: {lista}\n")
    #     print("")
        

def borbulhe(seq, n):
    ''' (list, int) -> int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso 
    deve ser da posição de índice 0 até a *posição de índice n* (item/elemento n, não índice). 

    Durante o percurso a função COMPARA todos os pares de valores 
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5] 
    e seq[6] e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

    Se os valores comparados não estiverem em ordem crescente, eles devem ser
    TROCADOS de posições. Por exemplo, para 
        seq = [w, x, y, 7, 5, z] 

    a comparação de seq[3]=7 e seq[4]=5 deve resultar na troca de seus valores. 
    A lista deve ser modificada de tal forma que tenhamos  
        seq = [w, x, y, 5, 7, z], 

    em que os valores w, x, y e z são irrelevantes.

    RETORNA o número de trocas realizadas durante o percurso.

    Esta função será o coração de mais um algoritmo de ordenação que nos 
    apresentará novas ideias.

    EXEMPLOS:

        In [24]: seq = [7, 4, 11, 5, 3]
        In [25]: t = borbulhe(seq, 3)
        In [26]: t
        Out[26]: 1
        In [27]: seq
        Out[27]: [4, 7, 11, 5, 3]

        In [28]: seq = [7, 4, 11, 5, 3]
        In [29]: t = borbulhe(seq, 4)
        In [30]: t
        Out[30]: 2
        In [31]: seq
        Out[31]: [4, 7, 5, 11, 3]

        In [32]: seq = [7, 4, 11, 5, 3]
        In [33]: t = borbulhe(seq, 5)
        In [34]: t
        Out[34]: 3
        In [35]: seq
        Out[35]: [4, 7, 5, 3, 11]

    SUGESTÃO: não use listas auxiliares como fatias. Basta
    percorrer seq, comparar pares vizinhos e trocar quando
    necessário.
    '''
    trocas_feitas = 0
    for i in range(1,n):
        if seq[i-1] > seq[i]:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            trocas_feitas += 1
    
    return trocas_feitas
        
## ==================================================================

def ordene_por_borbulhagem(seq):
    ''' (list) -> int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem ordenados.

    Esta função DEVE APLICAR repetidas vezes a função borbulhe() sobre a 
    lista seq até que seq esteja ordenada. 

    RETORNA o número total de trocas realizadas durante a ordenação. 

    Cada vez que a função borbulhe() é aplicada sobre a lista seq, os elementos
    da lista ficam mais próximos de seus lugares na lista ordenada.

    EXEMPLO. Suponha que seq = [7, 4, 11, 5, 3]. 
    Após aplicarmos borbulhe() sobre a lista seq na
 
        * primeira vez, obtemos seq=[4, 7, 5, 3, 11], com  3 trocas
        * segunda  vez, obtemos seq=[4, 5, 3, 7, 11], mais 2 trocas
        * terceira vez, obtemos seq=[4, 3, 5, 7, 11], mais 1 troca
        * quarta   vez, obtemos seq=[3, 4, 5, 7, 11], mais 1 troca

    Pronto! A lista seq está ordenada.
    Para seq = [7, 4, 11, 5, 3] a função deve retornar 7.
    '''
    n = len(seq)
    total_de_trocas = 0
    while True:
        trocas = borbulhe(seq,n)
        n -= 1
        if trocas == 0:
            break
        else: 
            total_de_trocas += trocas
    
    return total_de_trocas
            
## ==================================================================    

def borbulheX(seq, n):
    '''(list, int) -> int, int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso deve
    ser da posição de índice 0 até a posição de índice n. 

    Durante o percurso a função COMPARA todos os pares de valores 
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5] e 
    seq[6] e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

    Se os valores comparados não estiverem em ordem crescente, eles devem ser 
    TROCADOS de posições. 

    RETORNA o número de trocas E o maior índice de uma posição de seq
    que foi alterada durante o percurso.

    Se nenhum posição de seq foi alterada a função deve retorna o par (0, 0).

    Aqui estão alguns exemplos de execução da função.

        In [4]: seq = [7, 4, 11, 5, 3]
        In [5]: t, u = borbulheX(seq, 3)
        In [6]: t # trocas
        Out[6]: 1
        In [7]: u # índice
        Out[7]: 1
        In [8]: seq
        Out[8]: [4, 7, 11, 5, 3]

        In [9]: seq = [7, 4, 11, 5, 3]
        In [10]: t, u = borbulheX(seq, 4)
        In [11]: t # trocas
        Out[11]: 2
        In [12]: u # índice
        Out[12]: 3
        In [13]: seq
        Out[13]: [4, 7, 5, 11, 3]

        In [18]: seq = [7, 4, 11, 5, 3]
        In [19]: t, u = borbulheX(seq, 5)
        In [20]: t # trocas
        Out[20]: 3
        In [21]: u # índice
        Out[21]: 4
        In [22]: seq
        Out[22]: [4, 7, 5, 3, 11]
    '''

    trocas_feitas = 0
    ultima_posicao_trocada = 0
    
    for i in range(1,n):
        i_anterior = i-1
        if seq[i_anterior] > seq[i]:
            seq[i_anterior], seq[i] = seq[i], seq[i_anterior]
            trocas_feitas += 1
            ultima_posicao_trocada = i
    
    return trocas_feitas, ultima_posicao_trocada

def ordene_por_borbulhagemX(seq):
    '''(list) -> int, int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem ordenados.
 
    Esta função DEVE APLICAR repetidas vezes a função borbulheX() sobre a 
    lista seq até que seq esteja ordenada. 

    RETORNA o número total de trocas __e__ o número total de
    comparações realizadas durante a ordenação.
 
    Hmm. Como podemos utilizar os valores retornados por borbulheX() e
    o parâmetro n para _possivelmente_ evitarmos comparações
    desnecessárias entre posições vizinhas de seq?

    SUGESTÃO. Busquem inspiração examinando o comportamento da função 
    ordene_por_borbulhagem(). 
    Aqui vão alguns exemplos.

        In [24]: seq = [7, 4, 11, 5, 3]
        In [25]: t, c = ordene_por_borbulhagemX(seq)
        In [26]: t # trocas
        Out[26]: 7
        In [27]: c # comparações
        Out[27]: 10
        In [28]: seq
        Out[28]: [3, 4, 5, 7, 11]

        In [29]: seq = [5, 3, 11, 4, 7]
        In [30]: t, c = ordene_por_borbulhagemX(seq)
        In [31]: t # trocas
        Out[31]: 4
        In [32]: c # comparações
        Out[32]: 8
        In [33]: seq
        Out[33]: [3, 4, 5, 7, 11]

        In [34]: seq = [5, 3, 4, 7, 11]
        In [35]: t, c = ordene_por_borbulhagemX(seq)
        In [36]: t # trocas
        Out[36]: 2 
        In [37]: c # comparações
        Out[37]: 5
        In [38]: seq
        Out[38]: [3, 4, 5, 7, 11]
    '''
    
    ultimo_indice_ordenado = len(seq) # primeira iteração é coma lista toda
    total_de_trocas = 0
    comparacoes = ultimo_indice_ordenado - 1
    while True:
        trocas,ultimo_indice_ordenado = borbulheX(seq,ultimo_indice_ordenado)
        if trocas == 0:
            break
        else: 
            comparacoes += ultimo_indice_ordenado - 1
            total_de_trocas += trocas
    
    return total_de_trocas, comparacoes

## ==================================================================    
if __name__ == '__main__':
    main()
