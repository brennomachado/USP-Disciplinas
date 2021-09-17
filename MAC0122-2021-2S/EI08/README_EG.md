# EG08
Data de entrega: quinta, 16 set 2021, 12:30
Arquivos requeridos: eg_bem_formada.py ( Baixar)
Tipo de trabalho: Trabalho individual

## Exercício em time: EG da aula 08 - usos de pilha

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

1 Verifiquem se o EG segue a especificação como no enunciado. Em particular, verifiquem se:
  - A classe Pilha NÃO foi utilizada. A solução deve usar uma lista como se fosse pilha.
        A função bem_formada() trata sequências como parênteses, colchetes e chaves.
        A função bem_formada() ignora os caracteres que não sejam parênteses, colchetes e chaves.

    Caso vocês encontrem problemas, procurem corrigir a classe antes de continuar para o próximo item.

    Testes usando uma função main()
        Inclua no arquivo bem_formada.py uma função main() para testar a função bem_formada().

    Lembrem-se que a pessoa estagiária deve colocar os testes na main() e compartilhar esse EG com os demais membros do time para que todos possam testar os seus trabalhos individuais.

    Inclua o comando if __name__ == '__main__': para chamar a função main().

    Correção e testes individuais
        Cada pessoa do time deve verificar, com a ajuda de seus colegas quando necessário, se seu programa EI/EG está dentro da especificação. Não hesite em pedir ajuda a seu time em caso de dificuldade.
        Cada pessoa do time deve testar sua função bem_formada() usando a função main() e verificar se sua solução apresenta algum problema.
        Caso algum problema seja encontrado, discuta como resolvê-los com seus colegas de time.

    Desafio 1: extensão da função bem_formada() para tratar sequências com pares de ‘$’ além dos parênteses, colchetes e chaves.

    Diferente de parênteses, chaves e colchetes, que usam caracteres diferentes para abrir e fechar, seu time deve incluir sequências onde o símbolo ‘$’ também é usado para início e fim de um trecho. Por exemplo, as seguintes sequências são bem formadas:
        “$ $ { }”
        “[ $ { } $ ] $ ( $ $ $ $ ) $”

    Já as seguintes sequências não são bem formadas:
        “$ $ $”
        “$ { $ }”
        “( $ $ $ ) $”

    Sua função deve continuar a ignorar os demais caracteres.

    Desafio 2:

    A pilha é uma estrutura abstrata de dados com 1001 utilidades. A conversão entre bases numéricas é apenas um exemplo e objeto desse desafio.

    Vimos em exercícios anteriores que uma mesma informação pode ser representada de formas distintas, como uma fração que pode ser representado (aproximado) por um número real usando float. Números inteiros podem ser representados em qualquer base. Nós estamos acostumados a usar a base decimal, assim chamada pois usa 10 dígitos representados pelos caracteres de 0 a 9. Usando dois dígitos, 0 e 1, podemos representar números na base binária, que é uma forma muito mais apropriada, aliás, para representar inteiros em computadores eletrônicos atuais.

    Ao ler um número na base 10, como o número 123 (cento e vinte e três), cada dígito indica um fator multiplicador de uma potência da base, ou seja, 1 * 102 + 2 * 101 + 3 * 100 = 100 + 20 + 3. Da mesmo forma, ao ler um número na base 2 como 1011 devemos usar potencias de 2 para interpretar esse número de forma que 1011 equivale a 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 8 + 2 + 1, ou 11 na base decimal.

    E como converter o decimal 11 para um número binário? Uma solução é decompor o valor, como 11, divindindo pela base desejada, como 2, e empilhar os restos. O valor convertido fica armazenado na pilha, como descrito na seção Conversão de Decimal para Binário.

    Por exemplo, para converter 11 para binário usando uma pilha podemos fazer:


        início: valor 11 e pilha = []  # pilha vazia
        11 // 2 = 5 e resto 1.    
            Empilhamos o resto  =>  pilha = [1] e 
            continuamos o processo com o valor 5, obtido de 11//2.
         5 // 2 = 2 e resto 1.    
            Empilhamos o resto  =>  pilha = [1, 1] e 
            continuamos com o valor 2.
         2 // 2 = 1 e resto 0.    
            Empilhamos o resto  =>  pilha = [1, 1, 0] e 
            continuamos com 1.
         1 // 2 = 0 e resto 1.    
            Empilhamos o resto  =>  pilha = [1, 1, 0, 1] e 
            terminamos pois o valor chegou em 0.

    Ao final, o topo da pilha portanto possui o valor do dígito mais significativo. Basta portanto remover os elementos da pilha para compor o valor em binário.

    Escreva as funções dec2bin() e bin2dec() conforme os seguintes protótipos. Inclua essas funções no arquivo bem_formada.py e inclua testes na função main().

    def bin2dec( bin ):
        ''' (int) -> int
        Recebe um inteiro que representa um número na base binária e 
        retorna outro inteiro que representa o mesmo número na base decimal.
        Exemplo:
        >>> bin2dec( 11 )
        3
        >>> bin2dec( 1110 )
        14
        '''

    def dec2bin( dec ):
        ''' (int) -> int
        Recebe um inteiro que representa um número na base decimal e 
        retorna outro inteiro que representa o mesmo número na base binária.
        Exemplo:
        >>> dec2bin( 11 )
        1101
        >>> dec2bin( 5 )
        101
        '''

O que você deve entregar para conseguir um bônus

Para entregar o EG não é necessário modificar o cabeçalho do seu EI (exercício individual), ou seja, use o mesmo cabeçalho e faça as modificações que desejar no código do EI, seguindo ou não as discussões do time. Lembre-se de incluir o prefixo eg_ no nome do arquivo e de manter o formato .py para enviar seu EG.

Você só precisa entregar o arquivo eg_bem_formada.py contendo todas as funções que vocês implementaram.

Você também precisa responder o formulário individual cujo link se encontra no topo desse enunciado caso deseje concorrer ao bônus de ter participado do exercício em grupo.

Lembre-se de testar tudo antes de entregá-la e conferir suas respostas. O bônus recebido será 10% da nota do seu EG.

Não serão aceitos EGs após encerrado o prazo de entrega.
Arquivos requeridos
eg_bem_formada.py