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
        - https://www.youtube.com/watch?v=wx5juM9bbFo

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''

## ==================================================================
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas de tamanho mínimo, em ordem crescente,
        decrescente, etc.
        
        In [1] seq = [5, 7, 4, 3, 8, 6]
    In [2] m = pivote_seq(seq)
    
    seq = [6, 7, 5, 3, 8, 4]
    In [12] m = pivote_seq(seq)
    
    [-20, 24, 3, -8, 28, -18, 65, 81]
    [-20, 24, 3, -8, 28, -18, 81, 65]
    '''
    import numpy as np
    listas = []
    listas.append([5, 7, 4, 3, 8, 6])
    listas.append([6, 7, 5, 3, 8, 4])
    listas.append([-20, 24, 3, -8, 28, -18, 65, 81])
    
    
    for i in range(11):
        listas.append(list(np.random.randint(low = -20,high=100,size=7)))
    
    i=0
    for lista in listas:
        print(f"## Teste: {i}")
        print(f"  Lista antes da pivotação:  {lista}")
        pivo = pivote_seq(lista)
        print(f"  Lista depois da pivotação: {lista}")
        print(f"  Pivo: {pivo}\n")
        #print("######\n")
        i += 1

def pivote_seq(seq):
    ''' (list) -> int

    Recebe uma lista seq com n>0 elementos 
    e rearranja seus elementos para que o pivô, 
    o último elemento da lista,
    esteja na posição "ordenada" com relação aos demais 
    elementos, ou seja, todos os elementos menores fiquem
    a esquerda e todos os maiores fiquem a direita do pivô.

    Retorna um índice m tal que

        seq[:m] <= seq[m] < seq[m+1:]
    
    Exemplos:
    In [1] seq = [5, 7, 4, 3, 8, 6]
    In [2] m = pivote_seq(seq)
    In [3] m
    3
    In [4] seq
    [5, 4, 3, 6, 8, 7]

    ...

    In [11] seq = [6, 7, 5, 3, 8, 4]
    In [12] m = pivote_seq(seq)
    In [13] m
    1
    In [14] seq
    In [3, 4, 5, 6, 8, 7]

    DICAS:
    - observe que a pivotagem não ordena os elementos à 
    esquerda e à direita do pivô. Portanto, seu resultado
    pode ser diferente, desde que o pivô esteja na posição 
    correta.
    - não use sort() para resolver essa função, que tem 
    consumo de tempo O(n lg n). O consumo
    de tempo esperado para essa função é O(n) e o 
    de memória é O(1). 
    - O vídeo cujo link você encontra no enunciado dessa
    atividade ilustra uma possível solução.
    '''
    indice_fim = len(seq)-1
    indice_inicio = 0
    pivo = seq[indice_fim]
    for j in range(indice_inicio, indice_fim):
        if seq[j] <= pivo:
            seq[j],seq[indice_inicio] = seq[indice_inicio], seq[j]
            indice_inicio += 1
    seq[indice_inicio], seq[indice_fim] = seq[indice_fim], seq[indice_inicio]
    
    return indice_inicio
    
    
    ##vou fazer funcionar esse ainda...
    ## tem casos que dá errado quando o pivo é o maior elemento.
    
    # indice_pivo = len(seq)-1
    # pivo = seq[indice_pivo]
    # indice_maior = 0
    # indice_menor = indice_pivo - 1
    
    # while indice_maior < indice_menor:
    #     if seq[indice_maior] > pivo:
    #         while seq[indice_menor] > pivo and indice_maior <= indice_menor:
    #             indice_menor -= 1
    #         if seq[indice_menor] < pivo and indice_maior < indice_menor:
    #             seq[indice_menor], seq[indice_maior] = seq[indice_maior], seq[indice_menor]
    #         else:
    #             seq[indice_maior], seq[indice_pivo] = seq[indice_pivo], seq[indice_maior]
    #             return indice_maior
                
    #     indice_maior += 1
        
    # seq[indice_maior], seq[indice_pivo] = seq[indice_pivo], seq[indice_maior]   
    
            
    # return indice_maior
        
            
        


#-----------------------------------------------        
if __name__ == '__main__':
    main()
