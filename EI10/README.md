# EI10
Data de entrega: quinta, 23 set 2021, 08:00

# Extensões da classe Array2d

##Objetivos

Nesse exercício vamos estender a classe Array2d para explorar os conceitos de copia e vista de objetos.
Estudos preliminares

- Tuplas e mutabilidade
- Listas aninhadas

## Introdução

Quando trabalhamos com estruturas com muitos dados, devemos tomar o cuidado de não “desperdiçar” a memória do computador criando várias cópias da mesma estrutura. Nesse exercício, introduziremos o conceito de vista que nos ajuda a mitigar esse problema.
O que você deve fazer

Nesse exercício você deve implementar mais dois métodos da classe Array2d: copy() and reshape().

O método copy() retorna uma cópia completa do objeto do tipo Array2d, ou seja, incluindo uma cópia da lista data do objeto.

Já o método reshape() recebe uma tupla com uma dimensão (nlin, ncol) e retorna uma vista do objeto do tipo Array2d. A vista se comporta como um objeto Array2d com a nova dimensão, ou seja, com valores diferentes do atributo shape, mas compartilha a mesma lista data.

Para entender o comportamento esperado de vistas e cópias, estude o trecho de programa abaixo e o resultado dos comandos **print()**.

    ```
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
    ```

Saída dos comandos **print()**:

```
Testes da classe Array2d

teste 1: Criação do Array2d a:
3 3 3 3 3 3

teste 2: reshape cria uma vista
3 3 3
3 3 3

teste 3: mudanças em b devem resultar em mudanças em a:
3 3 3 3 3 100
3 3 3
3 3 100

teste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:
3 3 -1 3 3 100
3 3 -1
3 3 100

teste 5: copy cria um clone
a: 3 3 3 3 3 3
c: 3 3 3 3 3 3

teste 6: mudanças em um objeto não devem refletir no outro
a: 3 99 3 3 3 3
c: 3 3 3 3 3 -1
```

## Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- Utilize o arquivo array2d.py que você entregou anteriormente individualmente, que pode corresponder também ao trabalho que você realizou com seu time.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
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