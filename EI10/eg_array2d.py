# -*- coding: utf-8 -*-
"""eg_array2d-ei10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16iFELAfAAOsT5oLtSaIzkrxxZm0NPQIh
"""

# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''
    GRUPO: 7

    Nome: Brenno Pereira Machado
    NUSP: 6434401

    Nome: Augusto Lima Jardim
    NUSP: 11810918

    Nome: Ygor Peniche Maldonado
    NUSP: 10271558


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
    ''' função main() para teste da classe Array2d
    '''

    print("Testes da classe Array2d\n")

    # beginfora
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()

    b = a.reshape( (2,3) )   
    print(f'teste 2: reshape cria uma vista')
    print(b)
    print()

    print(f'teste 3: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(a)
    print(b)
    print()

    print(f'teste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1 
    print(a)
    print(b)
    print()

    print(f'teste 5: copy cria um clone')
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    c = a.copy()
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print(f'teste 6: mudanças em objeto um não devem refletir no outro')
    a[0,1] = 99
    c[0,5] = -1
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print("\n##Testes EG##")
    print("CARREGUE")

    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'a:\n{a}\n')

    a.carregue( lista )
    print(f'a:\n{a}\n')

    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')

    
    print("\nCARREGUE2")
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'a:\n{a}\n')

    a.carregue2( lista )
    print(f'a:\n{a}\n')

    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')

    print("\n## FlipV ##")
    lista = [1,2,3,4,5,6,7,8,9,0]
    a = Array2d( (5,2), 0)
    a.carregue( lista )
    print(f'a:\n{a}\n')

    flip = a.flipV()
    print(f'flip:\n{flip}\n')

    print(f'a:\n{a}\n')

    print("\n## FlipH ##")
    lista = [1,2,3,4,5,6,7,8,9,0]
    a = Array2d( (2,5), 0)
    a.carregue( lista )
    print(f'a:\n{a}\n')

    flipH(a)
    print(f'a:\n{a}\n')



## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

def flipH(array):
    nova_data = []
    i = 1
    j = 0
    while i <= array.shape[0]:
        while j < array.shape[1]:
            nova_data.append(array.data[array.shape[1] * i -1 - j])
            j += 1
        i += 1
        j = 0        
    array.data = nova_data


class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
         
        self.shape = shape
        self.size = shape[0]*shape[1]
        self.data = self.size*[val]

    # ---------------------------------------------------------------
    def copy(self):
        ''' (Array2d) -> Array2d
        Constrói e retorna um objeto do tipo Array2d com os atributos iguais ao 
        da referência 'self'.
        '''

        copia = Array2d(self.shape, 0)
        copia.data = self.data[:]
        return copia

    # ---------------------------------------------------------------
    def reshape(self, key):
        ''' (Array2d, tuple) -> Array2d
        Constrói e retorna um objeto do tipo Array2d, que utiliza o mesmo objeto/referência 
        list do atributo 'self.data'.
        '''
        
        view = Array2d(key, 0)
        view.data = self.data
        return view

    def carregue(self, nova_lista):
      '''(Array2d, list) -> none
      '''
      if self.size == len(nova_lista):
        self.data = nova_lista

    def carregue2(self, nova_lista):
      '''(Array2d, list) -> none
      '''
      if self.size == len(nova_lista):
        self.data = nova_lista[:]

    def flipV(self):
        nova_data = []
        i = 1
        j = 0
        while i <= self.shape[0]:
            while j < self.shape[1]:
                nova_data.append(self.data[i * (-1) * self.shape[1] + j])
                j += 1
            i += 1
            j = 0
        
        flip = Array2d((self.shape), 0)
        flip.carregue(nova_data)
        
        return flip


    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''

        lin, col = key
        return self.data[ self.shape[1]*lin + col]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''

        lin, col = key
        self.data[ self.shape[1]*lin + col] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> str
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        i = 0
        array = ""
        for elemento in self.data:
            i += 1
            array += str(elemento) + " "
            if i == self.shape[1]:
                array = array[:-1] + "\n"
                i = 0

        return array[:-1]

    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar

def teste_dados():

    print("Testes da classe Array2d\n")

    a = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    b = Array2d( (2,3), 1.7)   # criar Array2d com valor inicial 7
    print(f'teste 2: Criação do Array2d b:')
    print(b)
    print(f'shape: {b.shape}')
    print(f'size : {b.size}')
    print(f'data : {b.data}')
    print()

    print(f'teste 3: a[0,1] + 100 é: {a[0,1] + 100}') # acesso direto usando tupla: use o método __getitem__
    print()

    a[1,1] = -1    # atribuição usando tupla: use o método __setitem__
    print(f'teste 4: Array2d a:')
    print(a)

def teste_copy():
    A = Array2d((2,3),5)
    Copy_A = A.copy()
    print(f'Matriz A = \n{A}')
    print(f'Copy_A = \n{A.copy()}')
    print('Alterando A')
    print()
    print('A[0,0] = 2')
    print()
    A[0,0] = 2
    print(f'A = \n{A}')
    print(f'Copy_A = \n{Copy_A}')
    print()
    print('Alterando Copy_A')
    print()
    Copy_A[0,0] = 9
    print(' Copy_A[0,0] = 9')
    print(Copy_A)
    print()
    print(f'A = \n{A}')

def teste_reshape():
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(f'a = \n{a}')
    print()

    b = a.reshape( (2,3) )   
    print(f'teste 2: reshape cria uma vista')
    print('b = a.reshape((2,3))')
    print(f'b = \n{b}')
    
    print(f'teste 3: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(f'a = {a}')
    print(f'b = \n{b}')
    print()

    print(f'teste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1 
    print(f'a = {a}')
    print(f'b = \n{b}')
    print()


## ==================================================================

if __name__ == '__main__':
    main()
    #teste_dados()
    #teste_copy()
    #teste_reshape()