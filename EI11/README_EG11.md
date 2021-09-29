# EG11
Disponível a partir de: terça, 28 set 2021, 08:00
Data de entrega: terça, 28 set 2021, 10:30
Arquivos requeridos: eg_array2d.py ( Baixar)
Tipo de trabalho: Trabalho individual
## Exercício em time: EG da aula 11 - Numpy

Não se esqueça de preencher o Formulário Individual

Procurem ler as instruções para as atividades específicas em grupo
Preparação para a atividade em time

As instruções gerais para as atividades em grupo estão aqui.

Basicamente você deve:
- voltar para a sala principal caso você esteja sozinhE.
- fazer uma cópia do seu EI, colocando o prefixo eg_. Assim, se o nome do arquivo EI for exercicio.py, o nome do arquivo a ser entregue será eg_exercicio.py. Vamos chamar esse arquivo de EG.
- sortear a pessoa “estagiária” e a pessoa “gerente” conforme as instruções.
- preencher o formulário individual conforme as instruções.

## Atividades específicas

A partir daqui sugerimos que o gerente leia as instruções em voz alta para que todos possam acompanhar a leitura e colaborar para o seu entendimento.
Roteiro para realizar esse exercício

Ao realizar essas atividades, procure entender o comportamento de objetos do tipo ndarray.

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

1. Teste os métodos
   - getlin()
   - getcol()
   - dot()
   - e a função matmul() da classe Array2d usando uma (nova?) função main() no mesmo arquivo array2d.py.

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.
    
    Inclua o comando if __name__ == '__main__': para chamar a função main() como ilustrado no último exercício em time.

2. Correção e testes individuais
     - Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
     - Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
     - Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

3. Desafio 1: Escreva a função
    ```
     def marque_regiao(ar, esq, sup, dir, inf, valor=0):
         '''(Array2d, int, int, int, int, num) -> None
         Recebe um objeto Array2d e par de inteiros (esq,sup) 
         que indica o canto esquerdo-superior e o par de 
         inteiros (dir,inf) que indica o canto direito-inferior 
         de uma região do Array2d e preenche os elementos dessa 
         região com "valor".
         ''' 
    ```
    Exemplo: o trecho de código a seguir:
    ```
    la = list(range(25))
    ar = Array2d((5,5), 0)
    ar.data = la  ## ou use carregue
    print("Array:")
    print(ar)
    print()

    e, s, d, i = 1, 2, 3, 4
    marque_regiao(ar, e, s, d, i, -1)
    print(f"Região ({e},{s})x({d},{i}) do Array marcado com -1:")
    print(ar)
    print()
    ```
    deve resultar na saída (dos prints):
    ```
    Array:
    0 1 2 3 4
    5 6 7 8 9
    10 11 12 13 14
    15 16 17 18 19
    20 21 22 23 24

    Região (1,2)x(3,4) do Array marcado com -1:
    0 1 2 3 4
    5 6 7 8 9
    10 -1 -1 13 14
    15 -1 -1 18 19
    20 21 22 23 24
    ```
4. Desafio 2: Escreva a função
    ```
     def marque_regiao_np(ar, esq, sup, dir, inf, valor=0):
         '''(np.ndarray, int, int, int, int, num) -> None
         Recebe um ndarray do Numpy, um par de inteiros (esq,sup) 
         que indica o canto esquerdo-superior e o par de inteiros 
         (dir, inf) que indica o canto direito-inferior de uma 
         região do Array e preenche os elementos dessa região com "valor". 
         '''
    ```
    Essa função deve ter comportamento idêntico a função anterior marque_regiao(), mas agora usando um np.ndarray. Procure resolver esse exercício usando fatias do ndarray.

5. Discussão 1:
   - Será que a função marque_regiao() funciona também se passarmos um np.ndarray? Justifique.
   - Será que a função marque_regiao_np() funciona também se passarmos um Array2d? Justifique.

6. Desafio 3: Escreva a função
    ```
    def rotacione( ar ):
    ''' (Array2d) -> None
    Recebe um Array2d ar de dimensão quadrada e retorna None.
    Antes de retornar, gira ar de 90 graus no sentido anti-horário.
    '''
    ```
    Exemplo: o trecho de código a seguir:

    ```
    la = list(range(25))
    ar = Array2d((5,5), 0)
    ar.data = la  ## ou use carregue
    print("Array:")
    print(ar)
    print()

    rotacione(ar)
    print("Resultado de rotacione(ar):")
    print(ar)
    ```
    deve resultar na saída (dos prints):

    ```
    Array:
    0 1 2 3 4
    5 6 7 8 9
    10 11 12 13 14
    15 16 17 18 19
    20 21 22 23 24

    Resultado de rotacione(ar):
    4 9 14 19 24
    3 8 13 18 23
    2 7 12 17 22
    1 6 11 16 21
    0 5 10 15 20
    ```
7. Desafio 4: Escreva a função
    ```
    def rotacione_np( ar ):
    ''' (np.ndarray) -> None
    Recebe um np.ndarray ar de dimensão quadrada e retorna None.
    Antes de retornar, gira ar de 90 graus no sentido anti-horário.
    '''
    ```

    Essa função deve ter comportamento idêntico a função anterior rotacione(), mas agora usando um np.ndarray. Procure resolver esse exercício usando fatias do ndarray.

### O que você deve entregar para conseguir um bônus

- Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

- Você só precisa entregar o arquivo com extensão eg_ contendo os novos métodos e/ou funções implementados, inclusive a main() utilizada para testes.
- Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.
- Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.
- Não serão aceitos EGs após encerrado o prazo de entrega.


## Arquivos requeridos
#### eg_array2d.py
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

    print("Testes da classe Array2d\n")


## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        print("Vixe! ainda não fiz o construtor da classe.")

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        print("Vixe! ainda não fiz o método __getitem__.")

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        print("Vixe! ainda não fiz o método __setitem__.")

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        print("Vixe! ainda não fiz o método __str__.")

    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar


## ==================================================================

if __name__ == '__main__':
    main()
```