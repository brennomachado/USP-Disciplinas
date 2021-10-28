# EG18
Data de entrega: quinta, 28 out 2021, 13:00
Arquivos requeridos: eg_blobs.py ([Baixar](https://edisciplinas.usp.br/mod/vpl/views/downloadrequiredfiles.php?id=3943260))
Tipo de trabalho: Trabalho individual
## Exercício em time: EG da aula 18 - busca e ordenação de blobs

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

__1.__  Teste sua classe Blobs. Em particular a criação de um objeto Blobs que deve utilizar o método self.segmente().
    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.
    Inclua o comando if __name__ == '__main__': para chamar a função main() como ilustrado no último exercício em time.

__2.__ Correção e testes individuais
 - Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
 - Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
 - Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

__3.__ Desafio 1: o tamanho de uma blob é uma informação relevante para detectar objetos em uma imagem. Os maiores blobs podem corresponder ao fundo ou a partes de objetos dominantes, como a barriga do Fred Flintstone. Para pintar os blobs em ordem decrescente de tamanho, vamos implementar nesse laboratório um algoritmo de ordenação por seleção. Escreva no seu arquivo eg_blobs.py os seguintes métodos:
```
     def max_blob(self, n=None):
         ''' (Blobs, int) -> int

         Recebe um inteiro n > 0 que indica a porção da 
         lista self.data a ser procurada. Caso n seja None,
         a porção deve ser a lista self.data inteira.

         Retorna o índice da maior blob da porção da lista a ser 
         procurada, ou seja, no intervalo [0:n]. 
         Em caso de empate entre duas blobs de mesmo tamanho, 
         deve retornar o maior índice.

         Exemplo: 
         Lembre-se que a lista self.data é uma lista de blobs.
         Assumindo que essa lista tenha blobs de tamanhos
         [5, 7, 3, 7, 10, 4] então:
         - a chamada max_blobs( 3 ) deve retornar o índice 1
         - a chamada max_blobs( 4 ) deve retornar o índice 3
         - a chamada max_blobs(   ) deve retornar o índice 4

         '''
         # escreva sua solução

     ## ==================================================================

     def ordena_por_selecao(self):
         ''' (Blobs) -> None
         Ordena a lista self.data em ordem crescente de tamanho.
         A ideia do algoritmo de ordenação por seleção é a seguinte:
         - repita n vezes:
             - ache o índice do valor do máximo elemento dentro da porção da 
                 lista ainda não ordenada
             - troque essa blob com a blob no fim da porção não ordenada 
                 da lista. Observe que esse elemento agora está ordenado.
         Exemplo de execução da ideia para a lista [3, 7, 1, 4]:
             . passo 1: na porção não ordenada da lista (toda ela)
                 seleciona o máximo e troca com o último elemento. 
                 Resultado: [3, 4, 1, 7]. O último elemento está ordenado.
             . passo 2: na porção não ordenada da lista,
                 seleciona o máximo e troca com o último elemento da porção. 
                 Resultado [3, 1, 4, 7]. 
             . passo 3: na porção não ordenada da lista,
                 seleciona o máximo e troca com o último elemento. 
                 Resultado [1, 3, 4, 7]. 
             . passo 4: o último elemento sempre está na posição correta. 
             . fim.

         REQUISITO: use o método self.max_blob().
         '''    
         # escreva sua solução
```
Teste esses métodos com alguns casos simples, antes de prosseguir.

__4.__ Experimento 1: Vamos analisar o consumo de tempo do algoritmo de ordenação por seleção usando algumas imagens.

 - Baixe essas imagens [eg18_imagens.zip](https://drive.google.com/file/d/1DMYaBe9LkKKVA7mjf05hNXl6x05zZkKG/view?usp=sharing), unzipe o arquivo e coloque todas as imagens na mesma pasta do arquivo eg_blobs.py.

 - Baixe o seguinte [experimento](https://colab.research.google.com/drive/1t8bnh2Nq_yM8BiDJ10sy5IZxL42WyzsF?usp=sharing) na mesma pasta onde se encontra o seu arquivo eg_blobs.py.
   - SUGESTÃO: crie uma cópia e execute esse experimento no próprio colab.

 - Execute o experimento e discuta os resultados.

    - DICA 1: 
      - Tecle “ENTER” para pintar as regiões em ordem decrescente.
      - Digite “ENTER” várias vezes para cada imagem para entender melhor o comportamento do algoritmo de segmentação.
      - Varie a constante “NIVEIS_DE_CINZA”, para alterar o número de blobs segmentadas, por exemplo para 8 e 32.

    - DICA 2:
      - Tecle “i + ENTER” para experimentar a próxima imagem.
    - DICA 3: Tecle “q + ENTER” para sair do experimento.
    - Discussão: considerando o tamanho da lista de blobs, qual o consumo de tempo da ordenação por seleção?
      - Imagine que a lista já esteja ordenada de forma crescente. Qual seria o consumo de tempo do algoritmo de ordenação por seleção nesse caso?

      - Imagine que a lista já esteja ordenada de forma decrescente. Qual seria o consumo de tempo do algoritmo de ordenação por seleção nesse caso?

      - Imagine que a lista tenha seus elementos em ordem aleatória, sem ordenação. Qual seria o consumo de tempo do algoritmo de ordenação por seleção nesse caso?

__5.__ Desafio 2: tamanho das blobs

Um problema desse algoritmo simples de segmentação é o surgimento de um grande número de blobs de tamanhos muito pequenos. Parte desse problema pode ocorrer por ruidos na imagem e variações de cor e sobreamento.

Para ver o que acontece, implemente o método abaixo em sua classe Blobs:

```
    def busque_blob(self, size, ini):
        ''' (Blobs, int, int) -> list

        Recebe um inteiro size que indica qual tamanho de blob
        desejamos buscar. A busca deve começar a partir do índice ini
        da lista self.data.

        Retorna o índice da 1a ocorrência de uma blob de tamanho size 
        na lista self.data, a partir do índice ini.
        Retorna None caso não encontrar nenhuma blob com esse tamanho.

        Exemplo: 
        Lembre-se que a lista self.data é uma lista de blobs.
        Assumindo que essa lista tenha blobs de tamanhos
        [5, 7, 3, 7, 10, 4] então:
        - a chamada busque_blob( 7, 0 ) deve retornar 1.
        - a chamada busque_blob( 7, 3 ) deve retornar 3.
        - a chamada busque_blob( 7, 4 ) deve retornar None.
        - a chamada busque_blob( 4, 3 ) deve retornar 5.
        - a chamada busque_blob( 8, 0 ) deve retornar None.
        '''    
        # escreva sua solução
```
__6.__ Experimento 2: blobzinhas x blobzonas

Modifique a constante EXP_ORDENACAO do arquivo experimento para False. Isso vai fazer com que o experimento de busca seja executado ao invés da ordenação.

Rode o experimento de busca com valores distintos de NIVEIS_DE_CIINZA para ver o que acontece com as blobzinhas. Modifique os valores das constantes MENOR_BLOB e MAIOR_BLOB para marcar blobs de outros tamanhos (médios e grandes).
  - __Discussão 1:__ Analise o algoritmo usado no método busque_blob(). Qual o consumo de tempo esperado para buscar um certo tamanho de blob em função do tamanho n da lista?
    - Existe um melhor caso para a busca, em termos de consumo mínimo de tempo? Qual seria?
    - Existe um pior caso, de consumo máximo? Qual seria?
  - __Discussão 2:__ Para buscar blobs de mesmo tamanho, podemos usar o método a partir do índice onde do último elemento encontrado. Nesse caso, o que acontece com n?
  - __Discussão 3:__ É correto ou incorreto dizer que o consumo de tempo para pegar todos os blobs de um tamanho pequeno é o mesmo que o consumo para pegar todos os blobs de um tamanho grande (perto do máximo)?
  - __Discussão 4:__ Se a lista estivesse ordenada, seria possível inventar um algoritmo de busca mais eficiente?

#### O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com extensão eg_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.

### Arquivos requeridos
##### eg_blobs.py
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