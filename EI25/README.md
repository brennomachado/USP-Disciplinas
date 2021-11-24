# EI25

Data de entrega: quinta, 25 nov 2021, 08:00
Arquivos requeridos: some3.py ([Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3974776))
Tipo de trabalho: Trabalho individual

## Soma de 3 números

### Motivação

Nas últimas atividades tratamos de projeto e análise de algoritmo tendo como pretexto o problema de ordenação. Vimos várias técnicas nesse contexto:

- algoritmos dinâmicos: ordenação por inserção
- divisão e conquista: mergesort() e quicksort()
- estruturas de dados: ordenação por seleção com max-heap se transforma no heapsort()

Vimos como expressar o consumo de tempo e espaço através de notação assintótica. O resultado, em termos de consumo de tempo foi

| Algoritmo        | melhor caso | pior caso |
| ---------------- | ----------- | --------- |
| seleção          | O(n²)       | O(n²)     |
| inserção         | O(n)        | O(n2)     |
| inserção binária | O(nlg n)    | O(n2)     |
| borbulhagem      | O(n)        | O(n2)     |
| mergesort        | O(nlg n)    | O(nlg n)  |
| quicksort        | O(nlg n)    | O(n2)     |
| heapsort         | O(nlg n)    | O(nlg n)  |

Também vimos análise experimental para validar os valores analíticos.

Neste exercício vamos continuar a treinar o projeto e análise de algoritmos com um problema distinto. Vamos aproveitar também para revisar o tipo dict (dicionário) do Python.

---

### Problema Soma3

Definição: dada uma lista de números inteiros, determinar o número de trios que somam zero.

Por exemplo, para a lista [30, -30, -20, -10, 40, 0, 10, 15] temos que há 4 trios que somam zero:

```
     30  -30   0
     30  -20 -10
    -30  -10  40
    -10    0  10
```

Esse problema é conhecido como Soma3 (3SUM problem) (Wikipedia) e, apesar de parecer artificial, está relacionado a várias tarefas computacionais fundamentais em geometria computacional.

Hipótese simplificadora: a lista não possui dois números iguais, ou seja, são todos distintos.

Essa hipótese simplifica o código de algumas soluções.

---

### Revisão de Dicionários

Um dicionário é um tipo abstrato de dados que associa uma chave a um valor. A chave precisa ser única, ou seja, não pode haver chaves repetidas e também deve ser imutável, ou seja, uma vez criada, ela permanece a mesma.

O Python possui o tipo nativo dict que permite a criação e manipulação de dicionários. Para se criar um dicionário vazio, utilize:

```
    dic = {}
```

ou seja, use chaves ao invés dos colchetes usados na criação de listas.

Você também pode criar dicionários com elementos, separando a chave do valor usando : (dois pontos) como:

```
    >>> dic = {'banana':50, 'abacaxi':10}
    >>> print(dic)
    {'banana': 50, 'abacaxi': 10}
```

E você pode usar as chaves entre colchetes para criar ou modificar um elemento do dicionário como:

```
    >>> dic = {'banana':50, 'abacaxi':10}
    >>> print(dic)
    {'banana': 50, 'abacaxi': 10}
    >>> dic["melancia"] = 7
    >>> print(dic)
    {'banana': 50, 'abacaxi': 10, 'melancia': 7}
    >>> dic['banana'] += 15
    >>> print(dic)
    {'banana': 65, 'abacaxi': 10, 'melancia': 7}
    >>>
```

O acesso de uma chave usando colchetes [] resulta em erro caso a chave não exista (experimente!). Uma forma de evitar esse erro é acessar uma chave usando o método get(chave), que retorna None caso a chave não existir.

O for oferece uma forma conveniente de varrer todas as chaves do dicionário, como:

```
    >>> for fruta in dic:
    ...     print(f"chave:{fruta} \t valor: {dic[fruta]}")
    ...
    chave:banana     valor: 65
    chave:abacaxi    valor: 10
    chave:melancia   valor: 7
    >>>
```

Para saber mais:

- Dicionários. Notas de aula de Introdução à Computação.
- Dicionários. Do livro “Como Pensar Como um Cientista da Computação”

---

### O que você deve fazer

Nesse exercício você deve implementar 3 métodos da classe Soma3:

- imprima_pares(self)
- imprima_trios(self)
- monte_dicio_pos(self)

como descritos no arquivo soma3.py. Antes de implementar esses métodos, estude os métodos já implementados dessa classe. Esses métodos já implementados não devem ser modificados. Você deve também complementar a função main() com testes mais variados.

Observe que a classe ainda não possui métodos para resolver o problema Soma3. Esse é um exercício de preparação para que possamos resolver e discutir alguns algoritmos para a solução desse problema durante a discussão em grupos na próxima reunião.

O comportamento desses métodos pode ser observado pela saída do seguinte trecho de programa:

```
def main():
    '''
    Testes da classe Soma 3

    inclua mais 10 testes usando listas diferentes. Por exemplo,
    o que deve acontecer com listas vazias, listas com números negativos,
    listas ordenadas, etc.
    '''
    print("Testes do EI25 - Soma3")

    testes = [
        [44, 11, 77, 33]
    ]

    for t in testes:

        s3 = Soma3(t)
        print(f"\nCriação usando a lista:\nent : {t}")
        print(f"{s3}")

        print("\nDicionário de posições:")
        s3.monte_dicio_pos()
        print(f"{s3}")

        print("\nPares")
        s3.imprima_pares()

        print("\nTrios")
        s3.imprima_trios()
```

A saída esperada é:

```
    Testes do EI25 - Soma3

    Criação usando a lista:
    ent : [44, 11, 77, 33]
    data: [44, 11, 77, 33]
    pos : {}


    Dicionário de posições:
    data: [44, 11, 77, 33]
    pos : {44: 0, 11: 1, 77: 2, 33: 3}


    Pares
    44  11
    44  77
    44  33
    11  77
    11  33
    77  33

    Trios
    44  11  77
    44  11  33
    44  77  33
    11  77  33
```

Roteiro

- Baixe o arquivo soma3.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab ou seu IDE Python predileto.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Submeta apenas o arquivo soma3.py.

---

### Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

---

### Arquivos requeridos

##### some3.py

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
#
def main():
    '''
    Testes da classe Soma 3

    inclua mais 10 testes usando listas diferentes. Por exemplo,
    o que deve acontecer com listas vazias, listas com números negativos,
    listas ordenadas, etc.
    '''
    print("Testes do EI25 - Soma3")

    testes = [
        [44, 11, 77, 33]
    ]

    for t in testes:

        s3 = Soma3(t)
        print(f"\nCriação usando a lista:\nent : {t}")
        print(f"{s3}")

        print("\nDicionário de posições:")
        s3.monte_dicio_pos()
        print(f"{s3}")

        print("\nPares")
        s3.imprima_pares()

        print("\nTrios")
        s3.imprima_trios()

# ===================================================================

class Soma3:

    def __init__(self, seq):
        ''' (Soma3, list) -> None
        '''
        self.data = seq  # faz referência, não copia.
        self.pos = {}

    def __str__(self):
        ''' (Soma3) -> None
        '''
        return f'data: {self.data}\npos : {self.pos}\n'

    # -------------------------------------------------------------------

    def imprima_pares(self):
        ''' (Soma3) -> None

        Imprime todos os pares da lista self.data.
        Exemplo: para self.data = [44, 11, 77, 88]
        o método deve imprimir:
        44  11
        44  77
        44  88
        11  77
        11  88
        77  88
        '''

        # escreva sua solução

    # -------------------------------------------------------------------

    def imprima_trios(self):
        ''' (Soma3) -> None

        Imprime todos os trios da lista self.data.
        Exemplo: para self.data = [44, 11, 77, 88]
        o método deve imprimir:
        44  11  77
        44  11  88
        44  77  88
        11  77  88
        '''

        # escreva sua solução
    # -------------------------------------------------------------------

    def monte_dicio_pos(self):
        ''' (Soma3) -> None

        Monta o dicionário self.pos a partir do conteúdo em self.data.
        Usando cada elemento de self.data como chave, self.pos armazena
        o índice desse elemento na lista self.data.

        Exemplo: para self.data = [44, 11, 77, 88]
        então self.pos deve conter {44:0, 11:1, 77:2, 88:3}
        '''

        # escreva sua solução

# ===================================================================

if __name__ == '__main__':
    main()
```
