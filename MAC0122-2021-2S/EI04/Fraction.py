#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: 6434401

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
    print()
    print("###############################################################")
    print("###                TESTES DA CLASSE FRACTION                ###")
    print("###############################################################\n")

    ## Testes propostos pelo enunciado
    print("## TESTES DO ENUNCIADO do EI-4 ##\n")

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

    ## Outros testes
    print("\n\n## MEUS TESTES ##\n")

    print("   # Testes para SOMA")
    fracao1 = Fraction()
    fracao2 = 0
    print(f"      {fracao1}  + {fracao2}    = {fracao1 + fracao2}  ==> Esperado = 0/1")
    fracao1 = Fraction()
    fracao2 = 1
    print(f"      {fracao1}  + {fracao2}    = {fracao1 + fracao2}  ==> Esperado = 1/1")
    fracao1 = Fraction(3,2)
    fracao2 = 0
    print(f"      {fracao1}  + {fracao2}    = {fracao1 + fracao2}  ==> Esperado = 3/2")
    fracao1 = 0
    fracao2 = Fraction(3,2)
    print(f"      {fracao1}    + {fracao2}  = {fracao1 + fracao2}  ==> Esperado = 3/2")
    fracao1 = Fraction(3,2)
    fracao2 = 3
    print(f"      {fracao1}  + {fracao2}    = {fracao1 + fracao2}  ==> Esperado = 9/2")
    fracao1 = 3
    fracao2 = Fraction(3,2)
    print(f"      {fracao1}    + {fracao2}  = {fracao1 + fracao2}  ==> Esperado = 9/2")
    fracao1 = Fraction(48,12)
    fracao2 = Fraction(3,2)
    print(f"      {fracao1}  + {fracao2}  = {fracao1 + fracao2} ==> Esperado = 11/2")
    fracao1 = Fraction(3,2)
    fracao2 = Fraction(48,12)
    print(f"      {fracao1}  + {fracao2}  = {fracao1 + fracao2} ==> Esperado = 11/2")
    fracao1 = Fraction(33,9)
    fracao2 = 7
    print(f"      {fracao1} + {fracao2}    = {fracao1 + fracao2} ==> Esperado = 32/3")
    fracao1 = 7
    fracao2 = Fraction(33,9)
    print(f"      {fracao1}    + {fracao2} = {fracao1 + fracao2} ==> Esperado = 32/3")
    
    #=============================================================================
    print("\n   # Testes para DIVISÃO")
    fracao1 = Fraction(0)
    fracao2 = 1
    print(f"      {fracao1}  ÷ {fracao2}    = {fracao1 / fracao2}   ==> Esperado = 0/1")
    fracao1 = 0
    fracao2 = Fraction(1)
    print(f"      {fracao1}    ÷ {fracao2}  = {fracao1 / fracao2}   ==> Esperado = 0/1")
    fracao1 = Fraction(11,3)
    fracao2 = 1
    print(f"      {fracao1} ÷ {fracao2}    = {fracao1 / fracao2}  ==> Esperado = 11/3")
    fracao1 = 1
    fracao2 = Fraction(11,3)
    print(f"      {fracao1}    ÷ {fracao2} = {fracao1 / fracao2}  ==> Esperado = 3/11")
    fracao1 = Fraction(33,3)
    fracao2 = 1
    print(f"      {fracao1} ÷ {fracao2}    = {fracao1 / fracao2}  ==> Esperado = 11/1")
    fracao1 = 1
    fracao2 = Fraction(33,3)
    print(f"      {fracao1}    ÷ {fracao2} = {fracao1 / fracao2}  ==> Esperado = 1/11")
    fracao1 = Fraction(16,4)
    fracao2 = Fraction(8,7)
    print(f"      {fracao1}  ÷ {fracao2}  = {fracao1 / fracao2}   ==> Esperado = 7/2")
    fracao1 = Fraction(8,7)
    fracao2 = Fraction(16,4)
    print(f"      {fracao1}  ÷ {fracao2}  = {fracao1 / fracao2}   ==> Esperado = 2/7")
    fracao1 = Fraction(4,2)
    fracao2 = Fraction(10,4)
    print(f"      {fracao1}  ÷ {fracao2}  = {fracao1 / fracao2}   ==> Esperado = 4/5")
    fracao1 = Fraction(10,4)
    fracao2 = Fraction(4,2)
    print(f"      {fracao1}  ÷ {fracao2}  = {fracao1 / fracao2}   ==> Esperado = 5/4")
    fracao1 = Fraction(0)
    fracao2 = Fraction(17,5)
    print(f"      {fracao1}  ÷ {fracao2} = {fracao1 / fracao2}   ==> Esperado = 0/1")
    fracao1 = Fraction(17,5)
    fracao2 = 3
    print(f"      {fracao1} ÷ {fracao2}    = {fracao1 / fracao2} ==> Esperado = 17/15")
    fracao1 = 3
    fracao2 = Fraction(17,5)
    print(f"      {fracao1}    ÷ {fracao2} = {fracao1 / fracao2} ==> Esperado = 15/17")
    fracao1 = Fraction(4,16)
    fracao2 = 8
    print(f"      {fracao1}  ÷ {fracao2}    = {fracao1 / fracao2}  ==> Esperado = 1/32")
    fracao1 = 8
    fracao2 = Fraction(4,16)
    print(f"      {fracao1}    ÷ {fracao2}  = {fracao1 / fracao2}  ==> Esperado = 32/1")
    fracao1 = Fraction(3,2)
    fracao2 = 3
    print(f"      {fracao1}  ÷ {fracao2}    = {fracao1 / fracao2}   ==> Esperado = 1/2")
    fracao1 = 3
    fracao2 = Fraction(3,2)
    print(f"      {fracao1}    ÷ {fracao2}  = {fracao1 / fracao2}   ==> Esperado = 2/1")

    #=============================================================================
    print("\n   # Testes para EQUIDADE")
    fracao1 = Fraction(0)
    fracao2 = 0
    print(f"      {fracao1}  == {fracao2}    => {fracao1 == fracao2}  ==> Esperado = True")
    fracao1 = 0
    fracao2 = Fraction(0)
    print(f"      {fracao1}    == {fracao2}  => {fracao1 == fracao2}  ==> Esperado = True")
    fracao1 = Fraction(1,1)
    fracao2 = 1
    print(f"      {fracao1}  == {fracao2}    => {fracao1 == fracao2}  ==> Esperado = True")
    fracao1 = Fraction(4,2)
    fracao2 = 2
    print(f"      {fracao1}  == {fracao2}    => {fracao1 == fracao2}  ==> Esperado = True")
    fracao1 = Fraction(11,3)
    fracao2 = Fraction(11,3)
    print(f"      {fracao1} == {fracao2} => {fracao1 == fracao2}  ==> Esperado = True")
    fracao1 = 22
    fracao2 = Fraction(66,3)
    print(f"      {fracao1}   == {fracao2} => {fracao1 == fracao2}  ==> Esperado = True")
    fracao1 = Fraction(7,5)
    fracao2 = Fraction(5,7)
    print(f"      {fracao1}  == {fracao2}  => {fracao1 == fracao2} ==> Esperado = False")
    fracao1 = Fraction(4,1)
    fracao2 = 2
    print(f"      {fracao1}  == {fracao2}    => {fracao1 == fracao2} ==> Esperado = False")
    fracao1 = Fraction(3,5)
    fracao2 = 5
    print(f"      {fracao1}  == {fracao2}    => {fracao1 == fracao2} ==> Esperado = False")
    fracao1 = 5
    fracao2 = Fraction(3,5)
    print(f"      {fracao1}    == {fracao2}  => {fracao1 == fracao2} ==> Esperado = False")
    fracao1 = Fraction(3,2)
    fracao2 = 3
    print(f"      {fracao1}  == {fracao2}    => {fracao1 == fracao2} ==> Esperado = False")
    fracao1 = 3
    fracao2 = Fraction(3,2)
    print(f"      {fracao1}    == {fracao2}  => {fracao1 == fracao2} ==> Esperado = False")

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

    def __init__(self, cima=0, baixo=1):
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

        # Redução da fração cima/baixo pelo mdc n
        m = cima
        n = baixo
        while m%n != 0:
            mvelho = m
            nvelho = n
            m = nvelho
            n = mvelho%nvelho

        self.num = cima // n
        self.den = baixo // n
        
    #------------------------------------
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

        if type(other) is int:
            novo_numerador = self.num + other*self.den
            novo_denominador = self.den
        else :
            novo_numerador = self.num*other.den + self.den*other.num # self.num*other.den + self.den*other.num
            novo_denominador = self.den*other.den
        
        return Fraction(novo_numerador, novo_denominador)

    #------------------------------------
    def __radd__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a soma da Fraction `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fraction
        """
        return self + other

    #-------------------------------------
    def __truediv__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a divisão da Fraction `self` pela Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction / Fraction ou
                                            Fraction / int
        """

        if type(other) is int: 
            novo_numerador = self.num
            novo_denominador = self.den*other
        else :
            novo_numerador = self.num*other.den
            novo_denominador = self.den*other.num
        
        return Fraction(novo_numerador, novo_denominador)

    #-------------------------------------
    def __rtruediv__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a divisão do int `other` pela Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """

        novo_numerador = other*self.den
        novo_denominador = self.num
        return Fraction(novo_numerador,novo_denominador)

    #-------------------------------------
    def __eq__(self, other):
        """ (Fraction, Fraction ou int) -> True ou False

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        
        if type(other) is int:
            return (self.num/self.den) == other
        else :
            return self.num == other.num and self.den == other.den

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> True ou False

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int == Fraction
        """
        return self == other

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()