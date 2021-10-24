# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome:
    NUSP:

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

## ==================================================================

def segmente_blob( img, semente ):
    ''' (ndarray, tuple) -> set

        interface para a função segmente_blob_RM.
        Cria um conjunto vazio que é carregado
        de forma recursiva.  
        
        Não altere essa função.
    '''
    return segmente_blob_RM( img, semente, set() )

def segmente_blob_RM( img, semente, visitados ):
    ''' (ndarray, tuple, set) -> set

    Recebe um ndarray img e uma tupla semente contendo a
    coordenada de um pixel de img. Recebe também o conjunto
    visitados, que contém as coordenadas dos pixels já 
    visitados.

    DICA: uma ideia de algoritmo recursivo é
    - se a semente já foi visitada, retorna None.
    - caso contrário, 
        - marca a semente como visitada e
        - propaga recursivamente para os vizinhos de mesma cor.
    '''

    print("Vixe! Ainda não fiz a função semente_blob_RM.")

## ==================================================================

def pinte_blob( img, blob, nova_cor = 0):
    ''' (ndarray, set, int) -> None

    Recebe um ndarray img e um conjunto de pixels blob
    e pinta esses pixels com a nova_cor.

    '''

    print("Vixe! Ainda não fiz a função pinte_blob.")

## ==================================================================
## Coloque aqui outras funções que desejar

