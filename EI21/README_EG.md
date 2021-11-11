EG21
Data de entrega: quinta, 11 nov 2021, 13:00
Arquivos requeridos: eg_borbulhagem.py ( Baixar)
Tipo de trabalho: Trabalho individual

mais bolhinhas, mais bolhas e mais bolhonas

Fonte: Travel bubbles.
Preparação padrão

Volte a sala principal caso você esteja sozinhE.

Preencha o Formulário Individual conforme as instruções.

Faça uma cópia do seu EI, colocando o prefixo eg\_. Vamos chamar esse arquivo de EG. Se desejarem vocês podem baixar desta página o arquivo eg_borbulhagem.py com o esqueleto deste exercício. O programa experimento.py que usaremos para fazermos uma análise experimental das funções desenvolvidas pode ser baixado daqui.

Escolham a pessoa estagiária e a pessoa gerente conforme as instruções.

Sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.

Se tiverem alguma dúvida chamem o Hitoshi ou o Coelho. Eles devem estar passeando nas salas.
EI: ordenação por borbulhamento

Fonte: Bubble sort (Wikipedia).
Testes

Testem as funções que vocês fizeram para o EI:

    borbulhe(seq, n) e
    ordene_por_borbulhagem(seq)

Usem para isso uma coletânea dos testes que cada uma/um fez na função main().

A pessoa estagiária deve colocar os testes na main() do time e compartilhar esse EG com as demais pessoas do time para que todos possam testar os seus trabalhos individuais.

A propósito, a função ordene_por_borbulhagem(seq) é conhecida nas redes sociais como Bubble sort.
Testes individuais

Cada pessoa do time deve verificar as funções do seu EI/EG estão dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.

Caso algum problema seja encontrado, discuta com suas/seus colegas de time para resolvê-lo. Elas/eles ficarão muito felizes em lhe ajudar.
Reflexão

Algumas questões para discutirem.

Qual o número de trocas e comparações entre pares vizinhos são feitas por ordene_por_borbulagem() para ordenar a lista

    [1, 2, 3, 4, 5]?
    [5, 4, 3, 2, 1]?
    [1, 3, 2, 4, 5]?

Em geral, se uma lista seq tem n elementos, qual é o consumo de tempo de ordene_por_borbulagem(seq) no melhor caso (= a função trabalha pouco) e no pior caso (= a função se mata de trabalhar)? O(1)?, O(lg n), O(nlg n), O(n2)? O(n3)? O(2n)?.
Desafio: mais ordenação por borbulhagem

Fonte: Category:Bubble sort (Wikipedia).

Agora vocês vão desenvolver uma versão X das funções que fizeram. O objetivo e desenvolver funções

    borbulheX(seq, n) e
    ordene_por_borbulhagemX(seq)

que possivelmente/provavelmente façam menos comparações entre seu elementos. A ideia básica é que se sabemos que a ≤ b e que b ≤ c, então não precisamos comparar a e c para concluirmos que a ≤ c. Essa ideia já foi usada em ordenação por inserção e ordenação por inserção binária para evitar comparações supérfluas. Ela será usada de formas mais sofisticadas na próxima semana. Fiquem ligada(o)s!

Tratemos uma função por vez.
borbulheX()

A função borbulhagemX(seq,n) é semelhante a função borbulhagem(seq,n). A diferenção crucial é que ela retorna ainda um indice u tal que os elementos da sublista de seq[u:] já estão nas suas posições de direito na lista ordenada. Observar a animação acima pode ser esclarecedor.

A especifição da função está abaixo

def borbulheX(seq, n):
'''(list, int) -> int, int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso deve
    ser da posição de índice 0 até a posição de índice n.

    Durante o percurso a função COMPARA todos os pares de valores
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5] e
    seq[6] e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

    Se os valores comparados não estiverem em ordem crescente, eles devem ser
    TROCADOS de posições.

    RETORNA o número de trocas E o maior índice de uma posição de seq
    que foi alterada durante o percurso.

    Se nenhum posição de seq foi alterada a função deve retorna o par (0, 0).

Aqui estão alguns exemplos de execução da função.

    In [4]: seq = [7, 4, 11, 5, 3]
    In [5]: t, u = borbulheX(seq, 3)
    In [6]: t # trocas
    Out[6]: 1
    In [7]: u # índice
    Out[7]: 1
    In [8]: seq
    Out[8]: [4, 7, 11, 5, 3]

    In [9]: seq = [7, 4, 11, 5, 3]
    In [10]: t, u = borbulheX(seq, 4)
    In [11]: t # trocas
    Out[11]: 2
    In [12]: u # índice
    Out[12]: 3
    In [13]: seq
    Out[13]: [4, 7, 5, 11, 3]

    In [18]: seq = [7, 4, 11, 5, 3]
    In [19]: t, u = borbulheX(seq, 5)
    In [20]: t # trocas
    Out[20]: 3
    In [21]: u # índice
    Out[21]: 4
    In [22]: seq
    Out[22]: [4, 7, 5, 3, 11]

ordene_por_borbulhagemX(seq)

A especificação desta função também é muito semelhante a da função sua irmazinha que não tem o X no nome. Além do número de trocas, a função também retorna o número de comparações entre posições vizinhas realizadas durante toda a ordenação.

def ordene_por_borbulhagemX(seq):
'''(list) -> int, int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem ordenados.

    Esta função DEVE APLICAR repetidas vezes a função borbulheX() sobre a
    lista seq até que seq esteja ordenada.

    RETORNA o número total de trocas __e__ o número total de
    comparações realizadas durante a ordenação.

    Hmm. Como podemos utilizar os valores retornados por borbulheX() e
    o parâmetro n para _possivelmente_ evitarmos comparações
    desnecessárias entre posições vizinhas de seq?

    SUGESTÃO. Busquem inspiração examinando o comportamento da função
    ordene_por_borbulhagem().
    '''

Aqui vão alguns exemplos.

    In [24]: seq = [7, 4, 11, 5, 3]
    In [25]: t, c = ordene_por_borbulhagemX(seq)
    In [26]: t # trocas
    Out[26]: 7
    In [27]: c # comparações
    Out[27]: 10
    In [28]: seq
    Out[28]: [3, 4, 5, 7, 11]

    In [29]: seq = [5, 3, 11, 4, 7]
    In [30]: t, c = ordene_por_borbulhagemX(seq)
    In [31]: t # trocas
    Out[31]: 4
    In [32]: c # comparações
    Out[32]: 8
    In [33]: seq
    Out[33]: [3, 4, 5, 7, 11]

    In [34]: seq = [5, 3, 4, 7, 11]
    In [35]: t, c = ordene_por_borbulhagemX(seq)
    In [36]: t # trocas
    Out[36]: 2
    In [37]: c # comparações
    Out[37]: 5
    In [38]: seq
    Out[38]: [3, 4, 5, 7, 11]

Mais reflexão

Algumas questões para discutirem.

Qual o número de trocas e comparações entre pares vizinhos são feitas por ordene_por_borbulagem() para ordenar a lista

    [1, 2, 3, 4, 5]?
    [5, 4, 3, 2, 1]?
    [1, 3, 2, 4, 5]?

É claro que vocês podem usar a própria função ordene_por_borbulagemX() para obter esses número.

Em geral, se uma lista seq tem n elementos, qual é o consumo de tempo de ordene_por_borbulagemX() no melhor caso (= a função trabalha pouco) e no pior caso (= a função se mata de trabalhar)? O(1)?, O(lg n), O(nlg n), O(n2)? O(n3)? O(2n)?.
Análise experimental

Baixe o arquivo experimento.py. Modifique a constante PARES_DE_FUNCOES do arquivo para comparar o consumo de tempo das funções ordene_por_borbulhagem e ordene_por_borbulhagemX. Qual função tem o melhor desempenho para listas

    aleatórias?
    em ordem crescente ou quase crescente?
    em ordem decrescente ou quase decrescente?

Ainda mais ordenação por borbulhagem

Fonte: Cocktail shaker sort (Wikipedia).

Bem, se vocês ainda tem tempo … a situação ficará agora mais interessante. Aplicaremos a ideia do desafio 1 em dose dupla percorrendo a lista da esquerda para a direita e da direita para a esquerda como sugere a animação acima.

No arquivo eg_borbulhagem.py vocês encontram as seguintes funções totalmente implementadas

    borbulhe_de_luxe(seq, ini, fim, passo) e
    ordene_por_borbulhagem_de_luxe(seq)

A função ordene_por_borbulhagem_de_luxe(seq) é chamada nas redes sociais de Shaker sort. A animação acima ilustra o seu comportamento.

Como pode ser visto, a função borbulhe() na sua versão de_luxe ganhou mais alguns parâmetros.

    ini e fim indicam a parte relavente da lista e
    passo diz a direção que a lista será percorrida.

Notem que borbulhe_de_luxe(seq, 0, n, 1) faz o mesmo serviço que borbubleX(seq, n).
Mais análise experimental

Baixe o arquivo experimento.py. Modifique a constante PARES_DE_FUNCOES do arquivo para comparar os consumo de tempo de duas dentre as funções

    ordene_por_borbulhagem o Bubble sort,
    ordene_por_borbulhagemX e
    ordene_por_borbulhagem_de_luxe o Shaker sort

Mais reflexão ainda

Qual das funções tem o melhor desempenho para listas

    aleatórias?
    em ordem crescente ou quase crescente?
    em ordem decrescente ou quase decrescente?

Ideias?
Lições

Para evitar comparações desnecessárias as funções feitas utilizaram algumas ideias.

    a contagem do número de trocas faz com a ordenação pare assim que a lista está ordenada.
    ao retornar o índice da última troca as funções da família borbulhe() nos dizem que a partir daquele índice não há mais nada a ser feito

É claro é que toda essa contabilidade vem com um custo. Boas intenções podem produzir, para alguns casos, funções mais lentas.

Todo problema tem o direito de ficar calado. Se o problema abrir mão desse direito, toda e qualquer informação que ele nos der pode e será usada para resolvê-lo de forma mais efeiciente.
Para conseguir um bônus …

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time.

Você só precisa entregar o arquivo com extensão eg\_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
Arquivos requeridos
eg_borbulhagem.py

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
    '''
    print("Testes do EI21 - ordenação por borbulhagem")

## ==================================================================

def borbulhe(seq, n):
    ''' (list, int) -> int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso
    deve ser da posição de índice 0 até a posição de índice n.

    Durante o percurso a função COMPARA todos os pares de valores
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5] e seq[6]
    e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

    Se os valores comparados não estiverem em ordem crescente, eles devem ser
    TROCADOS de posições. Por exemplo, para

        seq = [w, x, y, 7, 5, z]

    a comparação de seq[3]=7 e seq[4]=5 deve resultar na troca de seus valores.
    A lista deve ser modificada de tal forma que tenhamos

        seq = [w, x, y, 5, 7, z],

    em que os valores w, x, y e z são irrelevantes.

    RETORNA o número de trocas realizadas durante o percurso.

    Esta função será o coração de mais um algoritmo de ordenação que nos
    apresentará novas ideias.

    EXEMPLOS:

    In [24]: seq = [7, 4, 11, 5, 3]
    In [25]: t = borbulhe(seq, 3)
    In [26]: t
    Out[26]: 1
    In [27]: seq
    Out[27]: [4, 7, 11, 5, 3]

    In [28]: seq = [7, 4, 11, 5, 3]
    In [29]: t = borbulhe(seq, 4)
    In [30]: t
    Out[30]: 2
    In [31]: seq
    Out[31]: [4, 7, 5, 11, 3]

    In [32]: seq = [7, 4, 11, 5, 3]
    In [33]: t = borbulhe(seq, 5)
    In [34]: t
    Out[34]: 3
    In [35]: seq
    Out[35]: [4, 7, 5, 3, 11]

    SUGESTÃO: não use listas auxiliares como fatias. Basta
    percorrer seq, comparar pares vizinhos e trocar quando
    necessário.
    '''
    print("Vixe! Ainda não fiz a função borbulhe()...")

## ==================================================================

def ordene_por_borbulhagem(seq):
    ''' (list) -> int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem ordenados.

    Esta função DEVE APLICAR repetidas vezes a função borbulhe() sobre a
    lista seq até que seq esteja ordenada.

    RETORNA o número total de trocas realizadas durante a ordenação.

    Cada vez que a função borbulhe() é aplicada sobre a lista seq, os elementos
    da lista ficam mais próximos de seus lugares na lista ordenada.

    EXEMPLO. Suponha que seq = [7, 4, 11, 5, 3].
    Após aplicarmos borbulhe() sobre a lista seq na

        * primeira vez, obtemos seq=[4, 7, 5, 3, 11], com 3 trocas
        * segunda  vez, obtemos seq=[4, 5, 3, 7, 11], mais 2 trocas
        * terceira vez, obtemos seq=[4, 3, 5, 7, 11], mais 1 troca
        * quarta   vez, obtemos seq=[3, 4, 5, 7, 11], mais 1 troca

    Pronto! A lista seq está ordenada.
    Para seq = [7, 4, 11, 5, 3] a função deve retornar 7.
    '''
    print("Vixe! Ainda não fiz a função ordene_por_borbulhagem()...")

## ==================================================================

def borbulheX(seq, n):
    '''(list, int) -> int, int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso deve
    ser da posição de índice 0 até a posição de índice n.

    Durante o percurso a função COMPARA todos os pares de valores
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5] e
    seq[6] e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

    Se os valores comparados não estiverem em ordem crescente, eles devem ser
    TROCADOS de posições.

    RETORNA o número de trocas E o maior índice de uma posição de seq
    que foi alterada durante o percurso.

    Se nenhum posição de seq foi alterada a função deve retorna o par (0, 0).

    EXEMPLOS:

    In [4]: seq = [7, 4, 11, 5, 3]
    In [5]: t, u = borbulheX(seq, 3)
    In [6]: t # trocas
    Out[6]: 1
    In [7]: u # índice
    Out[7]: 1
    In [8]: seq
    Out[8]: [4, 7, 11, 5, 3]

    In [9]: seq = [7, 4, 11, 5, 3]
    In [10]: t, u = borbulheX(seq, 4)
    In [11]: t # trocas
    Out[11]: 2
    In [12]: u # índice
    Out[12]: 3
    In [13]: seq
    Out[13]: [4, 7, 5, 11, 3]

    In [18]: seq = [7, 4, 11, 5, 3]
    In [19]: t, u = borbulheX(seq, 5)
    In [20]: t # trocas
    Out[20]: 3
    In [21]: u # índice
    Out[21]: 4
    In [22]: seq
    Out[22]: [4, 7, 5, 3, 11]

    '''
    print("Vixe! Ainda não fiz a função borbulheX()...")

## ==================================================================

def ordene_por_borbulhagemX(seq):
    '''(list) -> int, int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem ordenados.

    Esta função DEVE APLICAR repetidas vezes a função borbulheX() sobre a
    lista seq até que seq esteja ordenada.

    RETORNA o número total de trocas __e__ o número total de
    comparações realizadas durante a ordenação.

    Hmm. Como podemos utilizar os valores retornados por borbulheX() e
    o parâmetro n para _possivelmente_ evitarmos comparações
    desnecessárias entre posições vizinhas de seq?

    SUGESTÃO. Busquem inspiração examinando o comportamento da função
    ordene_por_borbulhagem().

    EXEMPLOS:

    In [24]: seq = [7, 4, 11, 5, 3]
    In [25]: t, c = ordene_por_borbulhagemX(seq)
    In [26]: t # trocas
    Out[26]: 7
    In [27]: c # comparações
    Out[27]: 10
    In [28]: seq
    Out[28]: [3, 4, 5, 7, 11]

    In [29]: seq = [5, 3, 11, 4, 7]
    In [30]: t, c = ordene_por_borbulhagemX(seq)
    In [31]: t # trocas
    Out[31]: 4
    In [32]: c # comparações
    Out[32]: 8
    In [33]: seq
    Out[33]: [3, 4, 5, 7, 11]

    In [34]: seq = [5, 3, 4, 7, 11]
    In [35]: t, c = ordene_por_borbulhagemX(seq)
    In [36]: t # trocas
    Out[36]: 2
    In [37]: c # comparações
    Out[37]: 5
    In [38]: seq
    Out[38]: [3, 4, 5, 7, 11]

    '''
    print("Vixe! Ainda não fiz a função ordene_por_borbulhagemX()...")

## ==================================================================

def borbulhe_de_luxe(seq, ini, fim, passo):
    '''(list, int, ini, init) -> int, int

    RECEBE uma lista seq e três inteiros ini e fim e passo em que
    ini <= fim e passo é +1 ou -1.

    A função deve PERCORRER sequencialmente a lista seq. Se passo é +1
    o percurso deve ser da posição de índice ini até a posição de
    índice fim. Já se passo é -1 o percurso deve ser da posição de
    índice fim-1 até a posição de índice ini.

    Durante o percurso a função COMPARA todos os pares de valores em
    posições vizinhas seq[i] e seq[i-1] para todo i, ini < i < fim.

    Se os valores comparados não estiverem em ordem crescente, eles devem
    ser TROCADOS de posições.

    RETORNA o número de trocas E o índice de uma posição de seq que foi
    alterada durante o percurso. Se passo é +1 o índice deve ser o maior
    dentre os alterados e se passo é -1 o índice deve ser o menor.

    Se nenhum posição de seq foi alterada a função retorna o par (0, ini)
    se passo é +1 e retorna o par (0, fim) se passo é -1.

    SUGESTÃO. Busquem inspiração na função borbulheX(). Notem que
    borbulhe_de_luxe(seq, 0, n, 1) faz o mesmo serviço que borbubleX(seq, n) e
    a partir dessa observação escrevam borbulhe_de_luxe().

    EXEMPLOS:
    In [7]: seq = [7, 4, 11, 5, 3]
    In [8]: t, u = borbulhe_de_luxe(seq, ini=0, fim=3, passo=1) # vai para direita
    In [9]: t # trocas
    Out[9]: 1
    In [10]: u # maior índice de posição alterada
    Out[10]: 1
    In [11]: seq
    Out[11]: [4, 7, 11, 5, 3]

    In [13]: seq = [7, 4, 11, 5, 3]
    In [14]: t, u = borbulhe_de_luxe(seq, ini=0, fim=4, passo=1) # vai para direita
    In [15]: t # trocas
    Out[15]: 2
    In [16]: u # maior índice de posição alterada
    Out[16]: 3
    In [17]: seq
    Out[17]: [4, 7, 5, 11, 3]

    In [18]: seq = [7, 4, 11, 5, 3]
    In [19]: t, u = borbulhe_de_luxe(seq, ini=0, fim=5, passo=1) # vai para direita
    In [20]: t # trocas
    Out[20]: 3
    In [21]: u # maior índice de posição alterada
    Out[21]: 4
    In [22]: seq
    Out[22]: [4, 7, 5, 3, 11]

    In [23]: seq = [7, 4, 11, 5, 3]
    In [24]: t, u = borbulhe_de_luxe(seq, ini=0, fim=3, passo=-1) # vai para esquerda
    In [25]: t # trocas
    Out[25]: 1
    In [26]: u # menor índice de posição alterada
    Out[26]: 0
    In [27]: seq
    Out[27]: [4, 7, 11, 5, 3]

    In [32]: seq = [7, 4, 11, 5, 3]
    In [33]: t, u = borbulhe_de_luxe(seq, ini=0, fim=5, passo=-1) # vai para esquerda
    In [34]: t # trocas
    Out[34]: 4
    In [35]: u # menor índice de posição alterada
    Out[35]: 0
    In [36]: seq
    Out[36]: [3, 7, 4, 11, 5]

    In [37]: seq = [7, 4, 11, 5, 3]
    In [38]: t, u = borbulhe_de_luxe(seq, ini=1, fim=5, passo=-1) # vai para esquerda
    In [39]: t # trocas
    Out[39]: 3
    In [40]: u
    Out[40]: 1
    In [41]: seq
    Out[41]: [7, 3, 4, 11, 5]
    '''
    trocas = 0
    ult    = 0
    if passo == -1: ini, fim = fim-2, ini
    for i in range(ini+1, fim, passo):
        if seq[i] < seq[i-1]:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            trocas += 1
            ult = i
    if passo == -1: ult -= 1
    return trocas, ult

## ==================================================================

def ordene_por_borbulhagem_de_luxe(seq):
    '''(list) -> int, int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem em ordenados.

    Esta função deve aplicar repetidas vezes a função
    borbulhe_de_luxe() sobre a lista seq até que esta esteja ordenada.

    RETORNA o número total de trocas __e__ o número total de comparações realizadas
    durante a ordenação.

    Hmm. Como podemos utilizar os valores retornados por borbulhe_de_luxe() e os
    parâmetros extras ini, fim e passo para possivelmente evitarmos comparações
    desnecessárias entre posições vizinhas de seq?

    SUGESTÃO. Procurem inspiração na função ordene_por_borbulhagemX().

    EXEMPLOS:
    In [41]: seq = [7, 4, 11, 5, 3]
    In [42]: t, c = ordene_por_borbulhagem_de_luxe(seq)
    In [43]: t
    Out[43]: 7
    In [44]: c
    Out[44]: 12
    In [45]: seq
    Out[45]: [3, 4, 5, 7, 11]

    In [46]: seq = [5, 3, 11, 4, 7]
    In [47]: t, c = ordene_por_borbulhagem_de_luxe(seq)
    In [48]: t
    Out[48]: 4
    In [49]: c
    Out[49]: 8
    In [50]: seq
    Out[50]: [3, 4, 5, 7, 11]

    In [51]: seq = [5, 3, 4, 7, 11]
    In [52]: t, c = ordene_por_borbulhagem_de_luxe(seq)
    In [53]: t
    Out[53]: 2
    In [54]: c
    Out[54]: 6
    In [55]: seq
    Out[55]: [3, 4, 5, 7, 11]

    In [65]: seq = [7, 1, 5, 2, 9, 6, 0, 4, 3, 8]
    In [66]: a = seq[:] # a é clone de seq
    In [67]: b = seq[:] # b é clone de seq
    In [68]: t, c = ordene_por_borbulhagemX(a)
    In [69]: t # trocas
    Out[69]: 22
    In [70]: c # comparações
    Out[70]: 35

    In [71]: t, c = ordene_por_borbulhagem_de_luxe(b)
    In [72]: t
    Out[72]: 22
    In [73]: c # comparações
    Out[73]: 32
    In [74]: a
    Out[74]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [75]: b
    Out[75]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
    total_trocas = 0
    total_cmps   = 0
    ini = 0
    fim = len(seq)
    passo = 1
    while fim > ini+1:
        total_cmps += fim - ini - 1
        trocas, ult = borbulhe_de_luxe(seq, ini, fim, passo)
        total_trocas += trocas
        if passo == 1: fim = ult
        else: ini = ult+1
        passo *= -1
    return total_trocas, total_cmps

## ==================================================================
if __name__ == '__main__':
    main()
```
