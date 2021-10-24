# EI17
Data de entrega: segunda, 25 out 2021, 22:00
Arquivos requeridos: blobs.py ( [Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3942004))
Tipo de trabalho: Trabalho individual
## Processamento de Imagens Digitais: segmentação de blobs

``All colors will agree in the dark.’’,
[Francis Bacon](https://en.wikipedia.org/wiki/Francis_Bacon).

### Objetivos

Neste exercício vamos retomar o tópico de processamento de imagens para desenvolver um algoritmo recursivo para a segmentação de blobs (regiões conexas) de uma imagem. Por simplicidade, vamos trabalhar diretamente sobre arrays do Numpy.

--- 

### O que é uma blob (região conexa)?

Vamos considerar uma blob como sendo uma região conexa (agrupamento) de pixels de mesma cor com conectividade de 4, isto é, considerando os vizinhos superiores, inferiores e laterais (iremos desconsiderar os vizinhos nas diagonais que aumentaria a conectividade para 8 vizinhos).

Vamos representar uma blob por meio de um conjunto (set) de tuplas, onde as tuplas contém coordenadas de pixeis que estão contidos na blob.

É interessante observar que uma imagem é, em geral, constituída por várias blobs. O exemplo abaixo ilustra esse caso.
#### Exemplo

Considere a imagem de níveis de cinza abaixo:
```
linha 0 |  1 8 7 6 2 4
linha 1 |  1 8 1 1 1 3
linha 2 |  1 0 2 1 2 8
linha 3 |  1 1 1 1 0 3
linha 4 |  5 9 1 0 1 1
linha 5 |  9 9 9 0 1 0
```

A blob segmentada usando como semente a origem (0, 0), corresponde aos pixels com valor 1 e conectividade 4 a partir de (0,0), como ilustrado abaixo:
```
linha 0 |  1 - - - - -    
linha 1 |  1 - 1 1 1 -    
linha 2 |  1 - - 1 - -    
linha 3 |  1 1 1 1 - -    
linha 4 |  - - 1 - - -    
linha 5 |  - - - - - -    
```
Podemos representar essa região como o seguinte conjunto de tuplas:

blob1 = {(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 2), (2, 3), (1, 3), (1, 2), (1, 4)}

### Tipo set

Vamos utilizar o tipo set do Python para representar uma blob. O comportamento básico de objeto do tipo set é ilustrado pelo trecho de código abaixo.
```
    '''
    Comportamento básico de um objeto do tipo set
    Para saber mais veja: 
    https://docs.python.org/pt-br/3/tutorial/datastructures.html#sets
    '''
    def main():
        conj0 = set()    # cria um conjunto vazio
        print(f' 1: conj0: {conj0} tem tamanho {len(conj0)}')

        # cria um conjunto. Observe que não há "ordem" nos elementos.
        conj1 = { 'set', "e'", (2,2), 'da hora', '!!' }
        print(f' 2: conj1: {conj1} tem tamanho {len(conj1)}')

        # use o método add para adicionar elementos
        for i in range(5):
            conj0.add( (i, 2) )
        print(' 3: conj0:', conj0)

        # união de conjuntos
        print(' 4: uniao:', conj0.union(conj1))
        # intersecção de conjuntos
        print(' 5: intersecção:', conj1.intersection(conj0))

        # varrer elementos em um conjunto. 
        # Lembre-se que não há uma "ordem"
        for elemento in conj0:
            # testa se ele está dentro de conj1
            if elemento in conj1:
                print(f" >>> {elemento} pertence a {conj1}")
            else:
                print(f" x   {elemento} não pertence a {conj1}")

    main()
```
Baixe e execute esse programa para entender o comportamento de objetos do tipo set. A saída desse programa é ilustrado abaixo:
```
    1: conj0: set() tem tamanho 0
    2: conj1: {'!!', 'set', (2, 2), 'da hora', "e'"} tem tamanho 5
    3: conj0: {(1, 2), (4, 2), (0, 2), (2, 2), (3, 2)}
    4: uniao: {(1, 2), (4, 2), (0, 2), '!!', 'set', (2, 2), 'da hora', (3, 2), "e'"}
    5: intersecção: {(2, 2)}
    x   (1, 2) não pertence a {'!!', 'set', (2, 2), 'da hora', "e'"}
    x   (4, 2) não pertence a {'!!', 'set', (2, 2), 'da hora', "e'"}
    x   (0, 2) não pertence a {'!!', 'set', (2, 2), 'da hora', "e'"}
    >>> (2, 2) pertence a {'!!', 'set', (2, 2), 'da hora', "e'"}
    x   (3, 2) não pertence a {'!!', 'set', (2, 2), 'da hora', "e'"}    
```

Observe que não há uma ordem definida entre os elementos em um conjunto. Também não há repetição de elementos. Portanto, permutações desses elementos implicam no mesmo conjunto. Sendo assim, nesse exercício, se você escolher inicialmente qualquer coordenada da blob como semente, a blob resultante será a mesma (mesmo conjunto).

Observe que a cor 1 está presente em duas regiões conexas distintas. Além da região descrita pela blob1, existe também uma segunda região definida por:
```
linha 0 |  - - - - - -
linha 1 |  - - - - - -
linha 2 |  - - - - - -
linha 3 |  - - - - - -
linha 4 |  - - - - 1 1
linha 5 |  - - - - 1 -
```
blob2 = { (4, 4), (4, 5), (5, 4) }

--- 

### Detalhes sobre a implementação

Como visto acima, uma blob deve ser representada como um conjunto de coordenadas.

Você deve implementar a função recursiva segmente_blob_RM() e pinte_blob() como descritas no arquivo blobs.py. O trecho de código abaixo ilustra o funcionamento dessas funções. Observe que a função segmente_blob_RM() é chamada pela interface segmente_blob().
```

    x = [    
            1, 8, 7, 6, 1, 4,
            1, 8, 1, 1, 1, 3,
            1, 0, 2, 1, 2, 8,
            1, 1, 1, 1, 0, 3,
            5, 9, 1, 0, 1, 1,
            9, 9, 9, 0, 1, 0
        ]

    img = np.array(x).reshape(6,6)
    print(f'Imagem\n', img)
    
    sementes = [(0,0), (5,4)]

    nova_cor = -1
    for s in sementes:
        res = segmente_blob(img, s)
        print(f'\nSegmentei {len(res)} pixels a partir de {s}')
        print( res )

        pinte_blob(img, res, nova_cor)
        print(f'\nimagem pintada')
        print(img)
        nova_cor -= 1
```

A saída desse trecho é mostrada abaixo.

```
Imagem
 [[1 8 7 6 1 4]
 [1 8 1 1 1 3]
 [1 0 2 1 2 8]
 [1 1 1 1 0 3]
 [5 9 1 0 1 1]
 [9 9 9 0 1 0]]

Segmentei 13 pixels a partir de (0, 0)
{(1, 2), (0, 4), (0, 0), (3, 1), (2, 0), (4, 2), (3, 0), (2, 3), (1, 4), (3, 3), (1, 0), (3, 2), (1, 3)}

imagem pintada
[[-1  8  7  6 -1  4]
 [-1  8 -1 -1 -1  3]
 [-1  0  2 -1  2  8]
 [-1 -1 -1 -1  0  3]
 [ 5  9 -1  0  1  1]
 [ 9  9  9  0  1  0]]

Segmentei 3 pixels a partir de (5, 4)
{(4, 4), (5, 4), (4, 5)}

imagem pintada
[[-1  8  7  6 -1  4]
 [-1  8 -1 -1 -1  3]
 [-1  0  2 -1  2  8]
 [-1 -1 -1 -1  0  3]
 [ 5  9 -1  0 -2 -2]
 [ 9  9  9  0 -2  0]]
 ```

---

### Roteiro

- Baixe o arquivo blobs.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo blobs.py.

### Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

### Arquivos requeridos
#### blobs.py

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

def segmente_blob( img, semente ):
    ''' (ndarray, tuple) -> set

        interface para a função segmente_blob_RM.
        Cria um conjunto vazio que é carregado
        de forma recursiva.  
        
        Não altere essa função.
    '''
    return segmente_blob_RM( img, semente, set() )

def segmente_blob_RM( img, semente, visitados ):
    ''' (ndarray, tuple, set) -> set

    Recebe um ndarray img e uma tupla semente contendo a
    coordenada de um pixel de img. Recebe também o conjunto
    visitados, que contém as coordenadas dos pixels já 
    visitados.

    DICA: uma ideia de algoritmo recursivo é
    - se a semente já foi visitada, retorna None.
    - caso contrário, 
        - marca a semente como visitada e
        - propaga recursivamente para os vizinhos de mesma cor.
    '''

    print("Vixe! Ainda não fiz a função semente_blob_RM.")

## ==================================================================

def pinte_blob( img, blob, nova_cor = 0):
    ''' (ndarray, set, int) -> None

    Recebe um ndarray img e um conjunto de pixels blob
    e pinta esses pixels com a nova_cor.

    '''

    print("Vixe! Ainda não fiz a função pinte_blob.")

## ==================================================================
## Coloque aqui outras funções que desejar
```