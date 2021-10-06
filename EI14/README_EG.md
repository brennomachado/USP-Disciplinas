# EG14
Disponível a partir de: terça, 5 out 2021, 08:00
Data de entrega: terça, 5 out 2021, 10:30
Arquivos requeridos: eg_recursao.py ( Baixar)
Tipo de trabalho: Trabalho individual
## Exercício em time: EG da aula 14 - Recursão

Não se esqueça de preencher o [Formulário Individual](https://forms.gle/W46bYdhZZS2hmhd3A)

Procurem ler as instruções para as atividades específicas em grupo

## Preparação para a atividade em time

As instruções gerais para as atividades em grupo estão aqui.

Basicamente você deve:

- voltar para a sala principal caso você esteja sozinhE.
- fazer uma cópia do seu EI, colocando o prefixo eg_. Assim, se o nome do arquivo EI for exercicio.py, o nome do arquivo a ser entregue será eg_exercicio.py. Vamos chamar esse arquivo de EG.
- sortear a pessoa “estagiária” e a pessoa “gerente” conforme as instruções.
- preencher o formulário individual conforme as instruções.

## Atividades específicas

A partir daqui sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.
Roteiro para realizar esse exercício

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

1. Teste as funções
    - **maxR()**
    - **somaR()**

    Certifique-se que as duas funções são recursivas.

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando **if \_\_name__ == '\_\_main__':** para chamar a função main() como ilustrado no último exercício em time.

2. Correção e testes individuais
    - Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
    - Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
    - Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

3. Desafio 1: Função iterativa para cálculo do n-ésimo número da sequência de Fibonacci de forma iterativa A sequência de Fibonacci é definida pela seguinte fórmula recursiva:

    Fn = Fn − 2 + Fn − 1

    considerando os valores iniciais F0 = 0 e F1 = 1, escreva a função iterativa
    ```
     def fibonacciI(n):
     '''(int) -> int

     Recebe um inteiro não negativos n e calcula o
     n-ésimo número de fibonacci de forma iterativa.
     Retorna o valor calculado.
     '''
    ```
4. Desafio 2: Escreva a função recursiva para calcular o n-ésimo elemento da sequência de Fibonacci:
    ```
     def fibonacciR(n):
     '''(int) -> int

     Recebe um inteiro não negativos n e calcula o
     n-ésimo número de fibonacci de forma recursiva.
     Retorna o valor calculado.
     '''
    ```
5. Experimento 1:

Copie o seguinte trecho de código para um arquivo experimento_fibonacci.py, que deve estar na mesma pasta que o seu arquivo eg_recursao.py. Execute o experimento para ver a diferença entre o desempenho dessas duas soluções.


    ```
    """
    Experimento: comparação do desempenho entre uma solução iterativa 
    e outra recursiva para cálculo de um elemento da sequência de Fibonacci.
    """
    from eg_recursao import fibonacciI 
    from eg_recursao import fibonacciR 
    
    #---------------------------------------------------------    
    def exp():
        print("Experimento: Fibonacci Iterativo x Recursivo\n")
        print(f"n\tIterativo\tRecursivo")
        for n in range(50):
            ti = cronometro(fibonacciI, n)
            tr = cronometro(fibonacciR, n)
            print(f"{n:4}\t{ti}\t{tr}")

    #---------------------------------------------------------    
    def cronometro(funcao, n):
        '''(int,int) -> float

        Recebe uma função e um inteiro positivo e mede o tempo de execução
        de uma execução de funcao(n).
        '''
        import timeit
        wrapped = wrapper(funcao,n) 
        total_time = timeit.timeit(wrapped, number = 1)
        return total_time

    #----------------------------------------------------------      
    def wrapper(func, n):
        def wrapped():
            valor = func(n)
            print(valor)
        return wrapped
    #---------------------------------------------------------    
    exp()
    ```

5. Desafio 3: Binomial iterativo e recursivo

Escreva as funções binomialI(n, k) e binomialR(n, k) que recebem inteiros não-negativos n e k e calcula o valor do número binomial(n,k) de forma iterativa e recursiva, respectivamente.

Para resolver esse exercício, derive a fórmula recursiva para calcular o binomial(n, k). A fórmula pode ser derivada do Triângulo de Pascal, como ilustrado abaixo, onde n representa o número de uma linha e k o número de uma coluna.

  k 0   1   2   3   4   5   6
n
0   1   1   1   1   1   1   1
1   1   2   3   4   5   6   
2   1   3   6   10  15
3   1   4   10  20
4   1   5   15  
5   1   6
6   1

Por exemplo, o triângulo mostra que:

- o binomial(4,2) é 15;
- binomial(1,3) é 4; e
- binomial(3,2) é 10.

Modifique o experimento para comparar o desempenho dessas duas formas, iterativa e recursiva, para cálculo do binomial.

## O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

- Você só precisa entregar o arquivo com extensão eg_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.
- Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.
- Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.
- Não serão aceitos EGs após encerrado o prazo de entrega.


## Arquivos requeridos
#### eg_recursao.py

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
