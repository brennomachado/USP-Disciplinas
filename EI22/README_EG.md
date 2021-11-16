EG22
Data de entrega: terça, 16 nov 2021, 11:00
Arquivos requeridos: eg_intercalacao.py ( Baixar)
Tipo de trabalho: Trabalho individual

De intercalação a ordenação

Fonte: ShadowTree.
Preparação padrão

Voltem a sala principal caso você esteja sozinhE.

Preencham o Formulário Individual conforme as instruções.

Escolham a pessoa estagiária e a pessoa gerente conforme as instruções.

Sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.

Façam uma cópia do seu EI, colocando o prefixo eg\_. Alternativamente, há um arquivo eg_intercalacao.py com um esqueleto deste EG que pode ser baixado desta página. Este esqueleto contém funções totalmente feitas que usaremos nos experimentos.

Baixem daqui o programa experimento.py que usaremos para fazermos nossas análises experimentais das funções desenvolvidas .

Se tiverem alguma dúvida chamem o Hitoshi ou o Coelho. Eles devem estar passeando pelas salas.
EI: intercalação

Fonte: Merge sort (Wikipedia).
Testes

Testem as funções que vocês fizeram para o EI:

    intercale_seqs(seq1, seq2) e
    main()

Usem para isso as coletânea de testes que cada uma/um fez na função main().

A pessoa estagiária deve agrupar todos os testes na main() do time e compartilhar main() com as demais pessoas do time para que todos possam testar os seus trabalhos individuais.

A propósito, a função intercale_seqs(seq1, seq2) é conhecida nas redes sociais como merge(). Ela é um aquecimento para as funções que vocês escreverão hoje.
Testes individuais

Cada pessoa do time deve verificar as funções do seu EI/EG estão dentro da especificação. Por exemplo, intercale_seqs(seq1, seq2) recebe duas listas e retorna uma lista.

Não hesite em pedir ajuda a seu time em caso de dificuldades.

Caso algum problema seja encontrado, discuta com suas/seus colegas de time para resolvê-lo. Elas/eles ficarão muito felizes em lhe ajudar.
Reflexão

Algumas questões para discutirem.

Qual o número de comparações entre elementos das listas são feitas pela suas funções intercale_seqs(seq1, seq2) quando

    seq1=[2, 5, 7, 11, 15] e seq2=[3] ?
    seq1=[3] e seq2=[2, 5, 7, 11, 15] ?
    seq1=[2, 5, 7, 11, 15] e seq2=[3] ?
    seq1=[3] e seq2=[2, 5, 7, 11, 15] ?
    seq1=[3, 6, 8, 10] e seq2=[2, 5, 7, 11, 15] ?

Em geral, se uma lista seq1 tem n elementos e seq2 tem m elementos, aproximadamente quantas comparações entre elementos das listas são feitas por intercale_seqs(seq1, seq2) no melhor caso (= a função faz poucas comparações) e no pior caso (= a função faz muitas comparações)?

Em notação assintótica, qual o consumo de tempo da sua função no melhor caso (= a função trabalha pouco) e no pior caso (= a função se mata de trabalhar)? É O(1)? É O(lg (n + m))? É O(n + m)? É O((n + m)lg (n + m))? É O((n + m)2)? É O((n + m)3)? É O(2n + m)? É O(?))?.
Desafio: de intercalação a ordenação

Diremos que os elementos de uma lista seq[i:j] estão em ordem crescente se seq[i] ≤ seq[i + 1] ≤ seq[i + 2] ≤ ⋯ ≤ seq[j − 1].
As vezes, de maneira abreviada, falaremos que a lista seq[i:j] é crescente significando que seus elementos estão em ordem crescente.

O desafio deste EG consiste em escrever mais duas funções:

    intercale(seq, e, m, d) e
    ordene_por_intercalacaoR(seq, e, d)

Trataremos de uma por vez.
intercale(seq, e, m, d)

A especifição desta função está a seguir.

def intercale(seq, e, m, d):
''' (list, int, int, int) -> None

    RECEBE uma lista seq e índices e, m e d tais que os elementos de

        - seq[e:m] estão em ordem crescente e
        - seq[m:d] estão em ordem crescente

    REARRANJA os elementos de seq[e:d] para que fiquem em ordem crescente.

    SUGESTÃO: Em busca de inspiração?
    Esta função é muito semelhante a função intercale_seqs().
    Alguns __possíveis__ passos...
       * CRIE uma lista auxiliar de tamanho n = d-e.
       * INTERCALE as sublistas seq[e:m] e seq[m:d] de seq[e:d] e armazene o resultado
         desta intercalação na lista auxiliar.
       * COPIE o conteúdo da lista auxiliar para seq[e:d].

    '''

Aqui vão alguns exemplos de execução da função.

    In [2]: seq = [7, 11, 56, 5, 7, 99, 104 ]
    In [3]: intercale( seq, 0, 3, 7) # retorna None
    In [4]: seq
    Out[4]: [5, 7, 7, 11, 56, 99, 104]

    In [5]: seq = [7,  11, 56, 5, 7, 99, -1]
    In [6]: intercale(seq, 1, 3, 6) # seq[1:3] = [11, 56] e seq [3:6] = [5, 7, 99]
    In [7]: seq # seq[1:6] crescente
    Out[7]: [7, 5, 7, 11, 56, 99, -1]

    In [8]: seq = [0, 1, 2, 3, 7, 11, 56, 5, 7, 99, 104]
    In [9]: intercale(seq, 4, 7, 11) # seq[4:7] = [7, 11, 56] seq[7:11] = [5, 7, 99, 104]
    In [10]: seq # seq[4:11] crescente
    Out[10]: [0, 1, 2, 3, 5, 7, 7, 11, 56, 99, 104]

    In [11]: seq = [99, 99, 99, 99, 7, 11, 56, 5, 7, 59, -1]
    In [12]: intercale(seq, 4, 7, 11) # seq[4:7] = [7, 11, 56] seq[7:10] = [5, 7, 59]
    In [13]: seq # seq[4:10] crescente
    Out[13]: [99, 99, 99, 99, 5, 7, 7, 11, 56, 59, -1]

Antes de continuar…

Qual o consumo de tempo da sua função intercale(seq, e, m, d) no melhor caso (= a função trabalha pouco) e no pior caso (= a função se mata de trabalhar) supondo que n=d-e? É O(1)? É O(lg n)? É O(n)? É O(nlg n)? É O(n2)? É O(n3)? É O(2n)? É O(?)?

Qual é aproximadamente a quantidade de espaço extra usado pela função intercale(seq, e, m, d) supondo que n=d-e? Considerem que a quantidade de espaço extra é o número de variáveis que sua função usa como rascunho para fazer o serviço e que são descartadas ao final. Cada posição em uma lista deve ser contada como uma variável.

Mais adiante vocês confrontarão essas conclusões com as realidades dos experimentos.
ordene_por_intercalacaoR(seq, e, d)

Fonte: Merge sort (Wikipedia).

A especificação da função ordene_por_intercalacaoR(seq, e, d) está logo abaixo. A função se apoia com todas suas forças no pensamento recursivo e na colaboração indispensável da função intercale(seq, e, m, d)! Busquem inspiração na busca binária e nas imagens e animações nesta página.

def ordene_por_intercalacaoR(seq, e, d):
'''(list, int, int) -> None
RECEBE uma lista seq e índice e e d.
REARRANJA os elementos de seq[e: d] para que fiquem em ordem crescente.
'''

Alguns exemplos… Aquelas e aqueles que puderem, prestem atenção na cores dos elementos.

    In [46]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [47]: ordene_por_intercalacaoR(seq, 0, 5)
    In [48]: seq
    Out[48]: [-1, 7, 17, 58, 99, 11, 56, 5, 7, 59, -1]
    In [48]: seq
    Out[48]: [-1, 7, 17, 58, 99, 11, 56, 5, 7, 59, -1]
    In [49]: ordene_por_intercalacaoR(seq, 5, 11)
    In [50]: seq
    Out[50]: [-1, 7, 17, 58, 99, -1, 5, 7, 11, 56, 59]

    In [51]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [52]: ordene_por_intercalacaoR(seq, 0, 6)
    In [53]: seq
    Out[53]: [-1, 7, 11, 17, 58, 99, 56, 5, 7, 59, -1]
    In [53]: seq
    Out[53]: [-1, 7, 11, 17, 58, 99, 56, 5, 7, 59, -1]
    In [54]: ordene_por_intercalacaoR(seq, 6, 11)
    In [55]: seq
    Out[55]: [-1, 7, 11, 17, 58, 99, -1, 5, 7, 56, 59]

Ordenação por intercalação

No arquivo eg_intercalacao.py vocês encontram duas funções totalmente implementadas:

    ordene_por_intercalacao(): é um invólucro para a função ordene_por_intercalacaoR()
    ordene_por_intercalacaoI(): é uma versão iterativa da ordenação por intercalação.

Essas funções são conhecidas por ai pelo nome de Mergesort.
Análise experimental

Agora vocês devem deixar as funções trabalharem em paz, apreciar a vista e observarem atentamente o que estão vendo.

Baixem o arquivo experimento.py. Este arquivo fará experimentos com as funções:

    ordene_por_insercao(), feita na semana passada;
    ordene_por_intercalacao(),
    ordene_por_intercalacaoI().

Baseado nesses experimentos, qual função teve o melhor desempenho para listas

    aleatórias?
    em ordem crescente ou quase crescente?
    em ordem decrescente ou quase decrescente?

Mais um pouco de reflexão

Algumas questões para discutirem.

Baseados nas suas análises para o consumo de tempo da função intercale(), qual é o consumo de tempo de ordene_por_intercalacao() no melhor caso e no pior caso para ordenar uma lista seq com n elementos? É O(1)? É O(lg n)? É O(n)? É O(nlg n)? É O(n2)? É O(n3)? É O(2n)?.

Os tempos obtidos nos experimentos comprovam a suas conclusões sobre o consumo de tempo? Por quê?
Lições

Note que no mergesort, após uma sublista ser produzida através da intercalação de duas outras, não haverá mais comparações entre pares de elementos nesta sublista. Todo o trabalho será feito comparando-se elementos entre sublistas separadas. A função intercale() é especializada neste tipo de serviço.

A maior lição de hoje é uma ideia genial chamada de divisão e conquista ou conquista por divisão ou Divide-and-conquer algorithm ou sei lá o que. Esse mesmo arcabouço é usado por ai por uma grande variedade funções que resolvem os mais diversos problemas!

Um pouco mais adiante neste EG há uma pequena discussão sobre a versão iterativa do mergesort. Vocês podem ler mais sobre o Mergesort aqui.

Ideias?
Para conseguir um bônus …

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time.

Você só precisa entregar o arquivo com extensão eg\_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link está no início deste EG.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
Mergesort recursivo

Mergesort: versão recursiva

A função ordene_por_intercalacao() é apenas um envoltório para a função ordene_por_intercalacaoR(). O conjunto da obra é uma versão recursiva do Mergesort, também conhecida como implementação top-down.

def ordene_por_intercalacao(seq):
'''(list) -> None
RECEBE uma lista seq.
REARRANJA os elementos de seq para que fiquem em ordem crescente.

    NOTA: É um invólucro para ordene_por_intercalacaoR().
    '''
    n = len(seq)
    ordene_por_intercalacaoR(seq, 0, n)

Exemplos…

    In [2]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [3]: ordene_por_intercalacao(seq)
    In [4]: seq
    Out[4]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

    In [11]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
    In [12]: ordene_por_intercalacao(seq)
    In [13]: seq
    Out[13]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']

Mergesort iterativo

Mergesort: versão iterativa

A função ordene_por_intercalacaoI() é uma versão iterativa do Mergesort, também chamada de implementação bottom-up.

O Mergesort iterativo é divido em fases. No início de cada fase tem-se que a lista está dividida/particionada em sublistas ordenadas, cada uma das quais com b elementos. No início da primeira fase b = 1. Em cada fase a função percorre a lista do seu início ao fim intercalando pares de sublistas ordenadas vizinhas com b elementos. Ao final de uma fase tem-se que a lista está particionada em sublistas ordenadas de 2 × b elementos, com excessao feita, possivelmente, a sublista do final da lista. Desta forma a próxima fase pode ser iniciada com 2 × b no papel do novo tamanho b das sublistas ordenadas.

    No início 1o. fase a lista está dividida em sublistas ordenadas com b = 1 elemento.
    No início 2o. fase a lista está dividida em sublistas ordenadas com b = 2 elementos.
    No início 3o. fase a lista está dividida em sublistas ordenadas com b = 4 elementos.
    No início 4o. fase a lista está dividida em sublistas ordenadas com b = 8 elementos.

Em geral, na fase i, cada sublistas tem 2i − 1 elementos. A função para no início da fase t em que b = 2t − 1 é maior ou igual ao número de elementos da lista.

Hmm. Qual o número de fases necessárias para se ordenar uma lista com n elementos?

Aqui vai uma pequena simulação…

     +----+----+----+----+----+----+----+----+----+
     | 55 | 33 | 66 | 44 | 99 | 11 | 77 | 22 | 88 |  b = 1
     +----+----+----+----+----+----+----+----+----+
       e    m    d
                 e    m    d
                           e    m    d
                                     e    m    d
                                               e    m    d # faz nada

     +----+----+----+----+----+----+----+----+----+
     | 33 | 55 | 44 | 66 | 11 | 99 | 22 | 77 | 88 |  b = 2
     +----+----+----+----+----+----+----+----+----+
       e         m         d
                           e         m         d
                                               e    faz nada

     +----+----+----+----+----+----+----+----+----+
     | 33 | 44 | 55 | 66 | 11 | 22 | 77 | 99 | 88 |  b = 4
     +----+----+----+----+----+----+----+----+----+
       e                   m                   d

     +----+----+----+----+----+----+----+----+----+
     | 11 | 22 | 33 | 44 | 55 | 66 | 77 | 99 | 88 |  b = 8
     +----+----+----+----+----+----+----+----+----+
       e                   m                   d
                                               e    faz nada

     +----+----+----+----+----+----+----+----+----+
     | 11 | 22 | 33 | 44 | 55 | 66 | 77 | 88 | 99 |  b = 16
     +----+----+----+----+----+----+----+----+----+
       e                                       m    d


Arquivos requeridos
eg_intercalacao.py

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
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    print("Testes do EG22 - ordenação por intercalação")

    # escreva seus testes

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2): # EI
    ''' (list, list) -> list

    RECEBE seq1 e seq2, duas listas tal que:

        - seq1 é crescente com n1 >= 0 elementos e
        - seq2 é crescente com n2 >= 0 elementos

    RETORNA uma lista com n1+n2 elementos, contendo
    os elementos de seq1 e seq2 em ordem crescente.

    EXEMPLO para

        seq1 = [7, 11, 56] e
        seq2 = [-5, 7, 99, 104]

    a função deve retornar a lista:

        [-5, 7, 7, 11, 56, 99, 104]
    '''
    # escreva sua solução

## ------------------------------------------------------------------

def intercale(seq, e, m, d): # EG: DESAFIO
    ''' (list, int, int, int) -> None

    RECEBE uma lista seq e índices e, m e d tais que os elementos de

        - seq[e:m] estão em ordem crescente e
        - seq[m:d] estão em ordem crescente

    REARRANJA os elementos de seq[e:d] para que fiquem em ordem crescente.

    SUGESTÃO: Em busca de inspiração?
    Esta função é muito semelhante a função intercale_seqs().
    Alguns __possíveis__ passos...
       * CRIE uma lista auxiliar de tamanho n = d-e.
       * INTERCALE as sublistas seq[e:m] e seq[m:d] de seq[e:d] e armazene o resultado
         desta intercalação na lista auxiliar.
       * COPIE o conteúdo da lista auxiliar para seq[e:d].

    EXEMPLOS

    In [2]: seq = [7, 11, 56, 5, 7, 99, 104]
    In [3]: intercale( seq, 0, 3, 7) # retorna None
    In [4]: seq
    Out[4]: [5, 7, 7, 11, 56, 99, 104]

    In [5]: seq = [7, 11, 56, 5, 7, 99, -1]
    In [6]: intercale(seq, 1, 3, 6) # seq[1:3] = [11, 56] e seq [3:6] = [5, 7, 99]
    In [7]: seq # seq[1:6] crescente
    Out[7]: [7, 5, 7, 11, 56, 99, -1]

    In [8]: seq = [0, 1, 2, 3, 7, 11, 56, 5, 7, 99, 104]
    In [9]: intercale(seq, 4, 7, 11) # seq[4:7] = [7, 11, 56] seq[7:11] = [5, 7, 99, 104]
    In [10]: seq # seq[4:11] crescente
    Out[10]: [0, 1, 2, 3, 5, 7, 7, 11, 56, 99, 104]

    In [11]: seq = [99, 99, 99, 99, 7, 11, 56, 5, 7, 59, -1]
    In [12]: intercale(seq, 4, 7, 11) # seq[4:7] = [7, 11, 56] seq[7:10] = [5, 7, 99]
    In [13]: seq # seq[4:10] crescente
    Out[13]: [99, 99, 99, 99, 5, 7, 7, 11, 56, 59, -1]
    '''
    # escreva sua solução


## ------------------------------------------------------------------

def ordene_por_intercalacao(seq):
    '''(list) -> None
    RECEBE uma lista seq.
    REARRANJA os elementos de seq para que fiquem em ordem crescente.

    NOTA: É um invólucro para ordene_por_intercalacaoR().

    EXEMPLOS

    In [2]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [3]: ordene_por_intercalacao(seq)
    In [4]: seq
    Out[4]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

    In [11]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
    In [12]: ordene_por_intercalacao(seq)
    In [13]: seq
    Out[13]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']
    '''
    n = len(seq)
    ordene_por_intercalacaoR(seq, 0, n)

## ------------------------------------------------------------------

def ordene_por_intercalacaoR(seq, e, d): # EG: DESAFIO
    '''(list, int, int) -> None
    RECEBE uma lista seq e índice e e d.
    REARRANJA os elementos de seq[e: d] para que fiquem em ordem crescente.

    Esta função deve ser RECURSIVA e deve se APOIAR na função intercale(seq, e, m, d).
    Busque inspiração na busca binária e nas animações na página do EG.

    EXEMPLOS

    In [46]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [47]: ordene_por_intercalacaoR(seq, 0, 5)
    In [48]: seq
    Out[48]: [-1, 7, 17, 58, 99, 11, 56, 5, 7, 59, -1]
    In [49]: ordene_por_intercalacaoR(seq, 5, 11)
    In [50]: seq
    Out[50]: [-1, 7, 17, 58, 99, -1, 5, 7, 11, 56, 59]

    In [51]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [52]: ordene_por_intercalacaoR(seq, 0, 6)
    In [53]: seq
    Out[53]: [-1, 7, 11, 17, 58, 99, 56, 5, 7, 59, -1]
    In [54]: ordene_por_intercalacaoR(seq, 6, 11)
    In [55]: seq
    Out[55]: [-1, 7, 11, 17, 58, 99, -1, 5, 7, 56, 59]
    '''
    # escreva sua solução

## ------------------------------------------------------------------

def ordene_por_intercalacaoI(seq):
    '''(list) -> None
    RECEBE uma lista seq.
    REARRANJA os elementos de seq para que fiquem em ordem crescente.

    É uma função ITERATIVA que se APOIA na função intercale(seq, e, m, d).
    Para entender o seu funcionamente pode ser útil ver as animações
    e simulação na página do EG.

    EXEMPLOS

    In [34]: seq = [99, 58, 17, -1, 7, 11, 56, 5, 7, 59, -1]
    In [35]: ordene_por_intercalacaoI(seq)
    In [36]: seq
    Out[36]: [-1, -1, 5, 7, 7, 11, 17, 56, 58, 59, 99]

    In [37]: seq = ['como', 'é', 'muito', 'bom', 'estudar', 'mac0122!']
    In [38]: ordene_por_intercalacaoI(seq)
    In [39]: seq
    Out[39]: ['bom', 'como', 'estudar', 'mac0122!', 'muito', 'é']
    '''
    n = len(seq)
    b = 1 # tamanho dos pares de blocos a serem intercalados
    while b < n:
        e = 0
        while e + b < n:
            d = e + 2*b
            if d > n: d = n
            intercale(seq, e, e+b, d)
            e = d
        b = 2*b # dobre o tamanho dos blocos

## ------------------------------------------------------------------

def ordene_por_insercao(seq):
    ''' (list) -> None

    RECEBE uma lista seq.
    REARRANJA os elementos da lista de tal forma que fiquem em
        ordem crescente.

    Esta função se apoio na função insira_ultimo.
    '''
    n= len(seq)
    for fim in range(2, n+1):
        insira_ultimo(seq, fim)

## ------------------------------------------------------------------

def insira_ultimo(seq, n):
    ''' (list, int) -> None

    RECEBE uma lista seq e um inteiro n tais que os elementos da
         sublista seq[0:n-1] estão em ordem crescente.
    REARRANJA os elementos da lista seq de tal forma que os
         elementos da sublista seq[0:n] estejam em ordem crescente.

    Essa função é o coração do algoritmo de ordenação
    por inserção.
    '''
    i = n-1
    while i > 0 and seq[i] < seq[i-1]:
        seq[i], seq[i-1] = seq[i-1], seq[i]
        i -= 1

#--------------------------------------------
if __name__ == '__main__':
    main()
```
