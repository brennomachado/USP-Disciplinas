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
    '''
    import numpy as np
    
    # testes individuais
    listas = []
    listas.append([5, 7, 4, 3, 8, 6])
    listas.append([6, 7, 5, 3, 8, 4])
    listas.append([1])
    listas.append([6])
    listas.append([-3])
    listas.append([0])
    listas.append([47, 0, 10, 7, 10, 26, 10])
    listas.append([-20, 24, 3, -8, 28, -18, 65, 81])
    listas.append([47, 18, 10, 96, 92, 48, -8])
    listas.append([11, 3, 37, 6, 71, 74, 33, -2])
    listas.append([90, 69, 0, 94, 32, -1, 50, -12])
    listas.append([-10, 77, 83, -9, 17, 36, 58, -13])
    
    
    # testes com listas aleatorias com tamanhos par e impar
    for i in range(11):
        listas.append(list(np.random.randint(low = -10,high=50,size=i%2+10)))
    
    # variaveis para checagem dos testes
    pivos_diferentes = 0
    testes_errados = 0
    
    i=0
    for lista in listas:
        print(f"## Teste: {i+1}")
        print(f"  Lista antes da pivotação:   {lista}")
        lista2 = lista[:]
        pivo2 = pivote_seq_2(lista2)
        pivo = pivote_seq(lista)
        print(f"  Lista depois da pivotação:  {lista}")
        print(f"  Alg. alternativo checagem:  {lista2}")
        print(f"  Pivo:  {pivo} - Pivo da checagem: {pivo2}")
        if (pivo == pivo2): print("  Pivos iguais")
        else:
            print("  Pivos DIFERENTES")
            pivos_diferentes += 1
            
        if (verifica_seq(lista,pivo) == 0): print("  Lista CERTA")
        else:
            print("  Lista ERRADA")
            testes_errados += 1  
        print("")
        i += 1
        
    print(f"Pivos diferentes: {pivos_diferentes}")
    print(f"Testes errados: {testes_errados}")

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
    i_pivo = len(seq) - 1
    i_maior = 0
    i_menor = i_pivo - 1
    pivo = seq[i_pivo]
    
    while i_maior <= i_menor:
        if seq[i_maior] >= pivo:
            while seq[i_menor] >= pivo and i_menor > -1:
                i_menor -= 1
            if i_menor > i_maior and seq[i_menor] < pivo:
                seq[i_menor], seq[i_maior] = seq[i_maior], seq[i_menor]
                i_menor -= 1
        if i_menor >= i_maior:
            i_maior += 1 
        
    seq[i_pivo], seq[i_maior] = seq[i_maior], seq[i_pivo]
    
    return i_maior
     
           
## Algoritmo visto na fonte externa citada, para comparação     
def pivote_seq_2(seq): 
    indice_fim = len(seq)-1
    indice_inicio = 0
    pivo = seq[indice_fim]
    for j in range(indice_inicio, indice_fim):
        if seq[j] <= pivo:
            seq[j],seq[indice_inicio] = seq[indice_inicio], seq[j]
            indice_inicio += 1
    seq[indice_inicio], seq[indice_fim] = seq[indice_fim], seq[indice_inicio]
    
    return indice_inicio
            
def verifica_seq(seq, pivo):
    status = 0
    
    for i in range(pivo + 1, len(seq)):
        if seq[i] < seq[pivo]:
            status = -1
            break
        
    #verifica lista inferior
    for i in range(pivo -1, -1, -1):
        if seq[i] > seq[pivo]:

            status = -1
            break

    return status

#-----------------------------------------------        
if __name__ == '__main__':
    main()
