# EI18
Data de entrega: quinta, 28 out 2021, 08:00
Arquivos requeridos: blobs.py ( Baixar)
Tipo de trabalho: Trabalho individual

## Processamento de Imagens Digitais: lista com todos os blobs
``All colors will agree in the dark.,
Francis Bacon.``

### Objetivos
Neste exercício vamos continuar o tópico de segmentação de blobs (regiões conexas) de uma imagem. Para facilitar a manipulação de blobs, vamos agora colocar tudo dentro de uma classe Blobs.
---
### O que você deve fazer

Nesse exercício você deve implementar a classe Blobs que deve conter os métodos:

- segmente(self, img)
- segmente_blob(self, img, semente)
- segmente_blob_RM(self, img, semente, visitados)
- pinte_blob(self, img, blob, nova_cor)

A descrição desses métodos está no arquivo blobs.py. Observe que apenas o método segmente(self, img) dentre esses métodos é inteiramente novo. Os demais métodos você deve adaptar das funções que você implementou no exercício anterior.

Além disso, ao ser criado, um objeto da classe Blobs deve possuir um atributo de nome data que contém a lista com todos os blobs, em qualquer ordem, que constituem a imagem usada na criação do objeto. Os métodos __init__() e __str__() da classe Blobs são dados. Você pode alterar esses métodos desde que não altere o comportamento abaixo.

O seguinte trecho de programa ilustra como um objeto da classe Blobs é criado e como podemos acessar as blobs na lista data.

```
    x = [    
            8, 8, 8, 8, 1, 4,
            1, 8, 1, 1, 1, 4,
            1, 8, 8, 1, 4, 4,
            1, 1, 1, 1, 4, 4,
            1, 9, 1, 4, 1, 4,
            9, 9, 9, 9, 1, 4
        ]

    img = np.array(x).reshape(6,6)
    print(f'Imagem\n', img)

    # cria um objeto Blobs usando img
    blobs = Blobs(img)

    # vamos ver as blobs
    dt = blobs.data
    n = len(dt)
    for i in range(n):
        elem = list(dt[i])[0] # pega um elemento do conjunto
        print(f'blob {i} tem tamanho {len(dt[i])} e cor {img[elem]}')
        print(f'   {dt[i]}')
```

A saída desse trecho de código deve ser:
```
    Imagem
    [[8 8 8 8 1 4]
    [1 8 1 1 1 4]
    [1 8 8 1 4 4]
    [1 1 1 1 4 4]
    [1 9 1 4 1 4]
    [9 9 9 9 1 4]]
    blob 0 tem tamanho 7 e cor 8
    {(0, 1), (2, 1), (0, 0), (1, 1), (0, 3), (0, 2), (2, 2)}
    blob 1 tem tamanho 13 e cor 1
    {(1, 2), (0, 4), (4, 0), (3, 1), (2, 0), (1, 4), (3, 0), (2, 3), (4, 2), (3, 3), (1, 0), (3, 2), (1, 3)}
    blob 2 tem tamanho 8 e cor 4
    {(2, 4), (5, 5), (3, 4), (1, 5), (4, 5), (0, 5), (2, 5), (3, 5)}
    blob 3 tem tamanho 5 e cor 9
    {(5, 1), (5, 0), (5, 3), (4, 1), (5, 2)}
    blob 4 tem tamanho 1 e cor 4
    {(4, 3)}
    blob 5 tem tamanho 2 e cor 1
    {(4, 4), (5, 4)}
```
---
### Roteiro

- Baixe o arquivo blobs.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
 -Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo blobs.py.

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
##### blobs.py
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

class Blobs:

    def __init__(self, img):
        ''' (Blobs, array) -> None 
        construtor da classe Blobs.
        '''

        self.data = []
        self.segmente(img) # deve carregar self.data
        ## inclua outros atributos que desejar

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Blobs) -> str
        retorna uma string com a descrição das blobs.
        '''
        
        txt = ''
        dt = self.data
        n = len(dt)
        for i in range(n):
            txt += f'blob {i} tem tamanho {len(dt[i])}\n'
            txt += f'   {dt[i]}\n'
        return txt

    # ---------------------------------------------------------------
    def segmente(self, img):
        ''' (Blobs, array) -> None
        Método usado pelo construtor para segmentar todas
        as blobs da imagem img.
        '''
        print("Vixe! Ainda não escrevi o método segmente.")

    # ---------------------------------------------------------------
    def segmente_blob( self, img, semente ):
        ''' (Blobs, ndarray, tuple) -> set

            interface para o método self.segmente_blob_RM.
            Cria um conjunto vazio que é carregado
            de forma recursiva.  
            
            Não altere esse método.
        '''
        return self.segmente_blob_RM( img, semente, set() )

    # ---------------------------------------------------------------
    def segmente_blob_RM(self, img, semente, visitados ):
        ''' (Blobs, ndarray, tuple, set) -> set

        Recebe, além de self, um ndarray img e uma tupla semente contendo a
        coordenada de um pixel de img. Recebe também o conjunto
        visitados, que contém as coordenadas dos pixels já 
        visitados.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        print("Vixe! Ainda não adaptei o método segmente_blob_RM.")

    ## ==================================================================

    def pinte_blob( self, img, blob, nova_cor = 0):
        ''' (Blobs, ndarray, set, int) -> None

        Recebe, além de self, um ndarray img e um conjunto de pixels blob
        e pinta esses pixels com a nova_cor.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        print("Vixe! Ainda não adaptei o método pinte_blob.")

## ==================================================================
## Coloque aqui outras funções e métodos que desejar
```