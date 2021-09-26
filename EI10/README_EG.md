# EG10
Disponível a partir de: quinta, 23 set 2021, 10:00
Data de entrega: quinta, 23 set 2021, 12:30
Arquivos requeridos: eg_array2d.py ( Baixar)
Tipo de trabalho: Trabalho individual
### Exercício em time: EG da aula 10 - extensões da Classe Array2d

Não se esqueça de preencher o Formulário Individual

Procurem ler as instruções para as atividades específicas em grupo
Preparação para a atividade em time

As instruções gerais para as atividades em grupo estão aqui.

Basicamente você deve:
- voltar para a sala principal caso você esteja sozinhE.
- fazer uma cópia do seu EI, colocando o prefixo eg_. Assim, se o nome do arquivo EI for exercicio.py, o nome do arquivo a ser entregue será eg_exercicio.py. Vamos chamar esse arquivo de EG.
- sortear a pessoa “estagiária” e a pessoa “gerente” conforme as instruções.
- preencher o formulário individual conforme as instruções.

## Atividades específicas

A partir daqui sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.

### Roteiro para realizar esse exercício

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

1. Teste a classe Array2d usando uma função main() no mesmo arquivo array2d.py.
   - Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.
   - Inclua o comando if __name__ == '__main__': para chamar a função main() como ilustrado no último exercício em time.

2. Correção e testes individuais
    - Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
    - Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
    - Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

3. Desafio 1: inclua na classe Array2d o método de protótipo def carregue(self, nova_lista), que recebe uma lista do mesmo tamanho de self.size e carrega a lista self.data com o conteúdo de nova_lista. Observe o exemplo a seguir com atenção para entender o efeito esperado do “carregamento” é uma referência ou cópia da lista.

```lista = [1,2,3,4,5,6]
a = Array2d( (2,3), 0)
print(f'a:\n{a}\n')

a.carregue( lista )
print(f'a:\n{a}\n')

a[1,1] = -1
print(f'a:\n{a}\n')
print(f'lista: {lista}')
```

A saída desse trecho deve ser:

```
a:
0 0 0
0 0 0

a:
1 2 3
4 5 6

a:
1 2 3
4 -1 6

lista: [1, 2, 3, 4, -1, 6]
```

1. Desafio 2: inclua na classe Array2d o método de protótipo def carregue2(self, nova_lista), que recebe uma lista do mesmo tamanho de self.size e carrega a lista self.data com o conteúdo de nova_lista. Observe o exemplo a seguir com atenção para entender o efeito esperado do “carregamento”.
```
lista = [1,2,3,4,5,6]
a = Array2d( (2,3), 0)
print(f'a:\n{a}\n')

a.carregue2( lista )
print(f'a:\n{a}\n')

a[1,1] = -1
print(f'a:\n{a}\n')
print(f'lista: {lista}')
```
A saída desse trecho deve ser:
```
a:
0 0 0
0 0 0

a:
1 2 3
4 5 6

a:
1 2 3
4 -1 6

lista: [1, 2, 3, 4, 5, 6]
```
5. Desafio 3: inclua na classe Array2d o método de protótipo def flipV(self), que retornar um objeto Array2d com os elementos de self refletidos verticalmente, ou seja, reflete as linhas, como ilustrado no trecho de código a seguir.

```
lista = [1,2,3,4,5,6,7,8,9,0]
a = Array2d( (5,2), 0)
a.carregue( lista )
print(f'a:\n{a}\n')

flip = a.flipV()
print(f'flip:\n{flip}\n')

print(f'a:\n{a}\n')
```
A saída desse trecho deve ser:

```
a:
1 2
3 4
5 6
7 8
9 0

flip:
9 0
7 8
5 6
3 4
1 2

a:
1 2
3 4
5 6
7 8
9 0
```

6. Desafio 4: função de protótipo def flipH( array ), que recebe um objeto Array2d e o altera, refletindo suas colunas. Para esse desafio, procure minimizar o uso de memória auxiliar usada para refletir as colunas de array. A função deve retornar None.

```
lista = [1,2,3,4,5,6,7,8,9,0]
a = Array2d( (2,5), 0)
a.carregue( lista )
print(f'a:\n{a}\n')

flipH(a)
print(f'a:\n{a}\n')
```
A saída desse trecho deve ser:
```
a:
1 2 3 4 5
6 7 8 9 0

a:
5 4 3 2 1
0 9 8 7 6
```
### O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com prefixo eg_ contendo o seu trabalho.

Você também precisa responder o formulário individual caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.

## Arquivos requeridos
#### eg_array2d.py
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