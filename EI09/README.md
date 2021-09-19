# EI09
Data de entrega: segunda, 20 set 2021, 22:00

# Classe Array2d

## Objetivos

O objetivo deste exercício é continuar a treinar a habilidade de pensar com tipos abstratos de dados, explorando o poder que a POO nos fornece ao permitir criar novos tipos. Nesse exercício vamos também reforçar o uso de tuplas (tipo tuple do Python) e o conceito de mutabilidade.
Estudos preliminares

- Tuplas e mutabilidade
- Listas aninhadas

## Introdução

Uma forma de representar matrizes de 2 dimensões em Python é por meio de listas aninhadas, como ilustrado no seguinte trecho de código Python:

```
>>> m2d = [ [1, 2, 3], [4, 5, 6] ]
>>> print(m2d)
[[1, 2, 3], [4, 5, 6]]
>>> m2d[1][1] = -1
>>> print(m2d)
[[1, 2, 3], [4, -1, 6]]
```

Nesse caso, a lista aninhada m2d, que contém \[[1, 2, 3], [4, 5, 6]], pode ser considerada uma matriz de dimensão (2,3), ou seja, com 2 linhas e 3 colunas, onde a primeira linha é representada pela lista linear [1, 2, 3] e a segunda linha por [4, 5, 6]. Observe que um elemento de m2d pode ser acessado usando dois pares de colchetes. O primeiro par define o índice da linha e o segundo define o índice da coluna.

Nesse exercício, ao invés de usar listas aninhadas para representar uma matriz, vamos começar a implementar a classe Array2d, cujos dados são armazenados em uma lista linear que pode ser acessada pelo atributo de nome data. Assim, usando o mesmo exemplo anterior, o conteúdo de data seria a lista [1, 2, 3, 4, 5, 6].

Nesse caso, a classe Array2d precisa de mais informação para saber qual a dimensão da matriz. Você deve criar também um atributo de nome shape que armazena uma tupla com as dimensões da matriz que, nesse exemplo, corresponde a tupla (2,3).

Vamos ver que é possível usar esses 2 atributos, data e shape, para trabalhar com matrizes 2d mas que internamente armazenam seus dados em uma lista 1d (linear). O primeiro problema que precisamos resolver é como acessar um elemento da lista data a partir de um par de coordenadas (lin, col). No exemplo, o elemento na posição (0, 1) é 2 e na posição (1,2) é 6.

Felizmente a solução é relativamente simples. Como sabemos o tamanho de cada linha, que corresponde ao número de colunas da matriz armazenada na tupla shape, para acessar o elemento na coordenada (lin, col), basta converter a coordenada para o índice shape[1] * lin + col da lista data, ou seja, data[ shape[1] * lin + col ].

Finalmente, como um objetivo é treinar o uso de tuplas, vamos usar tuplas também para criar um objeto Array2d e também para acessar seus elementos.
O que você deve fazer

Você deve implementar os métodos e atributos da classe Array2d necessários para que um objeto dessa classe apresente o comportamento como descrito na seguinte função main() de testes:

```
def main():

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
```

Preste atenção na saída desse programa mostrada a seguir, resultante dos prints, que define a parte do comportamento de objetos da classe Array2d que você deve implementar.


Testes da classe Array2d
```
teste 1: Criação do Array2d a:
3 3 3
3 3 3
shape: (2, 3)
size : 6
data : [3, 3, 3, 3, 3, 3]

teste 2: Criação do Array2d b:
1.7 1.7 1.7
1.7 1.7 1.7
shape: (2, 3)
size : 6
data : [1.7, 1.7, 1.7, 1.7, 1.7, 1.7]

teste 3: a[0,1] + 100 é: 103

teste 4: Array2d a:
3 3 3
3 -1 3
```
Você pode estender a classe com outros atributos e métodos, caso desejar, desde que não entrem em conflito com os comportamentos e especificações constantes nesse enunciado.
Dicas sobre esses comportamentos

Observe que um objeto da classe Array2d possui ao menos os seguintes 3 atributos: data e shape, como já descritos, e size que contém o número total de elementos do Array2d.

Ao criar um objeto da classe Array2d, o primeiro argumento é uma tupla e o segundo argumento é o valor inicial usado para carregar a lista data.

Observe o que acontece com o comando print(a) e siga a documentação descrita no método ***\_\_str__()*** do arquivo array2d.py.

Por fim, veja como podemos usar tuplas para manipular elementos de um objeto Array2d. Para pegar o valor de um elemento de um Array2d e usá-lo em uma expressão, por exemplo, como no teste 6: a[0,1] + 100, é necessário definir o método especial **\_\_getitem__(self, key)**, onde o parâmetro key corresponde à tupla entre colchetes que define a posição (lin, col) da matriz de onde o valor será lido para ser retornado pelo método.

Quando desejamos atribuir um novo valor a um elemento de um Array2d, por exemplo, como no teste 7 onde a[1,1] recebe o valor -1, é necessário definir o método especial **\_\_setitem__(self, key, valor)**, onde o parâmetro key corresponde à tupla entre colchetes que define a posição (lin, col) da matriz onde o valor valor será armazenado.
Roteiro

#### Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- Baixe o arquivo array2d.py.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “***if __ name __*** …” no final do arquivo.
- Submeta apenas o arquivo array2d.py.

#### Honestidade acadêmica

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