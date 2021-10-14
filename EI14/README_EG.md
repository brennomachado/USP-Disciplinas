EG14
Disponível a partir de: quinta, 14 out 2021, 10:00
Data de entrega: quinta, 14 out 2021, 12:59
Arquivos requeridos: eg_recursao.py ([Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3901730))
Tipo de trabalho: Trabalho individual
Exercício em time: EG da aula 14 - Recursão

Não se esqueça de preencher o [Formulário Individual](https://forms.gle/9rN1rtW4Uq8p6RZC6)

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

    Teste as funções
        maxR()
        somaR()

    Certifique-se que as duas funções são recursivas.

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando if __name__ == '__main__': para chamar a função main() como ilustrado no último exercício em time.

    Correção e testes individuais
        Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
        Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
        Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

    Desafio 1: Escreva as funções iterativas maxI() e somaI() que deve varrer as listas usando um comando de repetição como for ou while.

     def maxI( lista ):
         ''' (list) -> int
             recebe uma lista de números inteiros e retorna o valor do maior elemento, de forma semelhante à função maxR(), mas dessa vez de
             forma iterativa, ou seja, usando um comando while ou for.

             OBS: Esse é um exercício para treinar a construção de uma função iterativa, não use a função max() nativa do Python.
         '''

         # escreva sua solução

     def somaI( lista ):
         ''' (list) -> int
             recebe uma lista de números inteiros e retorna a soma dos elementos da lista, de forma semelhante à função somaR(), mas dessa vez de
             forma iterativa, ou seja, usando um comando while ou for.

             OBS: Esse é um exercício para treinar a construção de uma função iterativa, não use a função sum() nativa do Python.
         '''

         # escreva sua solução

    Experimento 1: Compare o desempenho entre as versões iterativa e recursiva das funções soma e max.

    Baixe o seguinte [trecho de código](https://colab.research.google.com/drive/1o8430jldtWAPUUqnbmtXYDId3s-TgP4C?usp=sharing) na mesma pasta onde se encontra o seu arquivo eg_recursao.py.
    Execute o arquivo e discuta os resultados: qual versão deve ser mais eficiente, a recursiva ou a iterativa?

    Desafio 2: Escreva a função maxR2(), que evita o uso de fatias para melhorar o desempenho das funções recursivas.

Lembre-se que fatias de listas criam novas listas com conteúdo clonado dos pedaços correspondentes da lista original. Uma forma de eliminar o trabalho de copiar a lista para cada chamada recursiva é usar sempre a mesma lista e incluir um marcador que indica o tamanho “útil” da lista.

Por exemplo, observe o trecho de código abaixo que mostra uma versão da função recursiva somaR2() sem o uso de fatias:


    def somaR2( lista, n ):
        ''' (list, int) -> int
        recebe uma lista de números inteiros e um marcador n que indica
        o tamanho útil da lista, ou seja, o número de elementos da lista 
        que devem ser considerados na soma.
        Calcula a soma dos elementos da lista até o n-ésimo elemento, de 
        forma recursiva.
        '''
        if n == 0:
            return 0
        ultimo = lista[n-1]
        return somaR2(lista, n-1) + ultimo

Utilize essa ideia para escrever a função maxR2(). Teste suas novas funções recursivas.

    Experimento 2: avaliação de desempenho das novas funções recursivas somaR2() e maxR2().

Primeiro um TRUQUE para manter o mesmo protótipo de somaR(). Observe que somaR2() usa um parâmetro a mais que somaR(). Modifique o nome de sua função somaR() para somaR1() para usar essa segunda versão recursive nos experimentos de avaliação de desempenho.


    def somaR(lista):
        ''' (list) -> int
        '''
        n = len(lista)
        return somaR2(lista, n)

Repita o mesmo para sua função maxR(), alterando o nome da função anterior para maxR1(), antes de executar o experimento de avaliação de desempenho.

Execute novamente o experimento, agora com a nova versão das funções recursivas. Discuta com o seu time:

    Qual foi a melhora de desempenho ao utilizar as funções R2 (sem fatias) sobre as versões R1 (com fatias)?
    Essa diferença depende da máquina ou é resultado do algoritmo?
    As versões iterativas tem desempenho superior ou inferior às versões R2? Por quê?

O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com extensão eg_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
Arquivos requeridos
eg_recursao.py

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