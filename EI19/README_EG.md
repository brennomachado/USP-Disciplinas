# EG19

Data de entrega: quinta, 4 nov 2021, 13:00
Arquivos requeridos: eg_busca.py ( [Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3943261))
Tipo de trabalho: Trabalho individual

## Exercício em time: EG da aula 19 - algoritmos de busca

Não se esqueça de preencher o Formulário Individual

Procurem ler as instruções para as atividades específicas em grupo

### Preparação para a atividade em time

As instruções gerais para as atividades em grupo estão aqui.

Basicamente você deve:

-   voltar para a sala principal caso você esteja sozinhE.

-   fazer uma cópia do seu EI, colocando o prefixo eg\_. Assim, se o nome do arquivo EI for exercicio.py, o nome do arquivo a ser entregue será eg_exercicio.py. Vamos chamar esse arquivo de EG.

-   sortear a pessoa “estagiária” e a pessoa “gerente” conforme as instruções.

-   preencher o formulário individual conforme as instruções.

---

### Atividades específicas

A partir daqui sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.

---

### Roteiro para realizar esse exercício

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

**1.** Teste as funções do arquivo eg_busca.py. Em particular verifique se:

-   a função busca_sequencial() varre a lista, sequencialmente.
-   busca_sequencial_em_lista_ordenada() aproveita, de alguma forma, que a lista está ordenada.
-   busca_binariaRED(), que é chamada de interface busca_binariaR(), é recursiva.

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando if \_\_name\_\_ == '\_\_main\_\_': para chamar a função main() como ilustrado no último exercício em time.

**2.** Correção e testes individuais

-   Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
-   Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
-   Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

**3.** Discussão 1: Considere a hipótese “O algoritmo busca_sequencial_em_lista_ordenada() se aproveita do fato da lista estar ordenada, portanto deve consumir menos tempo na média que o algoritmo busca_sequencial() em lista ordenada”. Qual dos seguintes algoritmos você acha que deve consumir mais tempo? E qual deve consumir menos tempo?

-   busca_sequencial() em lista não ordenada;
-   busca_sequencial() em lista ordenada;
-   busca_sequencial_em_lista_ordenada(), que só funciona em lista ordenada.

**4.** Experimento 1: Vamos analisar o consumo dos algoritmos de busca sequencial. Os experimentos sempre avaliam os algoritmos usando listas ordenadas. Mas todos os gráficos mostram o consumo de tempo do algoritmo de busca_sequencial() em lista NÃO ordenada, que corresponde a linha verde.

-   Baixe o seguinte [experimento](https://colab.research.google.com/drive/15VZLqDj_grvjUmE2IW4vDtJ3I9_V78WI?usp=sharing) na mesma pasta onde se encontra o seu arquivo eg_busca.py.

    -   SUGESTÃO: crie uma cópia e execute esse experimento no próprio colab.

-   verifique se o arquivo experimento está configurado como abaixo:

    ```
        PARES_DE_FUNCOES = [
            [ busca_sequencial, busca_sequencial_em_lista_ordenada ],
        #     [ busca_sequencial_em_lista_ordenada, busca_binariaR ],
        #     [ busca_binariaR, busca_binariaI ],
            ]
    ```

    caso não esteja, reconfigure o experiemnto para que avalie apenas esse par de funções.

-   Execute o experimento para avaliar o consumo dessas funções. Discuta com o seu time se esse é o comportamento esperado. Caso não seja e tenham alguma dúvida, converse com os seus professores.

**5.** Discussão 2: Uso de in e index, nativos do Python.

Substitua o corpo da função busca_sequencia() pelo seguinte trecho de código:

    ```
    if item in seq:
    return seq.index(item)
    return None

    ```

ou apenas coloque o trecho no início da função. Esse trecho usa o método index, que é equivalente ao algoritmo de busca sequencial. Isso deve tornar a função bem mais eficiente, a ponto de consumir menos tempo que as outras, correto? O que você acha?

Execute o experimento novamente para ver os resultados. Discuta o comportamento obtido.

**6.** Discussão 3: Pior caso ou caso médio?

Qual o melhor caso dos algoritmos? E o pior caso?

A constante FATOR_BUSCA_FORA do experimento deve estar com o valor 2. Isso significa que 1/2 das buscas é realizada “dentro” da lista. Modifique esse valor para 3 (1/3 das buscas dentro da lista) e para 1 (100% das buscas dentro da lista). Como você acha que o consumo de tempo dos algoritmos vai mudar?

**7.** Discussão 4: e o algoritmo de busca binária?

-   No pior caso, quando o tamanho da lista dobra, como varia o consumo de tempo dos algoritmos de busca sequencial? Sua conclusão está de acordo com os gráficos anteriores?
-   No pior caso, quando o tamanho da lista dobra, como varia o consumo de tempo do algoritmo de busca binária?
-   Qual o algoritmo que deve ter menor consumo de tempo?

No arquivo do experimento, remova o comentário da linha para que fique como no trecho abaixo:

    ```
        PARES_DE_FUNCOES = [
        #    [ busca_sequencial, busca_sequencial_em_lista_ordenada ],
                [ busca_sequencial_em_lista_ordenada, busca_binariaR ],
        #     [ busca_binariaR, busca_binariaI ],
            ]
    ```

Execute o experimento para verificar os resultados. Discuta os resultados e, em caso de dúvidas, converse com seus professores.

-   Pior caso x caso médio? Ao modificar a constante FATOR_BUSCAS_FORA, o que você acha que vai acontecer com o comportamento desses algoritmos?

**8.** Desafio: Implemente a função busca_binariaI(), que realiza a busca binária de forma iterativa, e a inclua em seu arquivo eg_busca.py.

-   altere a constante PARES_DE_FUNCOES para avaliar o desempenho das funções de busca binária recursiva e iterativa, e execute o experimento.

-   discuta com seu time se esse é o resultado que todos esperavam.

---

### O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg\_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com extensão eg\_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.

---

#### Arquivos requeridos

##### eg_busca.py

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
