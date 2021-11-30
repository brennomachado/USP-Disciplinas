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

#------------------------------------------------------
def main():
    '''
        Testes para os algoritmos de LCS

        Inclua ao menos 10 testes distintos para sua função subseq().
    '''
    
    print("Exemplos de execuções de lcs_rec() e lcs_iterPD()")
    # t = 'BDCABA'
    # s = 'ABCBDAB'
    s = 'tctgggaatgcggtctcgcttagctgcggggacgacgagcagtgaacgacgcttcccacgc'
    t = 'ttatggctcactaccacggccaaagaggtagagcacattttctacccaggctgaggtgtcctcttaccttt'
    m, n = len(s), len(t)
    memo = np.full((m+1,n+1), 0)
    lcsPD(s, m, t, n, memo)
    print(memo)
    print(monte_lcs(s, t, memo))
    
    print("----------------------------------")

    
#----------------------------------------------
def subseq (s, t): # DO EI26
    ''' (str, str) -> bool 
        RECEBE strings s e t.
        RETORNA True se s é subsequência de t.
    '''
    tam_s = len(s)
    tam_t = len(t)
    
    indice_s = 0
    indice_t = 0
    while indice_s < tam_s and indice_t < tam_t:
        achei_em_t = False
        while indice_t < tam_t:
            if s[indice_s] == t[indice_t]:
                indice_t+=1
                achei_em_t = True
                break
            indice_t+=1
        if not achei_em_t: return False
        indice_s+=1
        
    if indice_s == tam_s: return True
    return False 

#----------------------------------------------------------------
# LCS RECURSIVA 
#----------------------------------------------------------------    
def lcs_rec(s, t):
    '''(str, str) -> str
        INTERFACE para a função recursiva lcsR().

        EXEMPLOS

        In [17]: s = 'BDCABA'
        In [18]: t = 'ABCBDAB'
        In [19]: lcs_rec(s, t)
        Out[19]: 'BCBA'

        In [20]: s = 'ABRACADABRA'
        In [21]: t = 'YABBADABBADOO'
        In [22]: lcs_rec(s, t)
        Out[22]: 'ABADABA'
    '''
    m = len(s)
    n = len(t)
    return lcsR(s, m, t, n)

#----------------------------------------------
def lcsR(s, m, t, n):
    '''(str, int, str, int) -> str
        RECEBE uma string s, um inteiro m, uma string t e um inteiro n.
        RETORNA uma LCS de s[0:m] e t[0:n].

        EXEMPLOS

        In [23]: s = 'BDCABA'
        In [24]: t = 'ABCBDAB'
        In [25]: lcsR(s, 4, t, 5)
        Out[25]: 'BC'

        In [26]: s = 'ABRACADABRA'
        In [27]: t = 'YABBADABBADOO'
        In [28]: lcsR(s, 9, t, 7)
        Out[28]: 'ABADA'
    '''
    # BASE
    if m == 0 or n == 0: return ""

    # REDUZ 
    if s[m-1] == t[n-1]:
        return lcsR(s, m-1, t, n-1) + s[m-1]
    
    # REDUZ
    lcs_1 = lcsR(s, m-1, t,   n)
    lcs_2 = lcsR(s,   m, t, n-1)

    # COMBINA
    if len(lcs_1) > len(lcs_2): return lcs_1
    return lcs_2


#----------------------------------------------------------------
# LCS ITERATIVA com MEMÓRIA
#----------------------------------------------------------------    
def lcs_iterPD(s, t):
    '''(str, str) -> str
        INTERFACE para a função recursiva lcsPD() e monte_lcs().
        RETORNA uma LCS de s e t.

        EXEMPLOS

        In [42]: s = 'BDCABA'
        In [43]: t = 'ABCBDAB'
        In [44]: lcs_iterPD(s, t)
        Out[44]: 'BDAB'

        In [45]: s = 'ABRACADABRA'
        In [46]: t = 'ABCBDAB'
        In [47]: lcs_iterPD(s, t)
        Out[47]: 'ABCDAB'
    '''
    m = len(s)
    n = len(t)
    
    #------------------------------------------------
    # memo é o array rascunho em que para todo par (i,j)
    # com 0 <= i <= m e 0 <= j <= n tem-se que memo[i, j] 
    # é o comprimento de uma LCS de s[0:i] e t[0:j]
    memo = np.full((m+1, n+1), 0)
    
    # lcsPD(s, m, t, n, memo) preenche o array memo
    lcsPD(s, m, t, n, memo)
    
    return monte_lcs(s, t, memo) 
    
#----------------------------------------------
def lcsPD(s, m, t, n, memo):
    '''(str, int, str, int) -> None
        RECEBE uma string s, um inteiro m, uma string t, um inteiro n 
            e um array memo.
        PREENCHE o array memo de tal forma que para todo 
        par (i,j),  com 0 <= i <= m e 0 <= j <= n, tenhamos que 
        memo[i,j] é o comprimento de uma LCS de s[0:i] e t[0:j]

        VERSÃO ITERATIVA que nas redes sociais recebe o adjetivo sexy #??????
            de bottom-up, ou de baixo para cima.

        EXEMPLO

        In [6]: s = 'BDCABA'
        In [7]: t = 'ABCBDAB'
        In [8]: m, n = len(s), len(t)
        In [9]: memo = np.full((m+1,n+1), 0)
        In [10]: lcsPD(s, m, t, n, memo)
        Out[10]: 4
        In [11]: memo
        Out[11]: 
        array([[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 2, 2, 2],
            [0, 0, 1, 2, 2, 2, 2, 2],
            [0, 1, 1, 2, 2, 2, 3, 3],
            [0, 1, 2, 2, 3, 3, 3, 4],
            [0, 1, 2, 2, 3, 3, 4, 4]])

        In [12]: monte_lcs(s, t, memo)
        Out[12]: 'BDAB'
    '''
    limite_m = len(s)+1
    limite_n = len(t)+1
    
    for i in range(1, limite_m):
        for j in range(1, limite_n):
                if s[i-1] == t[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                elif memo[i][j-1] >= memo[i-1][j]:
                    memo[i][j] = memo[i][j-1]
                else: 
                    memo[i][j] = memo[i-1][j]
                     
#---------------------------------------------------------
# FUNÇÃO AUXILIAR
#---------------------------------------------------------
def monte_lcs(s, t, memo):
    '''(str, str, array) -> str
        RECEBE uma string s, uma string t e um array memo tal que 
            para todo i = 0,1,...,len(s) e j = 0,1,...,lent(t)
            memo[i,j] é comprimento de uma LCS de s[0:i] e t[0:j] 
        RETORNA uma LCS de s e t.
    '''
    lcs = ''        
    m, n = len(s), len(t)
    i, j  = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs = s[i-1] + lcs
            i -= 1
            j -= 1
        elif memo[i-1, j] >= memo[i, j-1]:
            i -= 1
        else:
            j -= 1
    return lcs
    
#----------------------------------------------------
if __name__ == "__main__":
    main()
    
