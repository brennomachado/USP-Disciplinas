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

import numpy as np

## ==================================================================

def main ():
    x = [    
            1, 8, 7, 6, 1, 4,
            1, 8, 1, 1, 1, 3,
            1, 0, 2, 1, 2, 8,
            1, 1, 1, 1, 0, 3,
            5, 9, 1, 0, 1, 1,
            9, 9, 9, 0, 1, 0
        ]

    img = np.array(x).reshape(6,6)
    print(f'Imagem\n', img)
    
    sementes = [(0,0), (5,4)]

    nova_cor = -1
    for s in sementes:
        res = segmente_blob(img, s)
        print(f'\nSegmentei {len(res)} pixels a partir de {s}')
        print( res )

        pinte_blob(img, res, nova_cor)
        print(f'\nimagem pintada')
        print(img)
        nova_cor -= 1

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
    if semente in visitados:
        return None
    else:
        visitados.add(semente)

        # Guardando as coordernadas de possíveis novos vizinhos
        semente_cima = (semente[0]-1, semente[1])
        semente_baixo = (semente[0]+1, semente[1])
        semente_direita = (semente[0], semente[1]+1)
        semente_esquerda = (semente[0], semente[1]-1)

        # Sequência de if que verificam se a coordenada é válida na imagem e
        # se vizinho é da mesma cor antes de fazer chamadas recursivas
        if semente_cima[0] > -1:
            if img[semente] == img[semente_cima]:
                segmente_blob_RM( img, semente_cima, visitados)
        if semente_baixo[0] < img.shape[0]:
            if img[semente] == img[semente_baixo]:
                segmente_blob_RM( img, semente_baixo, visitados)
        if semente_direita[1] < img.shape[1]:
            if img[semente] == img[semente_direita]:
                segmente_blob_RM( img, semente_direita, visitados)
        if semente_esquerda[1] > -1:
            if img[semente] == img[semente_esquerda]:
                segmente_blob_RM( img, semente_esquerda, visitados)

    return visitados

## ==================================================================

def pinte_blob( img, blob, nova_cor = 0):
    ''' (ndarray, set, int) -> None

    Recebe um ndarray img e um conjunto de pixels blob
    e pinta esses pixels com a nova_cor.

    '''
    for elemento in blob:
        img[elemento] = nova_cor


## ==================================================================

if __name__ == '__main__':
    main()
