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
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    print("Teste INTERCALE 01")
    seq = [99, 99, 99, 99, 7, 11, 56, 5, 7, 59, -1]
    print(f"   Lista antes da  intercalação: {seq}")
    intercale(seq, 4, 7, 10)
    print(f"   Lista depois da intervalação: {seq}\n")
    
    print("Teste INTERCALE 02")
    seq = [0, 1, 2, 3, 7, 11, 56, 5, 7, 99, 104]
    print(f"   Lista antes da  intercalação: {seq}")
    intercale(seq, 4, 7, 11)
    print(f"   Lista depois da intervalação: {seq}\n")
    
    print("Teste INTERCALE 03")
    seq = [7, 11, 56, 5, 7, 99, -1]
    print(f"   Lista antes da  intercalação: {seq}")
    intercale(seq, 1, 3, 6)
    print(f"   Lista depois da intervalação: {seq}\n")
    
    print("Teste INTERCALE 04")
    seq = [7, 11, 56, 5, 7, 99, 104]
    print(f"   Lista antes da  intercalação: {seq}")
    intercale( seq, 0, 3, 7)
    print(f"   Lista depois da intervalação: {seq}\n")
    print("")
    
    print("###################################")
    print("TESTES do ORDENE_POR_INTERCALAÇÃO_R\n")
    
    print("Teste 01 - ORDENE_POR_INTERCALAÇÃO_R01")
    seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    print(f"   Lista antes da  intercalação: {seq}")
    ordene_por_intercalacaoR(seq, 0, 5)
    print(f"   ordene_por_intercalacaoR(seq, 0, 5)")
    print(f"   Lista depois da intervalação: {seq}")
    ordene_por_intercalacaoR(seq, 5, 11)
    print(f"   ordene_por_intercalacaoR(seq, 5, 11)")
    print(f"   Lista depois da intervalação: {seq}\n")
    
    print("Teste 02 - ORDENE_POR_INTERCALAÇÃO_R01")
    seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    print(f"   Lista antes da  intercalação: {seq}")
    ordene_por_intercalacaoR(seq, 0, 6)
    print(f"   ordene_por_intercalacaoR(seq, 0, 6)")
    print(f"   Lista depois da intervalação: {seq}")
    ordene_por_intercalacaoR(seq, 6, 11)
    print(f"   ordene_por_intercalacaoR(seq, 6, 11)")
    print(f"   Lista depois da intervalação: {seq}\n")
    
    
    
    
    

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2): # EI
  ''' (list, list) -> list

      Recebe seq1 e seq2, duas listas tal que:

          - seq1 é crescente com n1 >= 0 elementos e
          - seq2 é crescente com n2 >= 0 elementos
          
      Retorna uma lista com n1+n2 elementos, contendo
      os elementos de seq1 e seq2 em ordem crescente.

      Exemplo para 
          seq1 = [7, 11, 56] e 
          seq2 = [-5, 7, 99, 104]
          
          
          seq1 = [-, -, -] e 
          seq2 = [-, -, 99, 104]
      
      a função deve retornar a lista:
          [-5, 7, 7, 11, 56, 99, 104]
  '''
  
  indice_seq1 = 0
  indice_seq2 = 0
  tamanho_seq1 = len(seq1)
  tamanho_seq2 = len(seq2)
  lista = []
  tamanho_nova_lista = tamanho_seq1+tamanho_seq2+1
  
  if tamanho_seq1 == 0 or tamanho_seq2 == 0:
      if tamanho_seq1 == 0:
          lista = seq2[:]
      else:
          lista = seq1[:]
      return lista
  
  for i in range(tamanho_nova_lista):
      if indice_seq1 >= tamanho_seq1:
          for j in range(indice_seq2, tamanho_seq2):
              lista.append(seq2[indice_seq2])
              indice_seq2 += 1
          i = tamanho_nova_lista
      elif indice_seq2 >= tamanho_seq2:
          for j in range(indice_seq1, tamanho_seq1):
              lista.append(seq1[indice_seq1])
              indice_seq1 += 1
          i = tamanho_nova_lista
      elif seq1[indice_seq1] <= seq2[indice_seq2]:
          lista.append(seq1[indice_seq1])
          indice_seq1 += 1
      else:
          lista.append(seq2[indice_seq2])
          indice_seq2 += 1
          
  return lista

## ------------------------------------------------------------------

def intercale(seq, e, m, d): # EG: DESAFIO
    ''' (list, int, int, int) -> None
      RECEBE uma lista seq e índices e, m e d tais que os elementos de
      
          - seq[e:m] estão em ordem crescente e
          - seq[m:d] estão em ordem crescente 
          
      REARRANJA os elementos de seq[e:d] para que fiquem em ordem crescente.

      SUGESTÃO: Em busca de inspiração? 
      Esta função é muito semelhante a função intercale_seqs(). 
      Alguns __possíveis__ passos...
        * CRIE uma lista auxiliar de tamanho n = d-e.
        * INTERCALE as sublistas seq[e:m] e seq[m:d] de seq[e:d] e armazene o resultado 
          desta intercalação na lista auxiliar.
        * COPIE o conteúdo da lista auxiliar para seq[e:d].
      
      EXEMPLOS
        In [2]: seq = [7, 11, 56, 5, 7, 99, 104]
        In [3]: intercale( seq, 0, 3, 7) # retorna None
        In [4]: seq
        Out[4]: [5, 7, 7, 11, 56, 99, 104]

        In [5]: seq = [7, 11, 56, 5, 7, 99, -1]
        In [6]: intercale(seq, 1, 3, 6) # seq[1:3] = [11, 56] e seq [3:6] = [5, 7, 99]
        In [7]: seq # seq[1:6] crescente
        Out[7]: [7, 5, 7, 11, 56, 99, -1]

        In [8]: seq = [0, 1, 2, 3, 7, 11, 56, 5, 7, 99, 104]
        In [9]: intercale(seq, 4, 7, 11) # seq[4:7] = [7, 11, 56] seq[7:11] = [5, 7, 99, 104] 
        In [10]: seq # seq[4:11] crescente
        Out[10]: [0, 1, 2, 3, 5, 7, 7, 11, 56, 99, 104]

        In [11]: seq = [99, 99, 99, 99, 7, 11, 56, 5, 7, 59, -1]
        In [12]: intercale(seq, 4, 7, 10) # seq[4:7] = [7, 11, 56] seq[7:10] = [5, 7, 99] 
        #In [12]: intercale(seq, 4, 7, 11) # seq[4:7] = [7, 11, 56] seq[7:10] = [5, 7, 99] - errado
        In [13]: seq # seq[4:10] crescente
        Out[13]: [99, 99, 99, 99, 5, 7, 7, 11, 56, 59, -1]
    '''
    lista_esq = seq[e:m]
    lista_dir = seq[m:d]
    tam_lista_esq = len(lista_esq)
    tam_lista_dir = len(lista_dir)
    indice_topo_esq, indice_topo_dir = 0, 0
    for k in range(e,d):
      if indice_topo_esq >= tam_lista_esq:
        seq[k] = lista_dir[indice_topo_dir]
        indice_topo_dir += 1
      elif indice_topo_dir >= tam_lista_dir:
        seq[k] = lista_esq[indice_topo_esq]
        indice_topo_esq += 1 
      elif lista_esq[indice_topo_esq] < lista_dir[indice_topo_dir]:
        seq[k] = lista_esq[indice_topo_esq]
        indice_topo_esq += 1 
      else:
        seq[k] = lista_dir[indice_topo_dir]
        indice_topo_dir += 1 


## ------------------------------------------------------------------

def ordene_por_intercalacao(seq): 
    '''(list) -> None
      RECEBE uma lista seq.
      REARRANJA os elementos de seq para que fiquem em ordem crescente.

      NOTA: É um invólucro para ordene_por_intercalacaoR().

      EXEMPLOS
        In [2]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
        In [3]: ordene_por_intercalacao(seq)
        In [4]: seq
        Out[4]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

        In [11]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
        In [12]: ordene_por_intercalacao(seq)
        In [13]: seq
        Out[13]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']
    ''' 
    n = len(seq)
    ordene_por_intercalacaoR(seq, 0, n)

## ------------------------------------------------------------------
    
def ordene_por_intercalacaoR(seq, e, d): # EG: DESAFIO
    '''(list, int, int) -> None
      RECEBE uma lista seq e índice e e d.
      REARRANJA os elementos de seq[e: d] para que fiquem em ordem crescente.

      Esta função deve ser RECURSIVA e deve se APOIAR na função intercale(seq, e, m, d).
      Busque inspiração na busca binária e nas animações na página do EG.

      EXEMPLOS
        In [46]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
        In [47]: ordene_por_intercalacaoR(seq, 0, 5)
        In [48]: seq
        Out[48]: [-1, 7, 17, 58, 99, 11, 56, 5, 7, 59, -1]
        In [49]: ordene_por_intercalacaoR(seq, 5, 11)
        In [50]: seq
        Out[50]: [-1, 7, 17, 58, 99, -1, 5, 7, 11, 56, 59]

        In [51]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
        In [52]: ordene_por_intercalacaoR(seq, 0, 6)
        In [53]: seq
        Out[53]: [-1, 7, 11, 17, 58, 99, 56, 5, 7, 59, -1]
        In [54]: ordene_por_intercalacaoR(seq, 6, 11)
        In [55]: seq
        Out[55]: [-1, 7, 11, 17, 58, 99, -1, 5, 7, 56, 59]
    '''
    if (d - e > 1):
      m = (e + d)//2
      ordene_por_intercalacaoR(seq, e, m)
      ordene_por_intercalacaoR(seq, m, d)
      intercale(seq, e, m, d)
    
## ------------------------------------------------------------------

def ordene_por_intercalacaoI(seq): 
    '''(list) -> None
    RECEBE uma lista seq.
    REARRANJA os elementos de seq para que fiquem em ordem crescente.
        
    É uma função ITERATIVA que se APOIA na função intercale(seq, e, m, d).
    Para entender o seu funcionamente pode ser útil ver as animações 
    e simulação na página do EG.

    EXEMPLOS

    In [34]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [35]: ordene_por_intercalacaoI(seq)
    In [36]: seq
    Out[36]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

    In [37]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
    In [38]: ordene_por_intercalacaoI(seq)
    In [39]: seq
    Out[39]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']
    '''
    n = len(seq)
    b = 1 # tamanho dos pares de blocos a serem intercalados
    while b < n:
        e = 0
        while e + b < n:
            d = e + 2*b
            if d > n: d = n
            intercale(seq, e, e+b, d)
            e = d
        b = 2*b # dobre o tamanho dos blocos

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
        
#--------------------------------------------
if __name__ == '__main__':
    main()
