## EI23

Data de entrega: quinta, 18 nov 2021, 08:00
Arquivos requeridos: pivotacao.py ([Baixar])(https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3968315))
Tipo de trabalho: Trabalho individual

## Ordenação por pivotação

### Objetivos

Neste exercício vamos continuar o tópico de ordenação de listas.

- Mas por que estudar ordenação se o Python já faz isso pra mim?

O **problema de ordenação** é um muito rico em soluções diferentes, cada uma baseada em ideias distintas que vai nos ajudar a continuar a desenvolver o pensamento computacional. Vamos aproveitar também para treinar e aprofundar vários fundamentos de análise de algoritmos.

Sendo assim, para treinar esses fundamentos nesses e em futuros exercícios, utilize apenas comandos básicos do Python e, para continuar a desenvolver o pensamento, evite pensar no tipo list. Procure desenhar no papel sequências de números que devem ser ordenados, por exemplo, percorrendo as sequência e trocando os elementos de posição.

---

### Motivação

Um problema do Mergesort (ordenação por intercalação) é o consumo de espaço extra de O(n). Será que podemos ter um algoritmo de ordenação com consumo de tempo O(nlg n) e memória O(1)?

Nesse exercício você deve implementar a função pivote_seq(), que é a base do algoritmo de ordenação conhecido como Quicksort ou ordenação por pivotação.

### Separação dos elementos de uma lista em torno de um pivô

Se seq é uma lista escreveremos seq[i: j] <= x como uma abreviatura de seq[k] <= x para todo k = i, i + 1, …, j − 1. Também escreveremos expressões semelhantes a seq[i: j] <= seq[k: t] significando que para todo elemento x de seq[i: j] e y de seq[k: t] vale que x <= y.

### Problema

Rearranjar uma dada lista seq com n > 0 elementos, usando o último elemento da lista como pivô. Retorna um índice m, com 0 ≤ m < n, tal que

seq[ : m] ≤ seq[m] < seq[m + 1 : n],

onde seq[m] é a nova posição do pivô.

Observe que, após a pivotagem, o pivô se encontra “ordenado” em relação aos demais elementos na lista.

    Entra:

            0                                                n
         +----+----+----+----+----+----+----+----+----+----+
    seq  | 99 | 33 | 55 | 77 | 11 | 22 | 88 | 66 | 33 | 44 |
         +----+----+----+----+----+----+----+----+----+----+

    Resultado da sequência pivotada usando 44 como pivô
    Retorna: 4

           0                   m                             n
         +----+----+----+----+----+----+----+----+----+----+
    seq  | 33 | 11 | 22 | 33 | 44 | 55 | 99 | 66 | 77 | 88 |
         +----+----+----+----+----+----+----+----+----+----+

---

### O que você deve fazer

Nesse exercício você deve implementar 2 funções:

- pivote_seq(seq)
- main(): que deve incluir 10 testes para sua função.

O comportamento de cada função está descrito no cabeçalho das funções no arquivo pivotacao.py.

### Material de apoio

O seguinte material foi criado para fornecer uma ideia inicial de uma possível solução. Procure desenvolver mais a idea em papel, usando outros exemplos, antes de implementá-la em Python. Como há outras ideias possíveis, não é necessário que sua solução seja baseada nessa ideia, desde que ela tenha consumo de tempo O( n ) e consumo de memória extra O(1).

- [Assista esse vídeo de introdução](https://drive.google.com/file/d/1SnTo18RgyjV3s00kjPrNkagUAHWWu32K/view?usp=sharing)
- [Slides usados no vídeo](https://drive.google.com/file/d/1Ao3E3PoVfzl4jrvPUIb8AdneqnAInrN-/view?usp=sharing)

---

### Roteiro

- Baixe o arquivo pivotacao.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab ou seu IDE Python predileto.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Submeta apenas o arquivo pivotacao.py.

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

##### pivotacao.py

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
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas de tamanho mínimo, em ordem crescente,
        decrescente, etc.
    '''
    print("Testes do EI23 - ordenação por pivotação")

def pivote_seq(seq):
    ''' (list) -> int

    Recebe uma lista seq com n>0 elementos
    e rearranja seus elementos para que o pivô,
    o último elemento da lista,
    esteja na posição "ordenada" com relação aos demais
    elementos, ou seja, todos os elementos menores fiquem
    a esquerda e todos os maiores fiquem a direita do pivô.

    Retorna um índice m tal que

        seq[:m] <= seq[m] < seq[m+1:]

    Exemplos:
    In [1] seq = [5, 7, 4, 3, 8, 6]
    In [2] m = pivote_seq(seq)
    In [3] m
    3
    In [4] seq
    [5, 4, 3, 6, 8, 7]

    ...

    In [11] seq = [6, 7, 5, 3, 8, 4]
    In [12] m = pivote_seq(seq)
    In [13] m
    1
    In [14] seq
    In [3, 4, 5, 6, 8, 7]

    DICAS:
    - observe que a pivotagem não ordena os elementos à
    esquerda e à direita do pivô. Portanto, seu resultado
    pode ser diferente, desde que o pivô esteja na posição
    correta.
    - não use sort() para resolver essa função, que tem
    consumo de tempo O(n lg n). O consumo
    de tempo esperado para essa função é O(n) e o
    de memória é O(1).
    - O vídeo cujo link você encontra no enunciado dessa
    atividade ilustra uma possível solução.
    '''

    # escreva sua solução


#-----------------------------------------------
if __name__ == '__main__':
    main()
```
