# EI08
Data de entrega: quinta, 16 set 2021, 08:00


# Sequência bem formada usando lista como se fosse uma pilha

## Objetivos
O objetivo deste exercício é continuar a treinar o uso do tipo abstrato de dados pilha. Vamos aproveitar para revisar o uso de listas e strings em Python.

## Resumo

Uma lista do Python pode ser usada diretamente para simular o comportamento de uma estrutura abstrata do tipo pilha. Para isso basta usar os métodos nativos append() e pop() para, respectivamente, empilhar e desempilhar elementos da pilha.
## Estudos preliminares

- Parêntese balanceados
- Símbolos balanceados

## O que você deve fazer

Você deve estender a funcionalidade da função bem_formada() para verificar se sequências formadas pelos seguintes pares de símbolos:

- (   )
- [ ]
- { }

Uma string desses símbolos é bem-formada se os símbolos são fechados na ordem inversa àquela em que foram abertos. Sua função deve ignorar caracteres diferentes de ‘ovo [ ] { }’ sem resultar em erro.

Por exemplo, as seguintes sequências são bem formadas:

- " ( { } )"
- " { } ( - ) [ { } (   ) ]"
- " (a + { b } )-{2 *[ 3+4 ]} "
- “{ ( { x } ) } [ y ]”

E as seguintes sequências não são bem formadas:

- “[”
- “( { ) }”
- “{ ( { } } )”
- “( ( ( . ) )”
- " ] "
- “{ ( { x } } [ y ] )”

Dessa vez, ao invés de utilizar a classe Pilha, use uma lista diretamente para se comportar como pilha na resolução desse exercício.

## Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

- Baixe o arquivo bem_formada.py.
- Carregue esse arquivo usando o Spyder ou Colab.
- Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
- Estude o enunciado e os exemplos fornecidos para entender como a função deve funcionar.
- Documente seu trabalho.
- Implemente e teste sua função.
- Caso você deseje testar sua função no próprio arquivo, não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
- Submeta apenas o arquivo bem_formada.py.

Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

- buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
- solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
- permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
- ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

## Arquivos requeridos
#### bem_formada.py

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

ABRE = '([{'
FECHA = ')]}'

def main():
    ''' função para teste da função bem_formada
    '''

    print("Vixe, ainda não fiz nenhum teste!")

# ---------------------------------------------------------

def bem_formada( seq ):
    ''' (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False
    '''
    print("Vixe, ainda não fiz a função bem_formada!")

# ---------------------------------------------------------

if __name__ == '__main__':
    main()
```