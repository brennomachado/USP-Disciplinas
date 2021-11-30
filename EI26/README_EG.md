# EG26

Data de entrega: terça, 30 nov 2021, 11:00
Arquivos requeridos: eg_lcs.py ([Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3975127))
Tipo de trabalho: Trabalho individual

## LCS, esquecimentos e memorização com programação dinâmica

<div align="center">
  <img height="200" src="dory.gif">
  <br>
  Fonte: Fonte: Procurando Nemo, Pixar Animation Studios (Tenor).
</div>

### Preparação padrão

Voltem a sala principal caso você esteja sozinhE.

Façam uma cópia do seu EI, colocando o prefixo eg\_. Alternativamente, há um arquivo com um esqueleto deste EG que pode ser baixado desta página. Este esqueleto contém funções totalmente feitas que usaremos nos experimentos.

[Baixem daqui](https://colab.research.google.com/drive/1e-vdQ6yBLRLe_25p1R-EAkMqOdBE36LD?usp=sharing) o programa experimento.py que usaremos para fazermos nossas análises experimentais das funções desenvolvidas .

Preencham o Formulário Individual conforme as instruções.

Escolham a pessoa estagiária e a pessoa gerente conforme as instruções.

Se tiverem alguma dúvida chamem o Hitoshi ou o Coelho. Eles devem estar passeando pelas salas, ou ter ido ao banheiro, ou foram tomar café.

---

### Testes do EI

Vamos testar em grupo a função subseq() que fizeram no EI.

Usem para isso as coletâneas de testes que cada uma/um fez na função main().

Uma das pessoas do time pode agrupar e compartilhar com as demais todos os testes na main(). Assim, todas e todos poderão testar os seus trabalhos individuais.

Cada pessoa do time deve verificar a funções do seu EI/EG está dentro da especificação.

Não hesite em pedir ajuda a seu time em caso de dificuldades.

Caso algum problema seja encontrado, discuta com suas/seus colegas de time para resolvê-lo. Elas/eles ficarão muito felizes em lhe ajudar.

---

### LCS

Uma subsequência de uma dada sequência é a resultante da possível remoção de alguns elementos da sequência dada, sem que a ordem dos elementos restantes seja alterada. Por exemplo, "abc", "abg", "bdf", "aeg", "acefg", "abcdefg", etc. são subsequências de "abcdefg". Já "ec", "ga", "bag", "afeg", "x", etc. não são subsequências de "abcdefg".

O problema que trataremos neste EG é o seguinte.

Problema LCS: dadas duas sequências s e t, encontrar uma maior subsequência comum (LCS=Longest Common Subsequence) de s e t.

Exemplos:

- uma LCS de "ABCDGH" e "AEDFHR" é "ADH", com comprimento 3.
- uma LCS de "AGGTAB" e "GXTXAYB" é "GTAB", com comprimento 4.
- uma LCS de "BDCABA" e "ABCBDAB" é "BDBA", com comprimento 4.
- uma LCS de "ABRACADABRA" e "YABBADABBADOO" é "ABADABA", com comprimento 4.

As operações básicas que usaremos nas nossas funções são igualdade e indexação. Desta forma, as nossas sequências podem ser de qualquer coisa que admita essas operações. No entanto, nas nossas brincadeiras, as sequências serão apenas strings.

Em vários do nossos testes neste EG utilizaremos os seguintes pares de sequências:

- "BDCABA" e "ABCBDAB" e
- "ABRACADABRA" e "YABBADABBADOO".

Como sempre sugerimos, desenhe as sequências e as subsequências para facilitar o entendimento do problema e as possíveis soluções, como abaixo:

```
        +---+---+---+---+---+---+          +---+---+---+---+---+---+---+---+---+---+---+---+
     s  | B | D | C | A | B | A |       s  | A | B | B | A | D | A | B | B | A | D | O | O |
        +---+---+---+---+---+---+          +---+---+---+---+---+---+---+---+---+---+---+---+


        +---+---+---+---+---+---+---+      +---+---+---+---+---+---+---+---+---+---+---+
     t  | A | B | C | B | D | A | B |   t  | A | B | R | A | C | A | D | A | B | R | A |
        +---+---+---+---+---+---+---+      +---+---+---+---+---+---+---+---+---+---+---+
```

Curioso. É fácil encontrar ou ver que uma sequência r é comum a duas sequências dadas s e t. Entretanto, não é nada fácil perceber se r é uma LCS de s e t, mesmo que s e t sejam subsequências curtas. A função subseq() pode ser usada para verificarmos se r e subsequência de s e t, mas ela não garante que r seja a maior subsequência comum.

---

### Desafio

Como desafio, neste EG vocês escreverão apenas a função

lcsPD(s, m, t, n, memo)

Essa função está especificada mais adiante. Ela é o braço direito ou esquerdo, dependendo se vocês são destra(o)s ou canhota(o)s, da função lcs_iterPD(s, t). Esta última, por sua vez, recebe duas sequências s e t e retorna uma LCS dessas sequências. O outro braço de lcs_iterPD(s, t), esquerdo ou direito, dependendo …, é uma função que aparecerá mais adiante na nossa estória de hoje. De qualquer forma, lcs_iter() precisará dos dois braços para fazer o seu trabalho.

---

### Perda de memória recente

No EI você viu uma função lcs_rec(). A alma de lcs_rec() é a função lcsR(), que também foi dada no EI. A função lcsR() parece meio embaçada. Ela se baseia em uma baita (!) ideia que é profundamente/visceralmente recursiva. Essa função é uma testemunha viva de que recursão está mais ligada a ideias do que a forma que essas ideias são expressas em uma linguagem de programação.

O problema com nossa função lcsR() e que, apesar de implementar um ideia sensacional, parece ser meio lerda. Parece que já passamos por uma situação semelhante, não lembro onde…

Esperem um pouco! Em umas reuniões passadas, quando discutíamos funções recursivas, havia algumas funções que eram muito lentas pois se esqueciam rapidamente das soluções de subproblemas que tinham acabado de resolver. Quais eram as funções? fatorialR()? fibonacciR()? binomialR()? Não importa.

A função lcsR() pode estar sofrendo da mesma falta de memória que suas colegas. Temos um remédio para perda de memória? Sim! Está relacionado a não jogarmos fora as soluções de subproblemas logo depois e terem sido obtidas, anotando os resultados parciais em um rascunho. Já fizemos isso em outras ocasiões, adicionamos a letra M, de memorização, ao final do nome das funções em que aplicávamos essa ideia: fatorialRM(); fibonacciRM(); binomialRM(),…

Quando aplicamos o princípio ativo M, estávamos lidando com funções recursivas que começam com um problema difícil, como fibonacciRM(10), e simplificam o problema até chegar em um caso base. Esse tipo de solução ataca o problema de cima-para-baixo (top-down).

No desafio de hoje vocês prepararão um remédio com princípio ativo PD, que ataca o problema de baixo-para-cima ou bottom-up.

---

### Remédio caseiro

O remédio caseiro que vocês prepararão utiliza o princípio ativo ou método chamado de Programação Dinâmica. Esse método transforma um problema em uma coleção de subproblemas mais simples. Cada subproblema é resolvido uma única vez e a solução é armazenada em uma tabela. Da próxima vez que o mesmo subproblema é encontrado, a solução pré computada é utilizada, economizando tempo mas com um gasto de espaço extra que desejamos que seja modesto.

No nosso caso, a função lcsPD(s, m, t, n) que vocês escreverão terá a missão de preencher iterativamente (o que é isso mesmo?) uma tabela de nome memo de dimensão (m + 1) × (n + 1). Para todo i=0,1,...,m e j=0,1,...,n a posição memo[i, j] deverá armazenar o comprimento de um LCS de s[0:i] e t[0,j]. A especificação dessa função esta logo abaixo.

```
def lcsPD(s, m, t, n, memo):
    '''(str, int, str, int) -> None
    RECEBE uma string s, um inteiro m, uma string t, um inteiro n
        e um array memo.
    PREENCHE o array memo de tal forma que para todo
      par (i,j),  com 0 <= i <= m e 0 <= j <= n, tenhamos que
      memo[i,j] é o comprimento de uma LCS de s[0:i] e t[0:j]
    '''
```

Aqui vai um exemplo de execução de lcsPD().

```
    In [6]: s = 'BDCABA'
    In [7]: t = 'ABCBDAB'
    In [8]: m, n = len(s), len(t)
    In [9]: memo = np.full((m+1,n+1), 0)
    In [10]: lcsPD(s, m, t, n, memo)
    In [11]: memo
    Out[11]:
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 2, 2, 2],
           [0, 0, 1, 2, 2, 2, 2, 2],
           [0, 1, 1, 2, 2, 2, 3, 3],
           [0, 1, 2, 2, 3, 3, 3, 4],
           [0, 1, 2, 2, 3, 3, 4, 4]])

    In [12]: monte_lcs(s, t, memo)
    Out[12]: 'BDAB'
```

Olhemos com uma lente de aumento para a tabela memo que lcsPD() preencheu para s="ABCBDAB" e t="BDCABA". A posição memo[7, 6] tem o valor 4 já que "BCBA" tem comprimento 4 e é uma LCS de s[0:7] = s e t[0:6]. A posição memo[4, 3] tem o valor 2 já que "BC" tem comprimento 2 e é uma LCS de s[0:4] = "ABCB" e t[0:3] = "BDC".

```
            B   D   C   A   B   A    t
        0   1   2   3   4   5   6
      +---+---+---+---+---+---+---+
    0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
      +---+---+---+---+---+---+---+
  A 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
      +---+---+---+---+---+---+---+
  B 2 | 0 | 1 | 1 | 1 | 1 | 2 | 2 |
      +---+---+---+---+---+---+---+
  C 3 | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
      +---+---+---+---+---+---+---+
  B 4 | 0 | 1 | 1 | 2 | 2 | 3 | 3 |
      +---+---+---+---+---+---+---+
  D 5 | 0 | 1 | 2 | 2 | 2 | 3 | 3 |
      +---+---+---+---+---+---+---+
  A 6 | 0 | 1 | 2 | 2 | 3 | 3 | 4 |
      +---+---+---+---+---+---+---+
  B 7 | 0 | 1 | 2 | 2 | 3 | 4 | 4 |
      +---+---+---+---+---+---+---+
  s
```

Precisa de inspiração para escrever a função lcsPD()? Olhe, mas olhe muito mesmo, para lcsR(), notamos que o valor de uma posição memo[i, j] depende de pouca gente. Em geral o valor de memo[i, j] depende apenas de cinco atrizes e atores:

- de s[i] e t[j] e
- dos valores nas posições memo[i-1,j-1], memo[i-1, j] e memo[i, j-1].

Procurem agora ver a política para preencher a tabela memo sugerida por essa observação.

---

### Mais devagar com isso…

Espera ai! Tem algo muito estranho aqui! Vamos levar à Anvisa uma queixa sobre esse remédio para memória! A função lcsPD(s, m, t, n, memo) apenas preenche o array memo com os comprimentos de LCSs de subsequências de s e t e não com LCSs.

Calma. Não há nada de errado com o remédio. Ele não trabalha sozinho. Vocês receberão uma LCS de s e t como prometido. Neste ponto talvez seja bom vocês seguirem a leitura dando uma olhada na função lcs_iterPD() que está no esqueleto deste EG.

```
def lcs_iterPD(s, t):
    '''(str, str) -> str
    INTERFACE para a função recursiva lcsPD() e monte_lcs().
    RETORNA uma LCS de s e t.
    '''
    m = len(s)
    n = len(t)

    #------------------------------------------------
    # memo[i,j] será o comprimento de uma LCS de s[0:i] e t[0:j]
    memo = np.full((m+1, n+1), 0)

    # lcsPD(s, m, t, n, memo) preenche o array memo
    lcsPD(s, m, t, n, memo)

    return monte_lcs(s, t, memo)
```

A função lcs_iterPD() é uma interface para lcsPD() e cuida de questões administrativas, como a criação do array memo. É de responsabilidade de lcsPD() preencher o array memo, certo? Ao preencher, a função está marcando os caminhos que levam a maior subsequência, deixando umas migalhas de pão nesse labirinto. Com o array memo preenchido e em mãos, lcs_iterPD() o repassa para a sua assistente monte_lcs(s, t, memo), que percorre o caminho marcado para montar a LCS. Agora sim! A função monte_lcs() está no esqueleto deste EG. Satisfeitas? Satisfeitos?

---

### Experimentos

Baixem o arquivo experimento.py. Este arquivo fará experimentos com as funções

- lcs_rec(): dada no EI, interface para lcsR(), recebeu medicamento neste EG para ajudar a lembrar as soluções dos subproblemas;
- lcs_iterPD(): interface para a função lcsPD() que vocês fizeram.

Baseados nesses experimentos, qual o consumo de tempo assintótico dessas funções? Agora, uma pergunta.

**Pergunta:** Quanto tempo vocês estimam que cada um dessas funções gastará para encontrar uma LCS de sequências de comprimento 218 = 262144?

Procure responder em unidades como segundos, ou minutos, ou horas, ou dias, ou anos, …

---

### Lições

Vimos como o pensamento recursivo é usado para desenvolver soluções para problema mais envolventes. As ideas trabalhadas são as mesmas que já haviam sido aplicadas em problemas mais simples.

Também aprendemos que… aprendemos que… aprendemos que… Hmm. Não lembro…

Ideias? Comentários? Perguntas?

---

### Para conseguir um bônus …

Nesta altura do campeonato todo mundo já sabe …

Para entregar o EG não é necessário modificar o cabeçalho do seu EI. Você pode fazer as modificações que desejar no código do EI, seguindo ou não as discussões do time.

Você precisa entregar o arquivo com extensão eg\_ contendo a função subseq() do EI com a main(). As novas funções implementados podem ser incluídas e têm sido bônus do bônus.

Você também precisa responder o formulário individual cujo link está no início deste EG.

Teste a solução antes de entregá-la.

O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.

---

### Simulação

Vejam o trabalho feito por lcs_rec('abra', 'yabba')

```
    lcsR(s[0:4],t[0:5])
      lcsR(s[0:3],t[0:4])
        lcsR(s[0:2],t[0:4])
          lcsR(s[0:1],t[0:3])
            lcsR(s[0:0],t[0:3])
            return ''
            lcsR(s[0:1],t[0:2])
              lcsR(s[0:0],t[0:1])
              return ''
            return 'a'
          return 'a'
        return 'ab'
        lcsR(s[0:3],t[0:3])
          lcsR(s[0:2],t[0:3])
            lcsR(s[0:1],t[0:2])
              lcsR(s[0:0],t[0:1])
              return ''
            return 'a'
          return 'ab'
          lcsR(s[0:3],t[0:2])
            lcsR(s[0:2],t[0:2])
              lcsR(s[0:1],t[0:2])
                lcsR(s[0:0],t[0:1])
                return ''
              return 'a'
              lcsR(s[0:2],t[0:1])
                lcsR(s[0:1],t[0:1])
                  lcsR(s[0:0],t[0:1])
                  return ''
                  lcsR(s[0:1],t[0:0])
                  return ''
                return ''
                lcsR(s[0:2],t[0:0])
                return ''
              return ''
            return 'a'
            lcsR(s[0:3],t[0:1])
              lcsR(s[0:2],t[0:1])
                lcsR(s[0:1],t[0:1])
                  lcsR(s[0:0],t[0:1])
                  return ''
                  lcsR(s[0:1],t[0:0])
                  return ''
                return ''
                lcsR(s[0:2],t[0:0])
                return ''
              return ''
              lcsR(s[0:3],t[0:0])
              return ''
            return ''
          return 'a'
        return 'ab'
      return 'ab'
    return 'aba'
    aba
```

---

### Arquivos requeridos

##### eg_lcs.py

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

#------------------------------------------------------
def main():
    '''
    Testes para os algoritmos de LCS

    Inclua ao menos 10 testes distintos para sua função subseq().
    '''
    print("Testes para sua função subseq()")
    print("--------------------------------\n")



    print("Exemplos de execuções de lcs_rec() e lcs_iterPD()")
    print("----------------------------------")


#----------------------------------------------
def subseq (s, t):
    ''' (str, str) -> bool
    RECEBE duas strings s e t.
    RETORNA True se s é subsequência de t.
    '''
    # escreva sua solução

#----------------------------------------------------------------
# LCS RECURSIVA
#----------------------------------------------------------------
def lcs_rec(s, t):
    '''(str, str) -> str
    INTERFACE para a função recursiva lcsR().

    EXEMPLOS

    In [17]: s = 'BDCABA'
    In [18]: t = 'ABCBDAB'
    In [19]: lcs_rec(s, t)
    Out[19]: 'BCBA'

    In [20]: s = 'ABRACADABRA'
    In [21]: t = 'YABBADABBADOO'
    In [22]: lcs_rec(s, t)
    Out[22]: 'ABADABA'
    '''
    m = len(s)
    n = len(t)
    return lcsR(s, m, t, n)

#----------------------------------------------
def lcsR(s, m, t, n):
    '''(str, int, str, int) -> str
    RECEBE uma string s, um inteiro m, uma string t e um inteiro n.
    RETORNA uma LCS de s[0:m] e t[0:n].

    EXEMPLOS

    In [23]: s = 'BDCABA'
    In [24]: t = 'ABCBDAB'
    In [25]: lcsR(s, 4, t, 5)
    Out[25]: 'BC'

    In [26]: s = 'ABRACADABRA'
    In [27]: t = 'YABBADABBADOO'
    In [28]: lcsR(s, 9, t, 7)
    Out[28]: 'ABADA'
    '''
    # BASE
    if m == 0 or n == 0: return ""

    # REDUZ
    if s[m-1] == t[n-1]:
        return lcsR(s, m-1, t, n-1) + s[m-1]

    # REDUZ
    lcs_1 = lcsR(s, m-1, t,   n)
    lcs_2 = lcsR(s,   m, t, n-1)

    # COMBINA
    if len(lcs_1) > len(lcs_2): return lcs_1
    return lcs_2


#----------------------------------------------------------------
# LCS ITERATIVA com MEMÓRIA
#----------------------------------------------------------------
def lcs_iterPD(s, t):
    '''(str, str) -> str
    INTERFACE para a função recursiva lcsPD() e monte_lcs().
    RETORNA uma LCS de s e t.

    EXEMPLOS

    In [42]: s = 'BDCABA'
    In [43]: t = 'ABCBDAB'
    In [44]: lcs_iterPD(s, t)
    Out[44]: 'BDAB'

    In [45]: s = 'ABRACADABRA'
    In [46]: t = 'ABCBDAB'
    In [47]: lcs_iterPD(s, t)
    Out[47]: 'ABCDAB'
    '''
    m = len(s)
    n = len(t)

    #------------------------------------------------
    # memo é o array rascunho em que para todo par (i,j)
    # com 0 <= i <= m e 0 <= j <= n tem-se que memo[i, j]
    # é o comprimento de uma LCS de s[0:i] e t[0:j]
    memo = np.full((m+1, n+1), 0)

    # lcsPD(s, m, t, n, memo) preenche o array memo
    lcsPD(s, m, t, n, memo)

    return monte_lcs(s, t, memo)

#----------------------------------------------
def lcsPD(s, m, t, n, memo):
    '''(str, int, str, int) -> None
    RECEBE uma string s, um inteiro m, uma string t, um inteiro n
        e um array memo.
    PREENCHE o array memo de tal forma que para todo
      par (i,j),  com 0 <= i <= m e 0 <= j <= n, tenhamos que
      memo[i,j] é o comprimento de uma LCS de s[0:i] e t[0:j]

    VERSÃO ITERATIVA que nas redes sociais recebe o adjetivo sexy
        de bottom-up, ou de baixo para cima.

    EXEMPLO

    In [6]: s = 'BDCABA'
    In [7]: t = 'ABCBDAB'
    In [8]: m, n = len(s), len(t)
    In [9]: memo = np.full((m+1,n+1), 0)
    In [10]: lcsPD(s, m, t, n, memo)
    Out[10]: 4
    In [11]: memo
    Out[11]:
    array([[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 1, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 2, 2, 2],
           [0, 0, 1, 2, 2, 2, 2, 2],
           [0, 1, 1, 2, 2, 2, 3, 3],
           [0, 1, 2, 2, 3, 3, 3, 4],
           [0, 1, 2, 2, 3, 3, 4, 4]])

    In [12]: monte_lcs(s, t, memo)
    Out[12]: 'BDAB'
    '''
    # escreva sua solução

#---------------------------------------------------------
# FUNÇÃO AUXILIAR
#---------------------------------------------------------
def monte_lcs(s, t, memo):
    '''(str, str, array) -> str
    RECEBE uma string s, uma string t e um array memo tal que
        para todo i = 0,1,...,len(s) e j = 0,1,...,lent(t)
        memo[i,j] é comprimento de uma LCS de s[0:i] e t[0:j]
    RETORNA uma LCS de s e t.
    '''
    lcs = ''
    m, n = len(s), len(t)
    i, j  = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            lcs = s[i-1] + lcs
            i -= 1
            j -= 1
        elif memo[i-1, j] >= memo[i, j-1]:
            i -= 1
        else:
            j -= 1
    return lcs

#----------------------------------------------------
if __name__ == "__main__":
    main()
```
