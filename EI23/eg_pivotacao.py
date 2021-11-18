# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''
    EG
    
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
    
    listas = []
    listas.append([7, 11, 56, 5, 7, 99, 104])
    listas.append([7, 11, 56, 5, 7, 99, 10])
    listas.append([7, 11, 56, 5, 7, 99, -10])
    listas.append([99, 99, 99, 7, 11, 56, 5, 7, 13, -10, -10])
    listas.append([99, 99, 99, 7, 11, 56, 5, 7, 6, -10, -10])
    
    testes = [(0,7), (0,7), (0,7), (3,9), (3,9)]
    
    for i in range(len(listas)):
      print(f"TESTE pivote: {i+1}")
      print(f"entradas: {testes[i][0]},{testes[i][1]}")
      print(f"  Lista antes da pivotação:  {listas[i]}")
      m = pivote(listas[i], testes[i][0],testes[i][1])
      print(f"  Lista depois da pivotação: {listas[i]}")
      print(f"  Pivo: {m}\n")
      
    print("##############")
    print("TESTES ordene_por_pivotacaoR")
    
    seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1, 22]
    print(f"  Seq:                               {seq}")
    m = pivote(seq, 0, 12) # divide
    print(f"  pivote(seq, 0, 12):                {seq}")
    print(f"  Pivo: {m}")
    ordene_por_pivotacaoR(seq, 0, 7)
    print(f"  ordene_por_pivotacaoR(seq, 0, 7):  {seq}")
    ordene_por_pivotacaoR(seq, 8, 12)
    print(f"  ordene_por_pivotacaoR(seq, 8, 12): {seq}\n")
    
    seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1, 0]
    print(f"  Seq:                               {seq}")
    m = pivote(seq, 0, 12) # divide
    print(f"  pivote(seq, 0, 12):                {seq}")
    print(f"  Pivo: {m}")
    ordene_por_pivotacaoR(seq, 3, 12)
    print(f"  ordene_por_pivotacaoR(seq, 3, 12): {seq}\n")
    
    seq = [99, 99, 17, -1, 7, 11, 56, 5, 7, 9, -10, -10]
    print(f"  Seq:                               {seq}")
    ordene_por_pivotacaoR(seq, 2, 10)
    print(f"  ordene_por_pivotacaoR(seq, 2, 10): {seq}\n")
               
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

def pivote(seq, e, d):
    ''' (list) -> int

      RECEBE uma lista seq e dois inteiros e < d. Chamaremos
          de pivô o elemento na posição seq[d-1].
      REARRANJA os elementos de seq de tal forma que para algum
          índice m, e <= m < d tenhamos
          * seq[m] == pivô e
          * seq[e: m] <= pivô < seq[m+1: d].
      RETORNA o índice m.
      '''
    i_pivo = d - 1
    i_maior = e
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

def ordene_por_pivotacaoR(seq, e, d): # EG: DESAFIO
    '''(list, int, int) -> None
    RECEBE uma lista seq e um par de índice e <= d.
    REARRANJA os elementos de seq[e: d] para que fiquem em ordem crescente.
    '''
    
    if e < d-1:
      m = pivote(seq, e, d)
      ordene_por_pivotacaoR(seq, e, m)
      ordene_por_pivotacaoR(seq, m+1, d)


## ------------------------------------------------------------------
## FUNÇÕES PRONTAS DO EG

def ordene_por_pivotacao(seq):
    '''(list) -> None
    RECEBE uma lista seq.
    REARRANJA os elementos de seq para que fiquem em ordem crescente.

    NOTA: É um invólucro para ordene_por_pivotacaoR().

    EXEMPLOS

    In [2]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [3]: ordene_por_pivotacao(seq)
    In [4]: seq
    Out[4]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

    In [11]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
    In [12]: ordene_por_pivotacao(seq)
    In [13]: seq
    Out[13]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']
    '''
    n = len(seq)
    ordene_por_pivotacaoR(seq, 0, n)
## ------------------------------------------------------------------
def ordene_por_pivotacaoI(seq):
    '''(list) -> None
    RECEBE uma lista seq.
    REARRANJA os elementos de seq para que fiquem em ordem crescente.

    É uma função ITERATIVA que se APOIA na função pivote(seq, e, d).
    Para entender o seu funcionamente pode ser útil ver as animações
    e exemplos na página do EG.

    EXEMPLOS

    In [34]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [35]: ordene_por_pivotacaoI(seq)
    In [36]: seq
    Out[36]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

    In [37]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
    In [38]: ordene_por_pivotacaoI(seq)
    In [39]: seq
    Out[39]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']
    '''
    n = len(seq)
    e = 0
    d = n
    pilha = []
    pilha.append((e, d))
    while pilha != []:
        e, d = pilha.pop()
        if e < d-1: # seq[e: d]) tem pelo menos dois elementos
            m = pivote(seq, e, d)
            # empilhe par de índices da fatia esquerda
            pilha.append((e, m))
            # empilhe par de índice da fatia direita
            pilha.append((m+1, d))
## ------------------------------------------------------------------
def ordene_por_insercao(seq):
    ''' (list) -> None

    RECEBE uma lista seq.
    REARRANJA os elementos da lista de tal forma que fiquem em
        ordem crescente.

    Esta função se apoio na função insira_ultimo.
    '''
    n= len(seq)
    for fim in range(2, n+1):
        insira_ultimo(seq, fim)
## ------------------------------------------------------------------
def insira_ultimo(seq, n):
    ''' (list, int) -> None

    RECEBE uma lista seq e um inteiro n tais que os elementos da
         sublista seq[0:n-1] estão em ordem crescente.
    REARRANJA os elementos da lista seq de tal forma que os
         elementos da sublista seq[0:n] estejam em ordem crescente.

    Essa função é o coração do algoritmo de ordenação
    por inserção.
    '''
    i = n-1
    while i > 0 and seq[i] < seq[i-1]:
        seq[i], seq[i-1] = seq[i-1], seq[i]
        i -= 1
#-----------------------------------------------        
if __name__ == '__main__':
    main()
