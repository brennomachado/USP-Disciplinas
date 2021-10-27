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
    ''' função main() para teste da classe Array2d
    '''

    print("Testes da classe Array2d e comparação com Numpy\n")

    lista_a = [1, 2, 3, 4, 5, 6]
    lista_b = [0, 1, 1, 0, 0, 1]
    tam_a = len(lista_a)
    tam_b = len(lista_b)

    a = Array2d( (1, tam_a), 0) # cria Array2d com valor inicial 0
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()
    a.data = lista_a   ## ou a.carregue(lista_a) como no EG10
    a.resize( (2,3) )
    print(f'a:\n{a}\n')

    b = Array2d( (1, tam_b), 0)
    b.data = lista_b   # ou b.carregue(lista_b)
    b.resize( (3,2) )
    print(f'b:\n{b}\n')

    linha = a.getlin(0)
    print(f'linha a.getlin(0)\n{linha}\n')

    coluna = b.getcol(1)
    print(f'coluna b.getcol(1)\n{coluna}\n')

    print(f'linha.dot(coluna)\n{linha.dot(coluna)}\n')

    print(f'matmul(a,b)\n{matmul(a,b)}\n')

    ### agora com Numpy
    import numpy as np
    npa = np.array( lista_a ).reshape((2,3))
    print(f'npa:\n{npa}\n')

    npb = np.array( lista_b ).reshape((3,2))
    print(f'npb:\n{npb}\n')

    print(f'np.matmul(npa, npb):\n{np.matmul(npa, npb)}\n')
    print('ao invés de np.matmul podemos usar @:')
    print(f'npa @ npb:\n{npa @ npb}\n')


## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.


def matmul(esq, dir):
    '''(Array2d, Array2d) -> Array2d
    Recebe dois objetos da classe Array2d e retorna a multiplicação
    matricial ('esq'*'dir')
    '''
    
    resultado = []
    colunas = []
    
    # For para acessar/construir uma única vez as colunas para multiplicação.
    # Melhora em até 2x a performance para numero alto de multiplicações com
    # matrizes grandes, gastando um pouco mais de memória.
    for j in range(dir.shape[1]):
        colunas.append(dir.getcol(j))  
    
    for i in range(esq.shape[0]):
        linha = esq.getlin(i)
        for j in range(dir.shape[1]):
            resultado.append(linha.dot(colunas[j]))

    array_resultado = Array2d((esq.shape[0], dir.shape[1]), None)
    array_resultado.carregue(resultado)

    return array_resultado

# ---------------------------------------------------------------
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
    def getlin(self, lin):
        '''(Array2d, int) -> Array2d
        Recebe uma referência 'self' da classe Array2d e um 'lin' do tipo int
        Retorna um Array2d que contem a linha de índice 'lin' do array 'self'
        '''

        indice_in_data = lin*self.shape[1]
        linha = []
        for i in range(indice_in_data, indice_in_data+self.shape[1]):
            linha.append(self.data[i])

        array_linha = Array2d((1,self.shape[1]), None)
        array_linha.carregue(linha)    
        
        return array_linha
    
    # ---------------------------------------------------------------
    def getcol(self, col):
        '''(Array2d, int) -> Array2d
        Recebe uma referência 'self' da classe Array2d e um 'col' do tipo int
        Retorna um Array2d que contem a coluna de índice 'lin' do array 'self'
        '''

        nlins, ncols = self.shape
        coluna = []
        for i in range(nlins):
            coluna.append(self.data[ncols*i + col])
        
        array_coluna = Array2d((self.shape[0], 1), None)
        array_coluna.carregue(coluna)

        return array_coluna
    
    # ---------------------------------------------------------------
    def dot(self, other):
        '''(Array2d, Array2d) -> obj
        Recebe uma referência 'self' da classe Array2d e um 'other' do tipo Array2d
        Retorna a somatória da multiplicação elemento a elemento de 'self' e 'other'
        '''

        produto = 0
        for i in range(self.size):
            produto += self.data[i]*other.data[i]

        return produto
    
    # ---------------------------------------------------------------
    def resize (self, novo_shape):
        ''' (Array2d, tuple) -> None
        Recebe uma referência 'self' da classe Array2d e uma tupla e cria uma
        nova referência para 'self.shape' com a tupla recebida 'novo_shape'
        '''

        self.shape = novo_shape

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