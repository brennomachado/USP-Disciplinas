# EG17
Data de entrega: terça, 26 out 2021, 11:00
Arquivos requeridos: blobs.py ( Baixar)
Tipo de trabalho: Trabalho individual
## Exercício em time: EG da aula 17 - Análise do desempenho de arrays, listas e conjuntos.

Não se esqueça de preencher o Formulário Individual

Procurem ler as instruções para as atividades específicas em grupo

### Preparação para a atividade em time

As instruções gerais para as atividades em grupo estão aqui.

Basicamente você deve:

- voltar para a sala principal caso você esteja sozinhE.

- fazer uma cópia do seu EI, colocando o prefixo eg_. Assim, se o nome do arquivo EI for exercicio.py, o nome do arquivo a ser entregue será eg_exercicio.py. Vamos chamar esse arquivo de EG.

- sortear a pessoa “estagiária” e a pessoa “gerente” conforme as instruções.

- preencher o formulário individual conforme as instruções.
--- 
### Atividades específicas

A partir daqui sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.

--- 
#### Roteiro para realizar esse exercício

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

__1.__ Teste as funções do seu EI e verifique se obedecem à especificação.
  - pinte_blob() e
  - segmente_blob() e segmente_blob_RM(), certifique-se que ela é recursiva.

Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

Inclua o comando if \_\_name__ == '\_\_main__': para chamar a função main() como ilustrado no último exercício em time.
    

__2.__ Correção e testes individuais
        Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
        Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
        Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

__3. Desafio 1:__ Escreva a função segmente_blob_RML() que deve se comportar da mesma forma que sua função segmente_blob_RM(), mas deve usar listas ao invés de conjuntos. Use a função segmente_blob_list() abaixo como interface para a sua função segmente_blob_RML().

```
    def segmente_blob_list( img, semente ):
        ''' (ndarray, tuple) -> lista

            interface para a função segmente_blob_RML.
            Cria uma lista vazia que é carregada
            de forma recursiva por segmente_blob_list

            Não altere essa função.
        '''
        return segmente_blob_RML( img, semente, [] )

    def segmente_blob_RML( img, semente, visitados ):
        ''' (ndarray, tuple, lista) -> lista
        '''
        # escreva sua função aqui
```
__4. Experimento 1:__ análise do consumo de tempo dos algoritmos

  - Inclua essas funções segmente_blob_list() e segmente_blob_RML() no seu arquivo eg_blobs.py.

  - Baixe o seguinte experimento na mesma pasta onde se encontra o seu arquivo eg_blobs.py.
    - SUGESTÃO: crie uma cópia e execute esse experimento no próprio colab.

  - Execute o experimento e procure responder às seguintes perguntas discutindo com seus colegas de time:
    - Quantos pixels tem uma imagem de tamanho np × np? Quando np dobra, qual a razão de pixels entre a nova imagem e a anterior?
    - Imagine uma função pertence(elemento, lista), que retorna True se o elemento está na lista e False caso contrário. Discuta como você implementaria essa função e responda:
        - O consumo de tempo dessa função pertence() depende do tamanho da lista?
        - Existe um melhor caso, quando a função termina mais rápido? Qual seria?
        - Existe um pior caso, quando a função demora mais para terminar? Qual seria?
        - Imaginando o melhor caso, caso o tamanho da lista dobre, o que acontece com o consumo de tempo?
        - Imaginando o pior caso, caso o tamanho da lista dobre, o que acontece com o consumo de tempo?

    - Qual o consumo de tempo que você espera para o comando in, que verifica se um elemento está dentro ou não em uma lista (ou conjunto) de tamanho n? Esse tempo é constante ou depende de n?

    - se o consumo de tempo de in depender linearmente de n (número de pixels de um blob), quando n dobra quanto deve aumentar o consumo de tempo da função segmente_blob()?

    - se o consumo de tempo de in for constante, ou seja, não depende de n (número de pixels de um blob), quando n dobra quanto deve aumentar o consumo de tempo da função segmente_blob()?

    - baseado no experimento, você pode afirmar qual o consumo de tempo de in para listas (tipo list) e de in para conjuntos (tipo set)?

__5. Desafio 2:__ vamos remover o in usando arrays do Numpy.

Ao invés de representar uma blob como conjunto de tuplas, vamos representar uma blob como um array de zeros e uns, onde zeros são posições que não pertecem à região conexa. A ideia então é usar um array como memória de rascunho e marcar no rascunho os pontos da blob.

Escreva a função segmente_blob_RMA() que deve se comportar da mesma forma que sua função segmente_blob_RM(), mas deve usar arrays ao invés de conjuntos. Use a função segmente_blob_array() abaixo como interface para a sua função segmente_blob_RMA().
```
    def segmente_blob_array( img, semente ):
        ''' (ndarray, tuple) -> array

            interface para a função segmente_blob_RMA.
            Cria um array vazio que é carregado
            de forma recursiva.  

            Não altere essa função.
        '''

        visitados = img.copy()
        visitados[:,:] = 0  # limpa o array para indicar nenhuma posição visitada
        return segmente_blob_RMA( img, semente, visitados )

    def segmente_blob_RML( img, semente, visitados ):
        ''' (ndarray, tuple, array) -> array
        '''
        # escreva sua função aqui
```

__6. Experimento 2:__ use o código do experimento para comparar o desempenho da função segmente_blob_array() com as versões usando conjunto e listas. Discuta:

  - A função segmente_blob_array() não usa in. Portanto ela deve ser mais rápida que as demais. Essa afirmação está correta ou incorreta?

  - Qual o consumo de memória da função segmente_blob_array()? Esse consumo é constante ou depende do tamanho do blob?

  - Qual o consumo de memória da função segmente_blob_set()? Esse consumo é constante ou depende do tamanho do blob?

#### O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com extensão eg_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.

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

def segmente_blob( img, semente ):
    ''' (ndarray, tuple) -> set

        interface para a função segmente_blob_RM.
        Cria um conjunto vazio que é carregado
        de forma recursiva.  
        
        Não altere essa função.
    '''
    return segmente_blob_RM( img, semente, set() )

def segmente_blob_RM( img, semente, visitados ):
    ''' (ndarray, tuple, set) -> set

    Recebe um ndarray img e uma tupla semente contendo a
    coordenada de um pixel de img. Recebe também o conjunto
    visitados, que contém as coordenadas dos pixels já 
    visitados.

    DICA: uma ideia de algoritmo recursivo é
    - se a semente já foi visitada, retorna None.
    - caso contrário, 
        - marca a semente como visitada e
        - propaga recursivamente para os vizinhos de mesma cor.
    '''

    print("Vixe! Ainda não fiz a função semente_blob_RM.")

## ==================================================================

def pinte_blob( img, blob, nova_cor = 0):
    ''' (ndarray, set, int) -> None

    Recebe um ndarray img e um conjunto de pixels blob
    e pinta esses pixels com a nova_cor.

    '''

    print("Vixe! Ainda não fiz a função pinte_blob.")

## ==================================================================
## Coloque aqui outras funções que desejar

```