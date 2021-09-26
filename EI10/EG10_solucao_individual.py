# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''
    Nome: Brenno Pereira Machado
    NUSP: 6434401

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
    '''(Array2d) -> none
    Recebe um objeto classe Array2d e modifica os elementos 
    correspondentes as colunas desse invertendo-os horizontalmente
    Exemplo: 
        print(array)
        a b c
        d e f

        flipH(array)
        print(array)
        c b a
        f e d
    '''
    nlins, ncols = array.shape
    for lin in range(nlins):
        for col in range(ncols//2):
            key1 = lin, col
            key2 = lin, ncols-1-col
            array[key1], array[key2] = array[key2], array[key1]
    
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
        Constrói e retorna um objeto do tipo Array2d, que utiliza o mesmo 
        objeto/referência list do atributo 'self.data'.
        '''
        
        view = Array2d(key, 0)
        view.data = self.data
        return view

    def carregue(self, nova_lista):
        '''(Array2d, list) -> none
        Recebe uma referência 'self' da classe Array2d e uma nova_lista do 
        tipo list com mesmo tamanho de self.size e atribui a referência de 
        'nova_lista' para 'self.data'.
        '''

        if self.size == len(nova_lista):
            self.data = nova_lista

    def carregue2(self, nova_lista):
        '''(Array2d, list) -> none
        Recebe uma referência 'self' da classe Array2d e uma nova_lista do 
        tipo list com mesmo tamanho de self.size e atribui à self.data uma
        cópia de 'nova_lista'.
        '''
        
        if self.size == len(nova_lista):
            self.data = nova_lista[:]

    def flipV(self):
        ''' (Array2d) -> Array2d
        Recebe uma referência 'self' da classe Array2d e retorna um novo
        objeto da classe Array2d com os elementos correspondentes as linhas
        de 'self' invertidos verticalmente.
        Exemplo: 
            print(a)
            a b
            c d

            print(a.flipV())
            c d
            a b
        '''

        novo = Array2d(self.shape, None)
        nlins, ncols = self.shape
        for lin in range(nlins):
            for col in range(ncols):
                novo[nlins - 1 - lin, col] = self[lin, col]
        return novo


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


## ==================================================================

if __name__ == '__main__':
    main()