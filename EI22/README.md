Objetivos

Neste exercício vamos continuar o tópico de ordenação de listas.

    Mas por que estudar ordenação se o Python já faz isso pra mim?

    O problema de ordenação é um muito rico em soluções diferentes, cada uma baseada em ideias distintas que vai nos ajudar a continuar a desenvolver o pensamento computacional. Vamos aproveitar também para treinar e aprofundar vários fundamentos de análise de algoritmos.

Sendo assim, para treinar esses fundamentos nesses e em futuros exercícios, utilize apenas comandos básicos do Python e, para continuar a desenvolver o pensamento, evite pensar no tipo list. Procure desenhar no papel sequências de números que devem ser ordenados, por exemplo, percorrendo as sequência e trocando os elementos de posição.
O que você deve fazer

Nesse exercício você deve implementar 2 funções:

    intercale_seqs(seq1, seq2)
    main(): que deve incluir 10 testes para sua função.

O comportamento de cada função está descrito no cabeçalho das funções no arquivo intercalacao.py.
Roteiro

    Baixe o arquivo intercalacao.py para uma pasta do seu computador.
    Carregue esse arquivo usando o Spyder ou Colab ou seu IDE Python predileto.
    Leia o cabeçalho do arquivo com atenção e edite o cabeçalho colocando seu nome e NUSP.
    Estude o conteúdo do arquivo, esse enunciado e os exemplos fornecidos para entender o que você deve implementar.
    Implemente, documente e teste seu trabalho.
    Submeta apenas o arquivo intercalacao.py.

Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

    buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
    solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
    permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
    ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

Arquivos requeridos
intercalacao.py

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
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    print("Testes do EI22 - ordenação por intercalação")

    # escreva seus testes

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2):
    ''' (list, list) -> list

    Recebe seq1 e seq2, duas listas tal que:

        - seq1 é crescente com n1 >= 0 elementos e
        - seq2 é crescente com n2 >= 0 elementos

    Retorna uma lista com n1+n2 elementos, contendo
    os elementos de seq1 e seq2 em ordem crescente.

    Exemplo para
        seq1 = [7, 11, 56] e
        seq2 = [-5, 7, 99, 104]

    a função deve retornar a lista:
        [-5, 7, 7, 11, 56, 99, 104]
    '''

    # escreva sua solução

#--------------------------------------------
if __name__ == '__main__':
    main()
```
