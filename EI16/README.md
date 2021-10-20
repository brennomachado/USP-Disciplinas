# EI16
Data de entrega: quinta, 21 out 2021, 08:00
Arquivos requeridos: binomial.py ( Baixar)
Tipo de trabalho: Trabalho individual

## Recursão

Vamos continuar a desenvolver algoritmos recursivos e aprender a torná-los tão eficientes quanto suas versões iterativas. Dessa vez, vamos aplicar memoization usando um array do Numpy como rascunho.
### Atividades preliminares

- Leitura sobre [Recursão](https://panda.ime.usp.br/pensepy/static/pensepy/12-Recursao/recursionsimple-ptbr.html)
- [EG15: recursão com memoização](https://edisciplinas.usp.br/mod/vpl/view.php?id=3929818)

### O que você deve fazer

Considere dois inteiros não-negativos n e k. O número ou [coeficiente binomial](https://pt.wikipedia.org/wiki/Coeficiente_binomial) (n k)
é número de maneiras diferentes em que que k objetos podem ser escolhidos, independentemente da ordem, de um conjunto com n objetos. Por exemplo, (35)=0, (34)=0, (33)=1, (32)=3, (31)=3 e (30)=1.

Neste exercício você escreverá duas funções que retornam o valor de binomial(n,k) (=(nk)):

- a função binomialI() que calcula iterativamente o valor de binomial(n,k); e
- a função binomialRM() que calcula recursivamente o binomial(n,k).

Para resolver esse exercício, primeiro obtenha a fórmula recursiva para calcular o binomial(n,k). Essa fórmula pode ser derivada do Triângulo de Pascal, como ilustrado na tabela abaixo, onde n é o índice de uma linha e k o índice de uma coluna. DICA: observe que o valor de binomial(n,k) resulta da adição de dois números da linha (n-1).

    k -> 0   1   2   3   4   5   6
      _____________________________
    n |
    0 |  1   0   0   0   0   0   0   
    1 |  1   1   0   0   0   0   0
    2 |  1   2   1   0   0   0   0
    3 |  1   3   3   1   0   0   0
    4 |  1   4   6   4   1   0   0
    5 |  1   5  10  10   5   1   0
    6 |  1   6  15  20  15   6   1   

Por exemplo, a tabela acima mostra que:

 - binomial(3,2) é 3;
 - binomial(4,1) é 4; e
 - binomial(6,3) é 20.

Após obter a fórmula recursiva, você deve escrever a função iterativa binomialI() a recursiva binomialRM() como definidas no arquivo binomial.py. A função binomialRM() usa memoização para evitar o recálculo de valores. Por isso, ela recebe um parâmetro rascunho que é um ndarray que armazena os valores intermediários do triângulo de Pascal e com isso evita que um mesmo valor seja recalculado várias vezes; como ocorreu com a função finonacciR().

Para facilitar o uso da função binomialRM() para que possamos utilizá-la usando apenas um par (n,k) e esconder o array rascunho de quem quer apenas o valor do binomial, criamos uma interface simplificada na forma da função binomialR(n,k). A função binomialR(n,k) já está implementada no arquivo binomial.py e chama a função binomialRM().

### Roteiro

Leia o(s) texto(s) sugeridos na seção Atividades premilinares.

 - Baixe o arquivo binomial.py para uma pasta do seu computador.
 - Carregue esse arquivo usando o Spyder ou Colab ou …
 - Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
 - Estude o enunciado os exemplos fornecidos para entender o que você deve implementar.
 - Implemente, documente e teste seu trabalho.
 - Caso você deseje testar sua classe no próprio arquivo, não deixe de incluir o if \_\_name__ ... no final do arquivo.
 - Submeta apenas o arquivo binomial.py.

### Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

### Arquivos requeridos
##### binomial.py
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

import numpy as np

## CONSTANTES

DEBUG = True

## ==================================================================

def binomialI(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialI(3,2)  -> deve retornar 3
    b) binomialI(5,1)  -> deve retornar 5
    c) binomialI(1,5)  -> deve retornar 0
    d) binomialI(4,2)  -> deve retornar 6

    NOTA. Está função é iterativa.
    '''
    print("Vixe! ainda não fiz a função binomialI")

## ==================================================================

def binomialR(n, k):
    '''(int,int) -> int

    RECEBE inteiros não-negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialR(3,2)  -> deve retornar 3
    b) binomialR(5,1)  -> deve retornar 5
    c) binomialR(1,5)  -> deve retornar 0
    d) binomialR(4,2)  -> deve retornar 6

    NOTA. Está função é uma interface para a função 
          binomialRM() e não deve ser alterada.
    '''
    # cria um array de dimensão (n+1)x(k+1) para ser usado como rascunho
    rascunho = np.zeros((n+1, k+1), int) 
    rascunho[:,0] = 1

    bin = binomialRM(n, k, rascunho)
    if DEBUG:
        print("Debug ligado.")
        print(f"bin({n}, {k}) = {bin}")
        print(f"   Rascunho:\n{rascunho}")

    return bin

## ==================================================================

def binomialRM(n, k, rascunho):
    '''(int, int, array) -> int

    RECEBE inteiros não negativos n e k e um array bidimensional rascunho.
    RETORNA o valor de binomial(n,k).

    NOTA. Está função é recursiva.
        Ela usa as posições do array rascunho para  guardar os valores dos 
        binomiais já calculado: 
           - rascunho[i][j] armazenará o valor de binomial(i, j).
        Com isso a função evita que um mesmo número binomial seja recalculado 
        várias vezes.
    '''
    print("Vixe! ainda não fiz a função binomialRM")

```