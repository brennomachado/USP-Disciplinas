# EI15
Data de entrega: segunda, 18 out 2021, 22:00
Arquivos requeridos: fibonacci.py ( Baixar)
Tipo de trabalho: Trabalho individual

## Recursão

Vamos continuar a desenvolver algoritmos recursivos e aprender a torná-los tão eficientes quanto suas versões iterativas.

### Leituras preliminares

- Recursão

### O que você deve fazer

Você deve escrever duas funções:

- função 1: Escreva uma função recursiva para cálculo do n-ésimo número da sequência de Fibonacci.

  A sequência de Fibonacci é definida pela seguinte fórmula recursiva para um inteiro não negativo n:

    Fn = Fn − 2 + Fn − 1

    considerando os valores iniciais F0 = 0 e F1 = 1, escreva a função:
    ```
    def fibonacciR(n):
        '''(int) -> int

        Recebe um inteiro não negativos n e calcula o
        n-ésimo número de fibonacci de forma recursiva.
        Retorna o valor calculado.

        Exemplos:
        fibonacciR(5) = 5
        fibonacciR(10) = 55
        fibonacciR(20) = 6765
        fibonacciR(30) = 832040
        fibonacciR(40) = 102334155
        '''
    ```
    Exemplos:

- função 2: Escreva uma função iterativa para cálculo do n-ésimo número da sequência de Fibonacci. A função deve ter o mesmo comportamento da função anterior, mas deve ser iterativa.
    ```
    def fibonacciI(n):
        '''(int) -> int

        Recebe um inteiro não negativos n e calcula o
        n-ésimo número de fibonacci de forma iterativa.
        Retorna o valor calculado.
        '''
    ```
### Discussão

Procure medir os tempos dessas funções para os seguintes valores de n : [10, 20, 30, 40, 50].

Informe os resultados e tempos que você mediu em sua máquina e sugira no Discord formas para diminuir os tempos da versão recursiva.

### Roteiro

Leia o(s) texto(s) sugeridos na seção Leitura premilinar.

- Baixe o arquivo fibonacci.py para uma pasta do seu computador.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender o que você deve implementar.
- Implemente, documente e teste seu trabalho.
- Caso você deseje testar sua classe no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo fibonacci.py.

### Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

### Arquivos requeridos
##### fibonacci.py
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

def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''

    print("Vixe! ainda não fiz a função fibonacciR")

## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''

    print("Vixe! ainda não fiz a função fibonacciI")
```