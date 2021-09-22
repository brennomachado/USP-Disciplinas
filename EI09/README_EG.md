# EG09
Disponível a partir de: terça, 21 set 2021, 08:00
Data de entrega: terça, 21 set 2021, 10:30
Arquivos requeridos: eg_array2d.py ( Baixar)
Tipo de trabalho: Trabalho individual
# Exercício em time: EG da aula 09 - Classe Array2d

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

## Roteiro para realizar esse exercício

Para que a leitura não se torne cansativa, procure ler apenas um item por vez e reuna o time para realizar a atividade referente ao item, antes de passar ao próximo item.

**1.** Teste a classe Array2d usando uma função main() no mesmo arquivo array2d.py. Observe que a classe deve seguir as especificações constantes no enunciado.

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando **if \_\_name__** == **'\_\_main__'**: para chamar a função main() como ilustrado no último exercício em time.

**2.** Correção e testes individuais
    
    - Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
    - Cada pessoa do time deve testar sua classe usando a função main() com todos os testes e executar os testes e verificar se a classe passa em todos os testes.
    - Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

**3**. Desafio leve: Método resize()

    - O método resize() recebe uma tupla e altera a dimensão do Array2d. Deve retornar None.

    - Exemplo:
    ```
    a = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print(f'Criação do Array2d a:')
    a[0,0] = 1
    a[0,1] = 2
    a[1,1] = 4
    a[1,2] = 5
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    a.resize( (3,2) )
    print(f'novo a depois de resize:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    ```
    a saída desse trecho deve ser:

    ```
    Criação do Array2d a:
    1 2 3
    3 4 5
    shape: (2, 3)
    size : 6
    data : [1, 2, 3, 3, 4, 5]

    novo a depois de resize:
    1 2
    3 3
    4 5
    shape: (3, 2)
    size : 6
    data : [1, 2, 3, 3, 4, 5]
    ```

4. Desafio médio: Operadores de subtração e multiplicação elemento a elemento
    - Estenda o comportamento da classe Array2d para que ela ofereça o comportamento como ilustrado no trecho de código abaixo.

    ```
    a = Array2d( (2,3), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    b = Array2d( (2,3), 7)   # criar Array2d com valor inicial 7
    print(f'teste 2: Criação do Array2d b:')
    print(b)
    print(f'shape: {b.shape}')
    print(f'size : {b.size}')
    print(f'data : {b.data}')
    print()

    # sub e rsub
    x = a - b
    print(f'teste: x = a - b ')
    print(x)  
    print()

    y = a - 2
    print(f'teste: y = a - 2 ')
    print(y) 
    print()

    z = 3.14 - b
    print(f'teste: z = 3.14 - b ')
    print(z) 
    print()

    # mul e rmul
    c = a * x
    print(f'teste: c = a * x ')
    print( c )  
    print()

    d = c * -1
    print(f'teste: d = c * -1 ')
    print( d ) 
    print()

    e = 0.5 * b
    print(f'teste: e = 0.5 * b ')
    print( e ) 
    print()
    ```
    
    A saída desse trecho deve ser:

    ```
    teste 1: Criação do Array2d a:
    3 3 3
    3 3 3
    shape: (2, 3)
    size : 6
    data : [3, 3, 3, 3, 3, 3]

    teste 2: Criação do Array2d b:
    7 7 7
    7 7 7
    shape: (2, 3)
    size : 6
    data : [7, 7, 7, 7, 7, 7]

    teste: x = a - b 
    -4 -4 -4
    -4 -4 -4

    teste: y = a - 2 
    1 1 1
    1 1 1

    teste: z = 3.14 - b 
    -3.86 -3.86 -3.86
    -3.86 -3.86 -3.86

    teste: c = a * x 
    -12 -12 -12
    -12 -12 -12

    teste: d = c * -1 
    12 12 12
    12 12 12

    teste: e = 0.5 * b 
    3.5 3.5 3.5
    3.5 3.5 3.5
    ```

    Dica: lembre-se que o operador * corresponde ao método especial __mul__() (e __rmul__()) e o operador de subtração binária - corresponde ao método especial __sub__()(e __rsub__).

    Você pode estender a classe com outros operadores caso desejar.

**5.** Discussão:
        quais as vantagens de usar lista linear para representar um array2d?
        quais as vantagens de usar lista aninhadas para representar um array2d?
            como funcionaria o método resize() se o atributo data fosse uma lista aninhada?

O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo com prefixo eg_array2d.py contendo o seu trabalho.

Você também precisa responder o formulário individual cujo link foi fornecido durante a aula caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar a solução antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
## Arquivos requeridos
### eg_array2d.py