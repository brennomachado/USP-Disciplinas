EG20
Data de entrega: terça, 9 nov 2021, 11:00
Arquivos requeridos: eg_insercao.py ( [Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3960796))
Tipo de trabalho: Trabalho individual
Exercício EG20 - algoritmo de ordenação por inserção

Não se esqueça de preencher o [Formulário Individual](https://forms.gle/TWdbtE1A4PazxZ276)

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

    Teste as funções usando uma coletânea dos testes que cada um fez na função main().
        insira_ultimo(seq, n)
        ordene_por_insercao( seq )

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() do time e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando if __name__ == '__main__': para chamar a função main() como ilustrado no último exercício em time.

    Correção e testes individuais
        Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
        Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
        Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

    Desafio 1: você deve (re)implementar o algoritmo de ordenação por seleção para listas (já fizemos para blobs). Para isso, escreva no seu arquivo eg_insercao.py as seguintes funções:

     def maior_elemento(seq , n):
         ''' (lista, int) -> int

         Essa função é a base para o algoritmo de ordenação
         por seleção.

         RECEBE uma sequência de números em ordem aleatória.
         A função deve considerar apenas a porção de [0:n] de seq

         RETORNA o índice do maior elemento nessa porção.
         Em caso de empate deve retornar o maior índice.

         Exemplos:

         > maior_elemento([4,7,1,7,3], 5)  - retorna 3, índice do maior
         > maior_elemento([4,7,1,7,3], 3)  - retorna 1
         > maior_elemento([4,7,1,7,3], 1)  - retorna 0

         DICA: varra seq até n, procurando pelo elemento de maior valor.
         '''
         # escreva sua solução

     ## ==================================================================

     def ordene_por_selecao(seq):
         ''' (list) -> None

         A ideia de ordenação por seleção (selection sort) é considerar
         porções inicialmente de tamanho n, selecionar um elemento máximo
         e colocá-lo no final dessa porção. A ordenação deve continuar
         decrementando o tamanho da porção até chegar em uma porção
         de tamanho 1. Uma lista de tamanho 1 já está ordenada e assim
         o processo termina.

         A função recebe uma sequência de números em ordem aleatória.
         e retorna None. Ao terminar, seq deve estar em ordem
         crescente aplicando a ideia de ordenação por seleção.

         Essa função DEVE usar a função maior_elemento().

         '''

         # escreva sua solução

    Teste esses métodos com alguns casos simples, antes de prosseguir.

    Experimento 1: Vamos analisar o consumo de tempo do algoritmo de ordenação por seleção e por inserção.

        Discussão inicial:
            Qual algoritmo de ordenação possui menor consumo de tempo para sequências aleatórias?
            Qual algoritmo de ordenação possui menor consumo de tempo para sequências em ordem crescente?
            Qual algoritmo de ordenação possui menor consumo de tempo para sequências dem ordem decrescente?

        Baixe o seguinte experimento na mesma pasta onde se encontra o seu arquivo eg_insercao.py.
            SUGESTÃO: crie uma cópia e execute esse experimento no próprio colab.

        Execute o experimento e discuta os resultados e suas respostas para a discussão inicial, variando o valor da constante OPCAO no arquivo experimento para CRESCENTE e DECRESCENTE.

        Em caso de dúvida, chame seus professores.

    Desafio 2: Inserção com busca binária

    Observe que a inserção de um elemento realiza uma busca sequêncial para encontrar a posição correta de um novo elemento. Para melhorar o desempenho desse algoritmo, podemos primeiro realizar uma busca binária da posição correta e apenas deslocar o trecho sem realizar a busca, como no algoritmo abaixo:

    def ordene_por_insercao_binaria(seq):
        '''(list) -> None
        RECEBE uma lista `seq`.
        REARRANJA os itens de `seq` para que fiquem em ordem
        crescente.

        A função é uma implementação de ordenação por inserção
        binária.
        '''
        n = len(seq)
        for i in range(1, n):
            x = seq[i]
            # encontre posição de x
            j = busca_binaria(seq, lo=0, hi=i, x=x)
            # print(f"{seq}, i={i}, x={x}, j={j}")
            for k in range(i, j, -1):
                seq[k] = seq[k-1]
            # coloque x na sua posição
            seq[j] = x

        # fim

    O desafio 2 é implementar a função de busca binária que permita usar esse algoritmo de inserção binária.


    def busca_binaria(seq, lo, hi, x):
        '''(list, int, obj) -> int
        RECEBE uma lista crescente `seq[lo:hi]` e um valor `x`.

        RETORNA um índice j no intervalo [lo:hi+1].

        Caso lo <= j < hi então
            seq[j] <= x < seq[j+1]    # qdo seq[j+1] existir

        Note que, caso j == hi, então x é maior que todos os
        elementos de seq.
        '''
        # escreva sua solução

    Experimento 2: Quando vale a pena usar inserção binária?

    Modifique a constante PARES_DE_FUNCOES do arquivo experimento para comparar o consumo de tempo do algoritmo de inserção binária com o de ordenação por seleção.

    Rode o experimento de busca com valores distintos da constante OPCAO.
        Discussão 1: Para listas aleatórias, qual algoritmo tem melhor desempenho?
        Discussão 2: Para listas em ordem crescente (ou quase), qual algoritmo tem melhor desempenho?
        Discussão 3: Para listas em ordem decrescente (ou quase), qual algoritmo tem melhor desempenho?

    Experimento 3: Inserção binária é sempre melhor que o algoritmo de inserção simples?

    Modifique a constante PARES_DE_FUNCOES do arquivo experimento para comparar o consumo de tempo do algoritmo de inserção binária com o de ordenação por inserção por busca sequencial.

    Rode o experimento de busca com valores distintos da constante OPCAO.
        Discussão 1: Para listas aleatórias, qual algoritmo tem melhor desempenho?
        Discussão 2: Para listas em ordem crescente (ou quase), qual algoritmo tem melhor desempenho?
        Discussão 3: Para listas em ordem decrescente (ou quase), qual algoritmo tem melhor desempenho?

O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg\_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com extensão eg\_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
Arquivos requeridos
eg_insercao.py
