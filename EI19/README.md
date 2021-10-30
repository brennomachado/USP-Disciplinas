# EI19
Data de entrega: quarta, 3 nov 2021, 22:00
Arquivos requeridos: busca.py ( [Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3943259) )
Tipo de trabalho: Trabalho individual

## Algoritmos de busca

### Objetivos

Nesse exercício vamos estudar princípios de algoritmos implementando e comparando o consumo de tempo de algoritmos diferentes para resolver o problema de busca de informação em sequências.

Vamos representar as sequências na forma de listas do Python. Por hora, para que possamos trabalhar os conceitos, não utilize os recursos que objetos do tipo listdo Python nos oferece, como sort(), index(), max() etc., pois essas funções podem esconder soluções que desejamos tornar explícitas.

Portanto, procure usar apenas os comando básicos, para tornar explícitas todas as operações. Isso simplifica a análise dos algoritmos e permite avaliar com mais clareza seus consumos de tempo.

--- 
### O que você deve fazer

Você vai implementar 3 funções:

- busca_sequencial()
- busca_sequencial_em_lista_ordenada()
- busca_binariaRED(), que usa a interface busca_binariaR().

O comportamento dessas funções está definido no arquivo busca.py.

---

### Roteiro

- Baixe o arquivo busca.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo buca.py.

---
### Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

### Arquivos requeridos
##### busca.py

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

## ==================================================================

def busca_sequencial( seq, item ):
    ''' (obj, lista) -> int ou None

        Recebe uma lista seq e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        Caso obj não esteja na lista, então a função retorna None.

        OBS: esse é um exercício muito simples para que possamos
        ver a diferença desse algoritmo com os demais. Por isso,
        não use o método index.

        Pré condição: a lista seq não está ordenada.

        Exemplos:

        para seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6] então:

        > busca_sequencial( seq, 0) retorna 5
        > busca_sequencial( seq, 8) retorna 2
        > busca_sequencial( seq, -1) retorna None

    '''
    # escreva sua solução

## ==================================================================

def busca_sequencial_em_lista_ordenada( seq, item ):
    ''' (lista, obj) -> int ou None

        Recebe uma lista seq em ordem crescente e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        
        Caso obj não esteja na lista, então a função retorna None.

        Observe que dependendo do sentido da varredura da lista 
        ordenada, só é necessário percorrer enquanto os itens 
        forem maiores ou menores que o obj.

        Pré condição: a lista seq está ordenada em ordem crescente.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_sequencial_em_lista_ordenada( seq, 0) retorna None
        > busca_sequencial_em_lista_ordenada( seq, 8) retorna 6
        > busca_sequencial_em_lista_ordenada( seq, -1) retorna None

    '''
    # escreva sua solução

## ==================================================================

def busca_binariaR( seq, item ):
    ''' (lista, obj) -> int ou None

        interface para a busca binária recursiva com esq e dir.
        Esq e dir indicam os índices da porção da lista onde 
        item deve ser procurado.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_binariaR( seq, 0) retorna None
        > busca_binariaR( seq, 8) retorna 6
        > busca_binariaR( seq, -1) retorna None

        Não modifique essa função.
    '''

    esq = 0
    dir = len(seq)
    return busca_binariaRED(seq, item, esq, dir)

## ==================================================================

def busca_binariaRED( seq, item, esq, dir ):
    ''' (lista, obj, int, int) -> int ou None

        A ideia de busca binária em sequencia ordenada é testar o meio
        da porção da lista delimitada por [esq : dir].

        Implemente a seguinte ideia recursiva:
        - Se o intervalo for nulo, retorna None. 
        
        - Se o item de seq no meio do intervalo for o elemento procurado, 
        retorna esse índice do meio. 
        
        - Caso contrário, se o meio for maior que o procurado, então
        a busca deve continuar recursivamente na metade menor dada por [esq:meio].
        
        - Caso contrário, a busca deve continuar na outra metade (maior) do
        intervalo.

    '''
    # escreva sua solução

## ==================================================================
## Coloque aqui outras funções que desejar
```