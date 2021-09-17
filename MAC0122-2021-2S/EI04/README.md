# Exercício Individual 04
**Entrega**: até 22:00 h de 30 de agosto.

# Complementos da classe Fraction
# Objetivos

O objetivo deste exercício é continuar a prática de programação conhecida como Orientação a Objetos. Vamos estender a classe Fraction para fortalecer nossa compreensão sobre o uso de métodos especiais, dessa vez misturando frações com objetos do tipo int.

A classe Fraction usada nesse exercício é baseada na classe de mesmo nome da seção 1.13.1 Uma Classe Fraction do livro Resolução de Problemas com Algoritmos e Estruturas de Dados usando Python.
Estudo preliminar

- [Mais sobre a implementação de operadores usando métodos especiais](https://edisciplinas.usp.br/mod/page/view.php?id=3846189&forceview=1)

# O que você deve fazer

Complete a classe Fraction com os métodos:

    __add__() e __radd__();
    __truediv__() e __rtruediv__(); e
    __eq__() e __req__().

Teste cada método antes de enviar sua solução. Lembre-se de testar com inteiros além de frações, segundo o cabeçalho de cada método.
Roteiro

Leia o(s) texto(s) sugeridos na seção Estudo premilinar:

- faça o download do arquivo fraction.py.
- carregue esse arquivo usando o Spyder ou Colab
- Leia o cabeçalho do arquivo fraction.py com atenção.
- Edite o cabeçalho colocando seu nome e NUSP.
- execute o arquivo no Spyder ou no Colab. Observe que ele possui apenas algumas sugestões de teste. Você é responsável para criar outros testes, mais abrangentes, como temos feito nas discussões em grupo.
- Escreva os métodos __add__() e __radd__() e teste-os. Em caso de dúvidas, consulte novamente os exemplos - do texto “Mais sobre a implementação de operadores usando métodos especiais”.
- Escreva os métodos __truediv__() e __rtruediv__() e teste-os.
- Escreva os métodos __eq__() e __req__() e teste-os.
- após testar, e testar de novo, submeta apenas o arquivo fraction.py.


# Arquivos requeridos

# Fraction.py

```
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome:
    NUSP:

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
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

# ===================================================================

def main():
    '''
        Programa main usado para teste da classe Fraction.
    '''

    # Criação de objetos do tipo Fraction 
    f12 = Fraction(1,2)
    f34 = Fraction(3,4)

    # soma 2 fracoes
    soma = f12 + f34
    print(f"{f12} + {f34}      = {soma}")
    print(f"Resultado esperado = 5/4 ")

    # soma fracao com inteiro
    soma = f12 + 2
    print(f"{f12} + 2         = {soma}")
    print(f"Resultado esperado = 5/2 ")

    # soma inteiro com fracao
    soma = 2 + f34
    print(f"  2 + {f34}      = {soma}")
    print(f"Resultado esperado = 11/4 ")

    # ===================================================================
    # Escreva outros testes


# ===================================================================
#
#   No futuro substituiremos a definição da classe por um import. 
#
# ===================================================================

class Fraction:
    '''
        Essa classe Fraction foi adaptada da seção 1.13.1 Uma Classe Fraction
        do capítulo 1 do livro Resolução de Problemas com Algoritmos e 
        Estruturas de Dados usando Python disponível no endereço
        https://panda.ime.usp.br/panda/static/pythonds_pt/index.html. 

        A classe Fraction representa uma fração. 
        Uma fração é constituída por um numerador e um denominador, 
        ambos inteiros, como por exemplo 2/5 (dois quintos), 
        onde 2 é o numerador e 5 o denominador.
    '''

    def __init__(self, cima, baixo):
        '''(Fraction, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros cima e baixo que representam
        a fração.

        Exemplos:

        >>> frac = Fraction(2,5) # construtor chama __init__()
        >>> frac.num
        2
        >>> frac.den
        5
        '''
        self.num = cima
        self.den = baixo

    def __str__(self):
        '''(Fraction) -> str

        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:

        >>> frac = Fraction(2,5)
        >>> print(frac)
        2/5
        '''
        return f"{self.num}/{self.den}"

    #------------------------------------
    def __add__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a soma da Fraction `self` e da Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction + Fraction ou
                                            Fraction + int
        """
        print("vixe! ainda preciso escrever o método __add__!")

    #------------------------------------
    def __radd__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a soma da Fraction `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fraction
        """
        print("vixe! ainda preciso escrever o método __radd__!")

    #-------------------------------------
    def __truediv__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a divisão da Fraction `self` pela Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction / Fraction ou
                                            Fraction / int
        """
        print("vixe! ainda preciso escrever o método __truediv__!")

    #-------------------------------------
    def __rtruediv__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a divisão do int `other` pela Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        print("vixe! ainda preciso escrever o método __rtruediv__!")


    #-------------------------------------
    def __eq__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        print("vixe! ainda preciso escrever o método __eq__!")

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        print("vixe! ainda preciso escrever o método __req__!")

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()

```