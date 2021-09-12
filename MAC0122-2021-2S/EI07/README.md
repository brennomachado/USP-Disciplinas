# EI07
Data de entrega: segunda, 13 set 2021, 22:00

## Classe Pilha
## Objetivos

O objetivo deste exercício é introduzir o tipo abstrato de dados conhecido como pilha. Vamos aproveitar para revisar o uso de listas e strings em Python.

## Resumo

Uma pilha (=stack) é uma estrutura linear dinâmica em que todas as operações:

- inserções;
- remoções; e
- consultas

são feitas em uma mesma extremidade chamada de topo da pilha, como ilustrado abaixo.
```
  empilha --->---+       +-->----> desempilha
  (=push)        |       |         (=pop)  
                 V       |
               +-----------+
               | vvvvvvvvv |
               +-----------+
               | wwwwwwwww |
               +-----------+
               | zzzzzzzzz |
               +-----------+
               | yyyyyyyyy |
               +-----------+
               | xxxxxxxxx |
               +-----------+
```
## Estudos preliminares

- O que é uma Pilha?
- O tipo abstrato de dados Pilha
- Implementando uma Pilha em Python

## O que você deve fazer

Implemente a classe Pilha que tem comportamento muito parecido com a classe Stack do livro, mas “fala” português.

Sua classe Pilha deve possuir um atributo de nome dados. Esse atributo dados deve ser uma lista que armazena os itens da pilha.
Comportamentos que você deve implementar na classe Pilha

### <span style="color:green">Os comportamentos que você deve implementar na classe Pilha são ilustrados pela seguinte função testes():</span>

```
def testes():

    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")
```
Você pode estender esses comportamentos, desde que sejam consistentes e não alterem os resultados como ilustrados nos exemplos de testes da main().

### <span style="color:green">Função</span> palindromo()

Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante. Por extensão, palíndromo é qualquer série de elementos com simetria linear, ou seja, que apresenta a mesma sequência de unidades nos dois sentidos Wikipedia.

No mesmo arquivo pilha.py, escreva a função palindromo() que recebe uma string e retorna True caso a string seja um palíndromo, e retorna False caso contrário. Sua solução para a função palindromo() deve utilizar a sua classe Pilha.

Observe que uma sequência de empilhamentos seguido por uma sequência de desempilhamentos é uma forma de inverter uma sequência. Por exemplo a sequência de caracteres “pilha” pode ser empilhada, caractere a caractere e, ao ser desempilhada, forma a sequência “ahlip”.


## Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- Baixe o arquivo pilha.py.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo pilha.py com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender como os métodos devem funcionar.
- Documente seu trabalho descrevendo cada método e/ou função.
- Implemente e teste cada método e função.
- Caso você deseje testar alguma função e/ou classe no próprio arquivo pilha.py, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo pilha.py.

## Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

Arquivos requeridos
pilha.py
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
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' documentacao da funcao '''


    print("Vixe! ainda não escrevi a função palindromo()")
    return False


## ==================================================================
##
class Pilha:

    def __init__(self):
        print("Vixe! ainda não escrevi a classe Pilha")

## ==================================================================
## Escreva outras funções e classes caso desejar


## ==================================================================
if __name__ == '__main__':
    palindromo( '' )
```