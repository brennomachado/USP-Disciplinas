# EI11
Data de entrega: segunda, 27 set 2021, 22:00
Arquivos requeridos: array2d.py ( Baixar)
Tipo de trabalho: Trabalho individual

## da classe Array2d para Numpy

## Objetivos

Nesse exercício vamos começar a trabalhar com Numpy, uma poderosa biblioteca numérica do Python. Nessa transição, vamos implementar alguns novos métodos muito úteis em álgebra linear na classe Array2d e discutir como esses comportamentos são realizados usando objetos da classe ndarray do Numpy.
Estudos preliminares

- Introdução ao NumPy: esse texto “interativo” é baseado nas seções 2.1 a 2.4 do NumPy User Guide.

## Introdução

Quando trabalhamos com estruturas com muitos dados, devemos tomar o cuidado de não “desperdiçar” a memória do computador criando várias cópias da mesma estrutura. Nesse exercício, introduziremos o conceito de vista que nos ajuda a mitigar esse problema.

## O que você deve fazer

Nesse exercício você deve implementar mais três métodos da classe Array2d:
- **def getlin (self, lin)**: que recebe um *Array2d* *self* e um inteiro *lin* e um *Array2d* formado pela a linha de índice *lin* de *self*.
- **def getcol (self, col)**: que recebe um *Array2d* *self* e um inteiro *col* e um *Array2d* formado pela coluna de índice *col* de *self*.
- **def dot (self, other)**: que recebe um *Array2d* *self* e outro *Array2d* other com o mesmo número de elementos (*size*), e retorna um número (*escalar*) resultante do produto termo a termo entre *self* e *other*.

Além desses 3 métodos, implemente também a função:
- **def matmul ( esq, dir )**: que recebe um *Array2d* *esq* de dimensão (m, n) e outro *Array2d* *dir* de dimensão (n, p) e retorna o produto matricial entre *esq* e *dir*, que deve ser outro *Array2d* de dimensão (m, p).

Para entender melhor o comportamento desses métodos e função, estudo o trecho de programa abaixo e o resultado dos prints.
```
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
```

Saída dos comandos print():
```
Testes da classe Array2d e comparação com Numpy

teste 1: Criação do Array2d a:
0 0 0 0 0 0

a:
1 2 3
4 5 6

b:
0 1
1 0
0 1

linha a[0,:]
1 2 3

coluna b[:,1]
1
0
1

linha.dot(coluna)
4

matmul(a,b)
2 4
5 10

npa:
[[1 2 3]
 [4 5 6]]

npb:
[[0 1]
 [1 0]
 [0 1]]

np.matmul(npa, npb):
[[ 2  4]
 [ 5 10]]

ao invés de np.matmul podemos usar @:
npa @ npb:
[[ 2  4]
 [ 5 10]]
```
## Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- Utilize o arquivo array2d.py que você entregou anteriormente individualmente, que pode corresponder também ao trabalho que você realizou com seu time.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o if __name__ ... no final do arquivo.
- Submeta apenas o arquivo array2d.py.

## Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

## Arquivos requeridos
#### array2d.py
```
# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome:
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

## ==================================================================

def main():

    print("Testes da classe Array2d\n")


## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        print("Vixe! ainda não fiz o construtor da classe.")

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
        print("Vixe! ainda não fiz o método __getitem__.")

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
        print("Vixe! ainda não fiz o método __setitem__.")

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        print("Vixe! ainda não fiz o método __str__.")

    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar


## ==================================================================

if __name__ == '__main__':
    main()
```
