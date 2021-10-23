EG16
Disponível a partir de: quinta, 21 out 2021, 10:00
Data de entrega: quinta, 21 out 2021, 13:00
Arquivos requeridos: eg_binomial.py ( Baixar)
Tipo de trabalho: Trabalho individual
Exercício em time: EG da aula 16 - Análise do algoritmo de cálculo do binomial recursivo com memoização

Não se esqueça de preencher o Formulário Individual

Procurem ler as instruções para as atividades específicas em grupo
Preparação para a atividade em time

As instruções gerais para as atividades em grupo estão aqui.

Basicamente você deve:

    voltar para a sala principal caso você esteja sozinhE.

    fazer uma cópia do seu EI, colocando o prefixo eg_. Assim, se o nome do arquivo EI for exercicio.py, o nome do arquivo a ser entregue será eg_exercicio.py. Vamos chamar esse arquivo de EG.

    sortear a pessoa “estagiária” e a pessoa “gerente” conforme as instruções.

    preencher o formulário individual conforme as instruções.

Atividades específicas

A partir daqui sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.
Roteiro para realizar esse exercício

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

    Teste as funções do seu EI e verifique se obedecem à especificação.
        binomialI(),
        binomialR(), que foi completamente dada no EI16 e
        binomialRM(), certifique-se que ela é recursiva.

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando if __name__ == '__main__': para chamar a função main() como ilustrado no último exercício em time.

    Correção e testes individuais
        Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
        Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
        Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

    Discussão 1: Uma versão recursiva SEM memoização para calcular o binomial(n,k) pode ser escrita usando a regra binomial(n, k) = binomial(n − 1, k − 1) + binomial(n − 1, k) conforme abaixo.

    def binomialR0(n, k):
        '''(int, int) -> int
        RECEBE inteiros não negativos n e k e 
        RETORNA o valor de binomial(n,k) calculado de forma recursiva
        e sem o uso de memoização.

        Objetivo: queremos analisar o consumo de tempo dessa solução
        sem memória extra.
        '''
        # confira esses casos base do triângulo de Pascal
        if n < k: return 0    
        if n == k or k == 0: return 1
        return binomialR0(n-1, k) + binomialR0(n-1, k-1)

        Analise esse algoritmo e procure responder qual a relação entre n e k que exige mais chamadas recursivas de binomialR0(n, k)?

    Para responder essa pergunta, procure discutir com seus colegas de time:

        Para binomialR0(5,1), quantas vezes a função é chamada recursivamente?

        Dica:

            binomialR0(5, 1) depende de binomialR0(4,1) e binomialR0(4,0)

            binomialR(5, 1) 
                - binomialR(4, 1)
                    - binomialR(3,1)
                        - binomialR(2,1)
                            - binomialR(1,1)  -> retorna 1
                            - binomialR(1,0)  -> retorna 1
                        - binomialR(2,0)  -> retorna 1
                    - binomialR(3,0)  -> retorna 1
                - binomialR(4, 0)  -> retorna 1

        Para binomialR0(5,3), quantas vezes a função é chamada recursivamente?

        Dica:

            binomialR(5,3) depende de binomialR(4,3) e binomialR(4,2)

            binomialR(5, 3) 
                binomialR(4,3)
                    - binomialR(3,3)          -> retorna 1
                    - binomialR(3,2) 
                        - binomialR(2,2)      -> retorna 1
                        - binomialR(2,1)
                            - binomialR(1,1)  -> retorna 1
                            - binomialR(1,0)  -> retorna 1
                binomialR(4,2)
                    - binomialR(3,2) 
                        - binomialR(2,2)
                            - binomialR(1,2)  -> retorna 0
                            - binomialR(1,1)  -> retorna 1
                        - binomialR(2,1)
                            - binomialR(1,1)  -> retorna 1
                            - binomialR(1,0)  -> retorna 1
                    - binomialR(3,1) 
                        - binomialR(2,1)
                            - binomialR(1,1)  -> retorna 1
                            - binomialR(1,0)  -> retorna 1
                        - binomialR(2,0)      -> retorna 0

        e para n=6, quais valores de k exigem mais chamadas recursivas da função binomialR0(n,k)? Vamos dizer que esse é o pior caso pois é quando a função consome mais tempo de execução.

        Observe que, sem memoização, muitos valores são calculados repetidas vezes.

    Experimento 1: análise do consumo de tempo dos algoritmos no pior caso

        Inclua a função binomialR0() no seu arquivo eg_binomial.py.

        Baixe o seguinte experimento na mesma pasta onde se encontra o seu arquivo eg_binomial.py.
            SUGESTÃO: crie uma cópia e execute esse experimento no próprio colab.

        Execute o experimento e discuta os resultados.

            DICA 1: modifique a constante NUMERO_DE_ITERACOES do experimento ao avaliar a função binomialR0.

            DICA 2: os arrays do Numpy tem uma precisão finita que devem “explodir” (overflow) ao trabalhar com valores muito grandes. Para esse experimento, modifique o tipo dos arrays para float ao invés de int, apenas para que possamos observar o comportamento dessas funções com valores maiores. Lembre-se que, mesmo usando float, o experimento pode explodir para um número grande de iterações.

        Procurem responder as seguintes perguntas:
        Considerando a função binomialI(n,k), quando o valor de n dobra e k é algum valor fixo a sua escolha, o tempo de execução dessa função:
            permanece o mesmo?
            aumenta de algum fator alfa?
            dobra?
            mais que dobra?
        Considerando a função binomialR(n,k), quando o valor de n dobra e k é algum valor fixo a sua escolha, o tempo de execução dessa função:
            permanece o mesmo?
            aumenta de uma constante alfa?
            dobra?
            mais que dobra?
        Considerando a função binomialR0(n,k), quando o valor de n dobra e k é algum valor fixo a sua escolha, o tempo de execução dessa função:
            permanece o mesmo?
            aumenta de uma constante alfa?
            dobra?
            mais que dobra?

    Desafio 1: binomial usando fatorial

    o problema de cálculo do binomial(n,k) é muito rico em termos de algoritmos alternativos. Vamos implementar e discutir mais duas soluções. A primeira solução alternativa é baseada na fórmula:

    (nk)=n!k!(n−k)!

Utilize a função factorial() do módulo math do Python e escreva a função binomialFAT(n,k) que calcula binomial(n, k) baseado nessa equação e usando a função factorial().


from math import factorial

def binomialFAT(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k) calculado usando a 
    função factorial do módulo math.
    '''

    Discussão 1: você espera que o algoritmo usado em binomialFAT() seja mais rápido que binomialI()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

    Discussão 2: você espera que o algoritmo usado em binomialFAT() seja mais rápido que binomialR()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

    Discussão 3: você espera que o algoritmo usado em binomialFAT() seja mais rápido que binomialR0()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

    Experimento: use o código do experimento para testar suas respostas e aproveita para comparar se os resultados são iguais e qual a relação entre os tempos de cada algoritmo.

Desafio 3: binomial com recursão de cauda

Com um pouco mais de manipulação algébrica da equação podemos escrever,

(nk)=n!(n−k)!k!=(n−1)!(n−k)!(k−1)!×nk=…

Vamos deixar o resto dessa derivação para você como exercício, mas isso permite reescrever a função binomial usando uma forma mais simples de recursão, conhecida como recursão de cauda (tail recursion), semelhante à forma que usamos para ilustrar o cálculo do fatorial e soma de lista de forma recursiva, que é dada pela seguinte igualdade:

(nk)=(n−1k−1)×nk

Escreva a função recursiva binomialRC(n,k) que calcula ((n),k)

    baseado nessa igualdade com recursão de cauda (RC):


    def binomialRC(n, k):
        ''' (int, int) -> int
        RECEBE dois inteiros não negativos n e k.
        RETORNA o valor de binomial(n,k) calculado usando a 
        versão recursiva da função binomial com recursão de cauda.
        '''

        Discussão 1: você espera que o algoritmo usado em binomialRC() seja mais rápido que binomialI()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

        Discussão 2: você espera que o algoritmo usado em binomialRC() seja mais rápido que binomialR()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

        Discussão 3: você espera que o algoritmo usado em binomialRC() seja mais rápido que binomialR0()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

        Discussão 4: você espera que o algoritmo usado em binomialRC() seja mais rápido que binomialFAT()? Para n=10 e k=5, quantas vezes mais rápido ou mais lento? E para n=20 e k=10?

        Experimento: use o código do experimento para testar suas respostas e aproveita para comparar se os resultados são iguais e qual a relação entre os tempos de cada algoritmo.

O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com extensão eg_ contendo as funções do EI e as novas funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
Arquivos requeridos
eg_binomial.py
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

## CONSTANTES

DEBUG = False

## ==================================================================

def main():
    print("Vixe! ainda não fiz a função main")
    
## ==================================================================

def binomialI(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialI(3,2)  -> deve retornar 3
    b) binomialI(5,1)  -> deve retornar 5
    c) binomialI(1,5)  -> deve retornar 0
    d) binomialI(4,2)  -> deve retornar 6

    NOTA. Está função é iterativa.
    '''
    print("Vixe! ainda não fiz a função binomialI")

## ==================================================================

def binomialR(n, k):
    '''(int,int) -> int

    RECEBE inteiros não-negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialR(3,2)  -> deve retornar 3
    b) binomialR(5,1)  -> deve retornar 5
    c) binomialR(1,5)  -> deve retornar 0
    d) binomialR(4,2)  -> deve retornar 6

    NOTA. Está função é uma interface para a função 
          binomialRM() e não deve ser alterada.
    '''
    # cria um array de dimensão (n+1)x(k+1) para ser usado como rascunho
    #rascunho = np.full((n+1, k+1), 0, dtype=np.longlong) 
    rascunho = np.full((n+1, k+1), 0.0)
    rascunho[:,0] = 1

    bin = binomialRM(n, k, rascunho)
    if DEBUG:
        print("Debug ligado.")
        print(f"bin({n}, {k}) = {bin}")
        print(f"   Rascunho:\n{rascunho}")

    return bin

## ==================================================================

def binomialRM(n, k, rascunho):
    '''(int, int, array) -> int

    RECEBE inteiros não negativos n e k e um array bidimensional rascunho.
    RETORNA o valor de binomial(n,k).

    NOTA. Está função é recursiva.
        Ela usa as posições do array rascunho para  guardar os valores dos 
        binomiais já calculado: 
           - rascunho[i][j] armazenará o valor de binomial(i, j).
        Com isso a função evita que um mesmo número binomial seja recalculado 
        várias vezes.
    '''
    print("Vixe! ainda não fiz a função binomialRM")

## ==================================================================

def binomialR0(n, k):
    '''(int, int) -> int
    RECEBE inteiros não negativos n e k e 
    RETORNA o valor de binomial(n,k) calculado de forma recursiva
    e sem o uso de memoização.

    Objetivo: queremos analisar o consumo de tempo dessa solução
    sem memória extra.
    '''
    # confira esses casos base do triângulo de Pascal
    if n < k: return 0    
    if n == k or k == 0: return 1
    return binomialR0(n-1, k) + binomialR0(n-1, k-1)
    
## ==================================================================

def binomialFAT(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k) calculado usando a 
    função factorial do módulo math.
    '''
    print("Vixe! ainda não fiz a função binomialFAT")
        
## ==================================================================
def binomialRC(n, k):
    ''' (int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k) calculado usando a 
    versão recursiva da função binomial com recursão de cauda.
    '''
    print("Vixe! ainda não fiz a função binomialRC")
    
## ==================================================================

if __name__ == "__main__":
    main()
```