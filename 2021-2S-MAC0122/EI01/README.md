Exercício individual

    Entrega: até 22:00 h de 18 de agosto.

Seja Hn o número harmônico de ordem n que pode ser calculado por ao menos duas formas:

Hmaior:   1 +    1/2     +   1/3     + 1/4 + ... + 1/n
Hmenor:   1/n +  1/(n-1) +   1/(n-2) + ... + 1/2 + 1

Onde Hmaior calcula Hn a partir do maior termo (1) até o menor termo (1/n) e Hmenor calcula Hn a partir do menor termo (1/n) até o maior termo (1).
Para pensar e discutir depois

Será que a ordem dessas somas altera o resultado, ou seja, o resultado de Hmaior() pode ser diferente de Hmenor()?
O que você deve fazer

Escreva uma função em Python de nome Hmaior() que recebe um inteiro positivo n e retorna o valor de Hmaiorn = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.

Escreva também a função Hmenor() recebe um inteiro positivo n e retorna o valor de Hmenorn = 1/n + 1/(n − 1) + 1/(n − 2) + ... + 1.

Cada função deve calcular as sequências na ordem definida nesse enunciado.
O que você deve entregar

Um arquivo Python (com extensão .py) contendo as duas funções: Hmaior() e Hmenor() e o seguinte esqueleto:
---
"""
Ao incluir esse cabeçalho declaro que todas as partes originais
desse exercício individual foram desenvolvidas e implementadas por
mim e que portanto não constituem desonestidade acadêmica ou plágio.
Declaro também que sou responsável por todas as cópias desse
programa e que não distribui ou facilitei a sua distribuição.
Estou ciente que os casos de plágio e desonestidade acadêmica
serão tratados segundo os critérios divulgados na página da 
disciplina.

Entendo que exercícios sem esse cabeçalho devem receber nota zero
e, ainda assim, poderão ser punidos por desonestidade acadêmica.    
"""
---

def main():
    ''' 
    a função main é opcional. 
    Caso desejar, inclua e deixe aqui os testes que você fez 
    com as funções Hmaior e Hmenor.
    '''
    print("testes das funções")


def Hmaior(n):
    ''' escreva uma documentação para essa função
    '''


def Hmenor(n):
    ''' escreva uma documentação para essa função
    '''

if __name__ == '__main__':
    main()    
    

Não deixe de documentar e testar as suas funções. Use EI01 como título ao enviar o arquivo .py com a sua solução.
Caso você deseje rever conceitos de Python para resolver esse exercício

    Variáveis, tipos e funções de entrada e saída
    Comando de repetição while
    Funções

Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

    buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
    solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
    permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
    ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.
