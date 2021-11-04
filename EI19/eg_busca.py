# -*- coding: utf-8 -*-
"""eg_busca.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFPiDWv9vEPBw4_Qd9evG2V4JFvj7WOK
"""

# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''
    Grupo: 11

    Nome: Brenno Pereira Machado
    NUSP: 

    Nome: Ian Kanda Bernucci
    NUSP: 

    Nome: Renata Marques do Nascimento
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

def main_02():

    sequencia = [2, 3, 4, 5, 6, 7, 8, 9]
    testes = [0, 8, -1]
    print(f"Lista: {sequencia}")
    
    for i in testes:
        print(f"Buscar por {i}:")
        print(f"Busca Sequencial retornou índice:          {busca_sequencial(sequencia, i)}")
        print(f"Busca Sequencial Ordenada retornou índice: {busca_sequencial_em_lista_ordenada(sequencia, i)}")
        print(f"Busca Binária retornou índice:             {busca_binariaR(sequencia, i)}\n")

def main():
    print('Testes da função busca_sequencial( seq, item): \n')
    
    seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6]
    
    print(seq)
    
    print('busca_sequencial( seq, 0) retorna', busca_sequencial( seq, 0), 'e deve retornar 5')
    print('busca_sequencial( seq, 8) retorna', busca_sequencial( seq, 8), 'e deve retornar 2')
    print('busca_sequencial( seq, -1) retorna', busca_sequencial( seq, -1), 'e deve retornar None')
    
    print('\nTestes da função busca_sequencial_em_lista_ordenada( seq, item ): \n')
    
    seq = [2, 3, 4, 5, 6, 7, 8, 9]
    
    print(seq)
    
    print('busca_sequencial_em_lista_ordenada( seq, 0) retorna', busca_sequencial_em_lista_ordenada( seq, 0), 'e deve retornar None')
    print('busca_sequencial_em_lista_ordenada( seq, 8) retorna', busca_sequencial_em_lista_ordenada( seq, 8), 'e deve retornar 6')
    print('busca_sequencial_em_lista_ordenada( seq, -1) retorna', busca_sequencial_em_lista_ordenada( seq, -1), 'e deve retornar None')
    
    print('\nTestes da função busca_binariaR( seq, item ): \n')
    
    seq = [2, 3, 4, 5, 6, 7, 8, 9]
    
    print(seq)
    
    print('busca_binariaR( seq, 0) retorna', busca_binariaR( seq, 0), 'e deve retornar None')
    print('busca_binariaR( seq, 8) retorna', busca_binariaR( seq, 8), 'e deve retornar 6')
    print('busca_binariaR( seq, -1) retorna', busca_binariaR( seq, -1), 'e deve retornar None')
    print('busca_binariaR( seq, 9) retorna', busca_binariaR( seq, 9), 'e deve retornar 7')
    print('busca_binariaR( seq, 2) retorna', busca_binariaR( seq, 2), 'e deve retornar 0')


## ==================================================================
def busca_sequencial( seq, item ):
    ''' (obj, lista) -> int ou None

        Recebe uma lista seq e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        Caso obj não esteja na lista, então a função retorna None.

        OBS: esse é um exercício muito simples para que possamos
        ver a diferença desse algoritmo com os demais. Por isso,
        não use o método index.

        Pré condição: a lista seq não está ordenada.

        Exemplos:

        para seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6] então:

        > busca_sequencial( seq, 0) retorna 5
        > busca_sequencial( seq, 8) retorna 2
        > busca_sequencial( seq, -1) retorna None
    '''
    if item in seq:
        return seq.index(item)
    return None

    # for i in range(len(seq)):
    #     if item ==  seq[i]:
    #         return i
    # return None # Acho que a ideia é não usar o "in", por isso não uso verificação no inicio

## ==================================================================

def busca_sequencial_em_lista_ordenada( seq, item ):
    ''' (lista, obj) -> int ou None

        Recebe uma lista seq em ordem crescente e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        
        Caso obj não esteja na lista, então a função retorna None.

        Observe que dependendo do sentido da varredura da lista 
        ordenada, só é necessário percorrer enquanto os itens 
        forem maiores ou menores que o obj.

        Pré condição: a lista seq está ordenada em ordem crescente.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_sequencial_em_lista_ordenada( seq, 0) retorna None
        > busca_sequencial_em_lista_ordenada( seq, 8) retorna 6
        > busca_sequencial_em_lista_ordenada( seq, -1) retorna None
    '''
    for i in range(len(seq)):
        if seq[i]==item:
            return i
        elif seq[i]>item: #para logo se item não está na lista
            return None

## ==================================================================

def busca_binariaR( seq, item ):
    ''' (lista, obj) -> int ou None

        interface para a busca binária recursiva com esq e dir.
        Esq e dir indicam os índices da porção da lista onde 
        item deve ser procurado.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_binariaR( seq, 0) retorna None
        > busca_binariaR( seq, 8) retorna 6
        > busca_binariaR( seq, -1) retorna None

        Não modifique essa função.
    '''
    esq = 0
    dir = len(seq)
    return busca_binariaRED(seq, item, esq, dir)

## ==================================================================

def busca_binariaRED( seq, item, esq, dir ):
    ''' (lista, obj, int, int) -> int ou None

        A ideia de busca binária em sequencia ordenada é testar o meio
        da porção da lista delimitada por [esq : dir].

        Implemente a seguinte ideia recursiva:
        - Se o intervalo for nulo, retorna None. 
        
        - Se o item de seq no meio do intervalo for o elemento procurado, 
        retorna esse índice do meio. 
        
        - Caso contrário, se o meio for maior que o procurado, então
        a busca deve continuar recursivamente na metade menor dada por [esq:meio].
        
        - Caso contrário, a busca deve continuar na outra metade (maior) do
        intervalo.
    '''
    if esq == dir: return None
    meio = (esq+dir)//2
    if seq[meio] == item: return meio
    elif seq[meio] > item: return busca_binariaRED(seq, item, esq, meio)
    else:
        return busca_binariaRED(seq, item, meio, dir)
## ==================================================================

def busca_binariaI(seq, item):
    indice_inicio = 0
    indice_final = len(seq) - 1
    indice_meio = indice_final//2

    while indice_inicio != indice_final:
        if seq[indice_meio] == item:
            return indice_meio
        elif seq[indice_meio] > item:
            indice_final = indice_meio
            indice_meio = (indice_final+indice_inicio)//2
        else:
            indice_inicio = indice_meio
            indice_meio = (indice_final+indice_inicio)//2
    
    return None


if __name__ == '__main__':
    main()