# EI06
Data de entrega: quinta, 9 set 2021, 08:00

# Classe Horario
## Objetivos

O objetivo deste exercício é continuar a prática de programação conhecida como Orientação a Objetos para aplicar os conceitos cobertos até aqui.
Estudos preliminares

A partir dessa atividade vamos começar a trabalhar com listas. Para refrescar sua memória para essa e futuras atividades, sugerimos a leiatura das seguintes sessões sobre listas em Python.

- Valores em uma lista
- Comprimento de uma lista
- Acessando os elementos
- Pertinência em uma lista
- Concatenação e repetição
- Fatias de listas

## O que você deve fazer

Implemente a classe Horario.

Sua classe Horário deve possuir um atributo de nome dados. Esse atributo dados deve ser uma lista contendo três números inteiros maiores ou iguais zero.

Assim, um horário é representado na lista dados da seguinte forma:

- dados[0]: um número inteiro entre 0 e 59 que indica segundos
- dados[1]: um número inteiro entre 0 e 59 que indica minutos
- dados[2]: um número inteiro entre 0 e 23 que indica horas

## Comportamentos que você deve implementar

Os comportamentos correspondem aos métodos que a classe deve oferecer para que possamos manipular objetos do tipo Horario. Escolha nomes apropriados para cada comportamento e utilize os métodos especiais que desejar para implementar esses comportamentos.

- Ao ser chamada pela função print(), um objeto Horario com dados = [7,5,2] deve imprimir a string ‘02:05:07’ que e podemos ler como 2 horas, 5 minutos e 7 segundos.

- Para criar o horário ‘14:30:05’ devemos usar a chamada Horario(14,30,5). Observe que o atribtuto dados deve corresponder à lista [5,30,14].
    - Para criar o horário ‘11:45:00’ (onze e quarenta e cinco) devemos usar a chamada Horario(11,45).
    - Para criar o horário ‘12:00:00’ (doze horas) devemos usar a chamada Horario(12).

Para ilustrar os demais comportamentos desejados para objetos da classe Horario e ajudar você a testar sua classe, utilize a seguinte função main() que mostra os comportamentos e os resultados esperados.

```
def main():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')

## CASO VOCÊ UTILIZE ESSA FUNÇÃO MAIN 
## NAO SE ESQUEÇA DE TERMINAR O SEU ARQUIVO COM
## if __name__ == '__main__':
##     main()
```

Você pode estender esses comportamentos, desde que sejam consistentes e não alterem os resultados como ilustrados nos exemplos de testes da main().

## Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar.

    Baixe o arquivo horario.py.
    Carregue esse arquivo usando o Spyder ou Colab.
    Leia o cabeçalho do arquivo horario.py com atenção e edite o cabeçalho colocando seu nome e NUSP.
    Estude o enunciado e os exemplos fornecidos para identificar os métodos que você deseja (ou precisa).
    Documente seu trabalho descrevendo cada método.
    Implemente e teste cada método.
    Caso você deseje utilizar a função main(), não se esqueça de incluir o “if _ _ name _ _ …” no final do arquivo.
    Submeta apenas o arquivo horario.py.

## Honestidade acadêmica

Esse é um exercício individual, não em grupo. Isso não significa que você não pode receber ajuda de outras pessoas, inclusive de seus colegas. De uma forma geral, gostaríamos de incentivar as discussões de ideias, conceitos e alternativas de solução. Nossa maior recomendação é evitar olhar o código fonte de uma solução antes de escrever o seu programa. Em caso de dúvida, consulte a página Sobre colaboração em MAC0122

De forma sucinta, evite as seguintes ações que caracterizam desonestidade acadêmica na realização dos trabalhos individuais desse curso:

    buscar e obter uma solução (parcial ou completa, correta ou não) de exercício programa (EP) na internet ou qualquer outro meio físico ou virtual, durante o período de submissão do referido EP;
    solicitar ou obter uma cópia (parcial ou completa, correta ou não) da solução de um EP durante o seu período de submissão;
    permitir que um colega acesse uma cópia (parcial ou completa, correta ou não) do seu EP, durante o período de submissão;
    ainda mais grave é o plágio, que se configura pela utilização de qualquer material não visto em aula ou não descrito no enunciado, que não seja de sua autoria, em parte ou ao todo, e entregar, com ou sem edição, como se fosse seu trabalho, para ser avaliado.

## Arquivos requeridos
### horario.py