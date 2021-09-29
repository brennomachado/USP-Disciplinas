# EI12
Data de entrega: quinta, 30 set 2021, 08:00
Arquivos requeridos: npimagem.py ( Baixar)
Tipo de trabalho: Trabalho individual

## Classe NPImagem

Nesse exercício vamos treinar o uso de arrays do módulo NumPy.
Leituras preliminares:
- Tipos de dados abstratos - Arrays
- O que é uma imagens digital
  - Por simplicidade, vamos trabalhar com imagens com tons de cinza, onde cada tom é representado por um inteiro. As funções para ler, gravar e mostrar imagens na tela serão fornecidas posteriormente. Nesse exercício vamos começar a entender como manipular as matrizes (arrays) que representam as imagens.


##O que você deve fazer

A classe NPImagem que você vai começar a implementar deve representar imagens digitais através dos arrays de NumPy. Para isso, um objeto da classe NPImagem deve possuir um atributo de nome data do tipo numpy.ndarray que é utilizado internamente nas operações com imagens dessa classe.

Seja img um objeto da classe NPImagem. Então img deve se comportar da seguinte forma:
- img = NPImagem( (nlins, ncols), val). Um objeto NPImagem é criado ao escrevermos NPImagem( (nlins, ncols), val). Aqui nlins e ncols são dois inteiros que definem a dimensão nlins x ncols do array que representa a imagem e val é o valor inicial de cada um de seus pixels, Caso o val não seja especificado na chamada, a imagem deve ser criada tendo 0 como valor de cada pixel.
- Importante: caso o tipo do val seja um array do Numpy, a NPImagem criada deve usar esse array como seu conteúdo inicial. Veja nos exemplos que os valores de nlins e ncols não importam se val é uma array.
- A função print() deve exibir um objeto NPImagem simplesmente mostrando o conteúdo do atributo data. Esse item é muito importante para ajudar você a depurar sua classe.
- img.shape. O valor do atributo shape de um objeto img da classe NPImagem deve ser a tupla (nlins, ncols) que indica a dimensão de img.
- img[lin, col]. Implemente o método \_\_getitem__() para permitir que, ao escrevermos img[lin, col], tenhamos acesso ao valor do pixel [lin, col].
- img[lin, col] = val. Implemente o método \_\_setitem__() para permitir que, ao escrevermos img[lin, col] = val, o valor val seja armazenado no pixel [lin, col] de img.
- img.crop(sup, esq, inf, dir). Implemente o método crop() que recebe 4 inteiros sup, esq, inf e dir que definem um retângulo de uma imagem onde: esq indica a primeira coluna, dir a última coluna, sup a primeira linha e inf a última linha do retângulo. Você pode entender esses inteiros como as coordenadas do canto esquerdo-superior (sup,esq) e do canto direito-inferior(inf,dir) do retângulo. Assim, se img é um objeto NPImagem, então img.crop(sup, esq, inf, dir) deve retornar uma nova NPImagem com a subimagem de img definida por sup, esq, inf e dir. Caso esses quatro valores não sejam especificados na chamada, o método considera sup e esq como sendo zero, a origem da imagem, e inf e dir como as dimensões da imagem. Nesse caso, portanto, a chamada retorna um clone de img. O exemplo também mostra quando apenas o canto (sup,esq) é fornecido.

Você pode estender sua classe com outros métodos, atributos e usar outras funções caso desejar, desde que eles não entrem em conflito ou modifiquem o comportamento da classe NPImagem, como especificado nesse texto.


### DICAS

Não faça nada do zero. Utilize o que você já implementou nos EPs anteriores e apenas faça as modificações necessárias para criar a classe NPImagem.

Para fazer recortes com crop(), você pode utilizar o operador slice em vez de laços. Além de ser mais eficiente, você economiza tempo escrevendo menos código.


### Exemplo

Estude os exemplos a seguir para compreender o comportamento esperado de um objeto do tipo NPImagem.

```
    lista = list(range(20))
    ar = np.array(lista).reshape(4,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1,2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)  
    print(f"img4:\n{img4}\n")

    img5 = NPImagem( (3,2) )
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1,2)
    print(f"img6:\n{img6}\n")
```
O resultado deve ser:
```

    img1:
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    Shape de img1: (4, 5)

    img2:
    [[100 100 100]
     [100 100 100]
     [100 100 100]
     [100 100 100]]
    Shape de img2: (4, 3)

    img2[1,2]=-10
    img2:
    [[100 100 100]
     [100 100 -10]
     [100 100 100]
     [100 100 100]]

    img3:
    [[100 100 100]
     [100 100 -10]
     [100 100 100]
     [100 100 100]]

    img4:
    [[ 1  2  3]
     [ 6  7  8]
     [11 12 13]]

    img5:
    [[0 0]
     [0 0]
     [0 0]]

    img6:
    [[ 7  8  9]
     [12 13 14]
     [17 18 19]]
```
## Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- Baixe o arquivo npimagem.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo npimagem.py.

## Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

### Arquivos requeridos
#### npimagem.py
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


import numpy as np

## ------------------------------------------------------------------
def main():

    print("Testes da classe NPImagem\n")

## ------------------------------------------------------------------
class NPImagem():

    # escreva aqui os métodos da classe NPImagem
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
```