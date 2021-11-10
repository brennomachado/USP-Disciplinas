# EI21

Data de entrega: quinta, 11 nov 2021, 08:00
Arquivos requeridos: borbulhagem.py ([Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3960100))
Tipo de trabalho: Trabalho individual

##<font size="4">bolhinhas</font>, <font size="5">bolhas</font> e <font size="6">bolhonas</font>

![Desenho de duas crianças brincando com bolhas](BubbleSort.jpg)

Fonte: [Computer Science without a computer.](https://www.csunplugged.org/)

### Objetivos

Neste exercício vamos continuar o tópico de ordenação de listas.

- Mas por que estudar ordenação se o Python já faz isso pra mim?

O problema de ordenação é um muito rico em soluções diferentes, cada uma baseada em ideias distintas que vai nos ajudar a continuar a desenvolver o pensamento computacional. Vamos aproveitar também para treinar e aprofundar vários fundamentos de análise de algoritmos.

Sendo assim, para treinar esses fundamentos nesses e em futuros exercícios, utilize apenas comandos básicos do Python e, para continuar a desenvolver o pensamento, evite pensar no tipo list. Procure desenhar no papel sequências de números que devem ser ordenados, por exemplo, percorrendo as sequência e trocando os elementos de posição.

---

### O que você deve fazer

Nesse exercício você deve implementar 3 funções:

- borbulhe(seq, n)
- ordene_por_borbulhagem(seq)
- main(): que deve incluir os seus testes para cada função.

O comportamento de cada função está descrito no cabeçalho das funções no arquivo borbulhagem.py.

---

### Roteiro

- Baixe o arquivo borbulhagem.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab ou seu IDE predileto.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Submeta apenas o arquivo borbulhagem.py.

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

##### borbulhagem.py

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


def borbulhe(seq, n):
    ''' (list, int) -> int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso
    deve ser da posição de índice 0 até a posição de índice n.

    Durante o percurso a função COMPARA todos os pares de valores
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5]
    e seq[6] e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

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

        * primeira vez, obtemos seq=[4, 7, 5, 3, 11], com  3 trocas
        * segunda  vez, obtemos seq=[4, 5, 3, 7, 11], mais 2 trocas
        * terceira vez, obtemos seq=[4, 3, 5, 7, 11], mais 1 troca
        * quarta   vez, obtemos seq=[3, 4, 5, 7, 11], mais 1 troca

    Pronto! A lista seq está ordenada.
    Para seq = [7, 4, 11, 5, 3] a função deve retornar 7.
    '''
    print("Vixe! Ainda não fiz a função ordene_por_borbulhagem()...")

## ==================================================================
if __name__ == '__main__':
    main()
```
