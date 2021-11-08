# EI20

Data de entrega: segunda, 8 nov 2021, 22:00
Arquivos requeridos: insercao.py ([Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3954314))
Tipo de trabalho: Trabalho individual

## Algoritmo de ordenação por inserção

### Objetivos

Neste e em próximos exercícios vamos continuar o tópico de ordenação de listas.

- Mas por que estudar ordenação se o Python já faz isso pra mim?
  - O problema de “ordenação” é muito rico em soluções diferentes, cada uma baseada em ideias distintas que vai nos ajudar a continuar a desenvolver o pensamento computacional. Vamos aproveitar também para treinar e aprofundar vários fundamentos de análise de algoritmos.

Sendo assim, para treinar esses fundamentos nesses e em futuros exercícios, utilize apenas comandos básicos do Python e, para continuar a desenvolver o pensamento, evite pensar no tipo list. Procure desenhar no papel sequências de números que devem ser ordenados, por exemplo, percorrendo as sequência e trocando os elementos de posição.

---

### O que você deve fazer

Nesse exercício você deve implementar 3 funções:

- insira_ultimo(seq, n)
- ordene_por_insercao( seq )
- main(): que deve incluir os seus testes para cada função.

---

### Roteiro

- Baixe o arquivo insercao.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if \_ _ name _ \_ …” no final do arquivo.
- Submeta apenas o arquivo insercao.py.

---

### Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

---

#### Arquivos requeridos

##### insercao.py

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

def main():
    '''
        Testes das suas funções
    '''

    print("Testes do EI20 - ordenação por inserção")


## ==================================================================

def insira_ultimo(seq, n):
    ''' (list, int) -> None

    Essa função é a base para o algoritmo de ordenação
    por inserção, que veremos em uma próxima aula e
    não se trata de um algoritmo completo de ordenação.

    Essa função considerar apenas a porção da lista seq
    no intervalo [0:n].

    A ideia é visitar cada elemento, a partir do fim da
    porção, ou seja, do elemento de índice n-1.
    Caso o elemento anterior seja maior, os elementos são
    trocados de posição, fazendo o elemento visitado "descer"
    na lista. A varredura deve persistir enquanto o elemento
    visitado for menor que o seu anterior.

    Por exemplo,  para seq = [4, 7, 11, 5, 3] e n = 3 a
    função não precisa fazer nada pois o elemento anterior
    ao 11 já é menor.

    Para seq = [4, 7, 11, 5, 3] e n = 4 a
    função deve deslocar o 5 até que seq se torne
    [4, 5, 7, 11, 3].

    Outro exemplo, para seq = [4, 5, 7, 11, 3] e n = 5 a
    função deve deslocar o 3 até que seq se torne
    [3, 4, 5, 7, 11].

    DICA: não use outras listas, nem fatias. Basta
    varrer seq, comparar com seu vizinho anterior
    e trocar enquanto necessário.

    '''
    # escreva sua solução

## ==================================================================

def ordene_por_insercao(seq):
    ''' (list) -> None

    A ideia de ordenação por inserção (insertion sort)
    é considerar porções da lista, a partir de 2 elementos até n.
    Para cada porção, apenas o último elemento precisa ser
    deslocado até sua posição correta.

    Exemplo para a lista [4, 7, 5, 3]
    - inicio com a porção da lista de tamanho 2 contendo [4, 7, ? , ?].
        O último elemento já está na posição correta.
    - a ordenação continua com a porção de tamanho 3 com [4, 7, 5, ?]
        O último elemento da porção, o 5, precisa ser deslocado até
        sua posição final [4, 5, 7, ?]
    - a ordenação continua com a porção de tamanho 4, agora com
        [4, 5, 7, 3]. O último elemento da porção, o 3, precisa ser
        deslocado até sua posição final [3, 4, 5, 7].
    - fim, pois já tratamos todas as porções até o tamanho n.

    O que você deve fazer:

    A função recebe uma sequência de números em ordem aleatória.
    e retorna None. Ao terminar, seq deve estar em ordem
    crescente aplicando a ideia de ordenação por inserção.

    Essa função DEVE usar a função insira_ultimo().

    '''
    # escreva sua solução

## ==================================================================
## Escreva outras coisas que desejar
## ==================================================================


## ==================================================================

if __name__ == '__main__':
    main()

## ==================================================================
```
