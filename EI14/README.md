# EI14
Data de entrega: quinta, 7 out 2021, 08:00
Arquivos requeridos: recursao.py ( Baixar)
Tipo de trabalho: Trabalho individual

## Recursão

Vamos fazer uma pausa na descrição de tipos de dados abstratos para introduzir o conceito de recursão.

Recursão é um método de solução de problemas que visa quebrar o problema em subproblemas menores, em geral fazendo a função chamar ela mesma, até alcançar um problema simples o bastante para ser resolvido trivialmente. O uso de algoritmos recursivos nos permite escrever soluções elegantes para problemas que, de outra forma, seriam muito difíceis de programar.

## Leituras preliminares

 - [Recursão](https://panda.ime.usp.br/pensepy/static/pensepy/12-Recursao/recursionsimple-ptbr.html)

## O que você deve fazer

Você deve escrever duas funções recursivas:

  - função somaR()
    
    ```
    def somaR( lista ):
        ''' (list) -> int
            recebe uma lista de numeros inteiros e retorna a soma de todos os elementos da lista.
            Exemplo: 
            - para a entrada [12, -15, 7], a funcao deve retornar 4.
            - para a entrada [51], a funcao deve retornar 51.
            - para a entrada [], a funcao deve retornar 0 (zero).

            OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
            não use a função nativa sum() do Python para resolver esse exercício.
        '''
    ```
- função maxR()
    ```
    def maxR( lista ):
        ''' (list) -> int
            recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
            Exemplos: 
            - para a entrada [12, 15, 7], a funcao deve retornar 15.
            - para a entrada [51], a funcao deve retornar 51.
            - para a entrada [], a funcao deve retornar None.

            OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
            não use a função nativa max() do Python para resolver esse exercício.
        '''
    ```

## Roteiro

Leia o(s) texto(s) sugeridos na seção Leitura premilinar.

- Baixe o arquivo recursao.py para uma pasta do seu computador.
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

## Arquivos requeridos
#### recursao.py
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

    print("Testes das suas funções recursivas \n")

## ------------------------------------------------------------------

def maxR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
        Exemplos: 
        - para a entrada [12, 15, 7], a funcao deve retornar 15.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar None.

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa max() do Python para resolver esse exercício.
    '''

    print("Vixe! ainda não fiz a função maxR.")

## ------------------------------------------------------------------

def somaR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna a soma de todos os elementos da lista.
        Exemplo: 
        - para a entrada [12, -15, 7], a funcao deve retornar 4.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar 0 (zero).

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa sum() do Python para resolver esse exercício.
    '''

    print("Vixe! ainda não fiz a função somaR.")

## ------------------------------------------------------------------

if __name__ == '__main__':
    main()
```