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
    ''' Unidade de teste da classe MaxHeap '''
    print("Testes do EG24 - ordenação usando max heap")

    x = [21, 12, 43, 61, 41, 71, 91, 31, 81]
    # x = [13, 12, 43, 61, 41, 71, 91, 31, 60]
    print(f"Entrada:\n{x}")

    # print("\n testes do MaxHeap.insira()")
    # h = MaxHeap()
    # for item in x:
    #     h.insira(item)
    #     print(h)
    #     input("Tecle enter para continuar ...")

    print("\n teste do construa")
    h = MaxHeap()
    h.construa(x)
    print(h)

    #------------------------------------------
    print("\n teste do MaxHeap.remova()")
    print(h)
    while not h.vazio():
        print(f"removi {h.remova()}")
        print(h)
        input("Tecle enter para continuar ...")
    
    #------------------------------------------
    print("\n testes do heapsort")
    x = [21, 12, 43, 61, 41, 71, 91, 31, 81]
    print(f"x  antes: {x}")
    heapsort(x)
    print(f"x depois: {x}")

    y = ['aa', 'c', 'e', 'aa', 'z', 'a-b', 'ef', 'b', 'a', 'cz']
    print(f"y  antes: {y}")
    heapsort(y)
    print(f"y depois: {y}")
    
## ==================================================================
def heapsort(seq):
    '''(list) -> None
    RECEBE uma lista seq.
    REARRANJA os elementos de seq de tal forma que fiquem em ordem
        crescente.
    Usa a classe MaxHeap. Adaptação mutadora de heapsort() em
    https://docs.python.org/3/library/heapq.html

    EXEMPLOS

    In [2]: x = [21, 12, 43, 61, 41, 71, 91, 31, 81]
    In [3]: heapsort(x)
    In [4]: x
    Out[4]: [12, 21, 31, 41, 43, 61, 71, 81, 91]

    In [5]: y = ['aa', 'c', 'e', 'aa', 'z', 'a-b', 'ef', 'b', 'a', 'cz']
    In [6]: heapsort(y)
    In [7]: y
    Out[7]: ['a', 'a-b', 'aa', 'aa', 'b', 'c', 'cz', 'e', 'ef', 'z']
    '''
    n = len(seq)
    # pré-processamento: crie um MaxHeap com elementos de seq 
    h = MaxHeap()
    for item in seq: h.insira(item)
    
    # ordenação por seleção
    for i in range(n-1, -1, -1):
        # maior vai para o final
        seq[i] = h.remova() 

## ==================================================================

class MaxHeap:
    #-----------------------------------------------------
    def __init__(self):
        '''(MaxHeap) -> None
        CONSTRUTOR da classe MaxHeap.
        CRIA uma lista self.data com [None] que representa 
             um MaxHeap vazio.

        Os itens do MaxHeap serão armazenados em
        self.data[1], self.data[2], ... , self.data[n-1]

        PERIGO. o elemento na posição de índice zero não 
            faz parte do MaxHeap. O primeiro elemento 
            está na posição de índice 1.
        '''
        self.data = [None]

    #-----------------------------------------------------        
    def __len__(self):
        ''' (MaxHeap) -> int
        RECEBE um MaxHeap self.
        RETORNA o número de elementos no MaxHeap self.

        EXEMPLOS

        In [12]: h = MaxHeap()
        In [13]: len(h)
        Out[13]: 0

        In [15]: h.insira(7)
        In [16]: h.insira(3)
        In [17]: h.insira(9)
        In [18]: print(h)
        9	
        3	7	
        In [19]: len(h)
        Out[19]: 3
        '''
        return len(self.data) - 1

    #-----------------------------------------------------        
    def vazio(self):
        ''' (MaxHeap) -> bool
            RECEBE um MaxHeap self.
            RETORNA True se o MaxHeap está vazio e False em caso 
                contrário.
            
            EXEMPLOS

            In [12]: h = MaxHeap()
            In [13]: len(h)
            Out[13]: 0
            In [14]: h.vazio()
            Out[14]: True

            In [15]: h.insira(7)
            In [16]: h.insira(3)
            In [17]: h.insira(9)
            In [19]: len(h)
            Out[19]: 3

            In [20]: h.vazio()
            Out[20]: False
        '''
        return len(self) == 0 # equivalente a len(self.data) == 1
  
    #-----------------------------------------------------        
    def maxheap(self):
        ''' (MaxHeap) -> bool
            RECEBE um MaxHeap self.
            RETORNA True se self.data representa um max-heap e False 
                em caso contrário.

            EXEMPLOS                

            In [21]: h  = MaxHeap()
            In [22]: h.maxheap()
            Out[22]: True

            In [23]: h.data = [None, 1, 2, 3]
            In [24]: h.maxheap()
            Out[24]: False

            In [25]: h.data = [3, 1, 2]
            In [26]: h.maxheap()
            Out[26]: False

            In [27]: h.data = [None, 3, 1, 2]
            In [28]: h.maxheap()
            Out[28]: True
        '''
        # apelidos 
        n = len(self.data)
        dt = self.data
        # deve ter pelo menos None
        if n == 0: return False
        # primeira posição deve ser None
        if dt[0] != None: return False
        # verifique se satisfaz a propriedade/invarinte de max-heap
        for filha in range(2, n):
            mae = filha // 2
            # mãe deve ser maior ou igual a filha
            if dt[mae] < dt[filha]: return False
        return True
    
    #-----------------------------------------------------
    def __str__(self):
        ''' (MaxHeap) -> str
        RECEBE um MaxHeap self.
        RETORNA uma string usada para exibir o MaxHeap.
        Método usado pelas funções print() e str().
        '''
        # apelidos 
        n = len(self.data)
        dt = self.data
        # construa a string txt que representa o MaxHeap.
        txt = '\n'
        nivel = 0
        # pecorra o MaxHeap
        i = 1 
        while i < n:
            fim = 2 ** nivel
            nivel += 1
            filho = 0
            while i < n and filho < fim:
                txt += f'{dt[i]}\t'
                i += 1
                filho += 1
            txt += '\n'
        return txt

    #-----------------------------------------------------
    def insira(self, item):
        ''' (MaxHeap, obj) -> None
            Recebe um objeto item e o insere no heap.

            Inicialmente, o item deve ser colocado no final da lista. 
            Em seguida, enquanto o pai desse item for menor, o item
            deve subir na árvore até sua posição correta. 

            Exemplo:
            Caso self.data seja a lista [None], a inserção de 21 deve
            rearranjar self.data para que se torne: [None, 21].

            Caso self.data seja a lista [None, 21], a inserção de 12 deve
            rearranjar self.data para que se torne: [None, 21, 12].
            
            Caso self.data seja a lista [None, 21, 12] a inserção de 43 
            deve rearranjar self.data para que se torne: [None, 43, 12, 21].

            Caso self.data seja a lista [None, 43, 12, 21] a inserção de 65
            deve rearranjar self.data para que se torne: [None, 65, 43, 21, 12].

            Dica: desenhe as árvores binárias correspondentes.
        '''
        self.data.append(item)
        i_filho = len(self.data) -1
        i_pai = i_filho // 2
        
        while i_pai > 0:
            if self.data[i_pai] < self.data[i_filho]:
                self.data[i_pai], self.data[i_filho] = self.data[i_filho], self.data[i_pai]
                i_filho = i_pai
                i_pai = i_filho // 2
            else: i_pai = 0
    
    def construa(self, seq):
        ''' (MaxHeap, list) -> None
            Recebe uma lista de números seq. 
            Para cada item em seq, insere o item no heap
            usando o método insira. Dessa forma, seq é
            transformada em um max heap em self.data.
        '''
        for item in seq:
            self.insira(item)

    #-----------------------------------------------------
    def remova(self):                                 # EG
        '''(MaxHeap) -> obj
            RECEBE um MaxHeap self.
            RETORNA e REMOVE o maior item do MaxHeap. 

            EXEMPLOS

            In [2]: h = MaxHeap()
            In [3]: seq = [1, 4, 5, 3, 6]
            In [4]: h.construa(seq)
            In [5]: seq
            Out[5]: [1, 4, 5, 3, 6]
            In [6]: h.data
            Out[6]: [None, 6, 5, 4, 1, 3]

            In [7]: h.remova()
            Out[7]: 6
            In [8]: h.data
            Out[8]: [None, 5, 3, 4, 1]

            In [9]: h.remova()
            Out[9]: 5
            In [10]: h.data
            Out[10]: [None, 4, 3, 1]

            In [11]: h.remova()
            Out[11]: 4
            In [12]: h.data
            Out[12]: [None, 3, 1]

            In [13]: h.remova()
            Out[13]: 3
            In [14]: h.data
            Out[14]: [None, 1]

            In [15]: h.remova()
            Out[15]: 1
            In [16]: h.data
            Out[16]: [None]

            In [17]: h.remova()
            MaxHeap ERRO: tentativa de remoção em max-heap vazio
        '''
        # crie apelidos
        n = len(self.data) # 1 a mais que o número de itens no MaxHeap
        dt = self.data     # itens: dt[1], dt[2],...,dt[n-1]
        # MaxHeap vazio: erro
        if n == 1:
            print("MaxHeap ERRO: tentativa de remoção em max-heap vazio")
            return None
        else:
            
            if n > 2:
                # self.maxheapfy(1) #Se existir algum dt que não for maxheap usar isso antes
                removido = dt[1]
                dt[1] = dt.pop()
                self.maxheapfy(1)
                ## Não precisou usar o método maxheap() dado
                # if self.maxheap():
                #     removido = dt[1]
                #     dt[1] = dt.pop()
                #     self.maxheapfy(1)
                # else:
                #     self.maxheapfy(1)
                #     removido = dt[1]
                #     dt[1] = dt.pop()
                #     self.maxheapfy(1)
            else:
                removido = dt.pop()
         
        return removido
                       
    def maxheapfy(self, pai):
        e,d = self.verifica_pai(pai)
        
        if e != -1 and d != -1:
            filho_e = self.filho_e(pai)
            filho_d = self.filho_d(pai)
            if e or d:
                if self.data[filho_e] > self.data[filho_d]:
                    self.troca(pai, filho_e)
                    self.maxheapfy(filho_e)
                else:
                    self.troca(pai, filho_d)
                    self.maxheapfy(filho_d)
        elif e != -1:
            filho_e = self.filho_e(pai)
            if e:
                self.troca(pai, filho_e)
                self.maxheapfy(filho_e)
        
    def filho_e(self, pai):
        return pai*2
    
    def filho_d(self, pai):
        return pai*2 + 1

    def troca(self, pos1, pos2):
        self.data[pos1], self.data[pos2] = self.data[pos2], self.data[pos1]
    
    def verifica_pai(self, i_pai):
        """ Return (e,d)
                Se filho_e não existe e = -1
                Se filgo_d não existe d = -1
                
                Se filho_e é maior que pai => = 1,
                    se é menor => e = 0
                Se filho_d é maior que pai => d = 1,
                    se é menor => d = 0
        """
        #indices
        i_filho_e = 2*i_pai
        i_filho_d = 2*i_pai +1
        n = len(self.data) -1
        
        if i_filho_d <= n:
            if self.data[i_filho_d] < self.data[i_pai]:
                d = 0
            else: d = 1
            
            if self.data[i_filho_e] < self.data[i_pai]:
                e = 0
            else: e = 1
        else:
            d = - 1
            if i_filho_e <= n:
                if self.data[i_filho_e] < self.data[i_pai]:
                    e = 0
                else: e = 1
            else: e = - 1
            
        return (e,d)
        
                
        # escreva sua solução

        
if __name__ == '__main__':
    main()

#---------------------------------------------------------
#
#  PARA EXPERIMENTOS
#
#---------------------------------------------------------

#---------------------------------------------------------
def quicksortI(v):
    '''(list, int, int) -> None
    RECEBE uma lista v.
    REARRANJA os itens de v para que fiquem em ordem crescente.
    É um implementação do algoritmo quicksort, versão iterativa
    '''
    n = len(v)
    e = 0
    d = n
    pilha = []
    pilha.append([e, d])
    while pilha != []:
        e, d = pilha.pop()
        if e < d-1:
            m = separe(v, e, d)
            # empilhe fatia esquerda
            pilha.append([e, m])
            # empilhe fatia direita
            pilha.append([m+1, d])

#---------------------------------------------------------
def separe(v, e, d):
    '''(list, int, int) -> int
    RECEBE uma lista v e inteiros e e d.
    REARRANJA os itens de `v[e: d]` e RETORNA um 
    índice m tal que v[e:m] <= v[m] < v[m+1:r].
    '''
    x = v[d-1] # pivo
    i = e-1
    for j in range(e, d): 
        if v[j] <= x:
            i += 1
            v[i], v[j] = v[j], v[i]
    return i
