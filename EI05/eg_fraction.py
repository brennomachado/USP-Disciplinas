# -*- coding: utf-8 -*-
"""eg_fraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zM7CjygjztGhAne_Klxu1wKZOehbC8BO
"""

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    GRUPO:  9 
    Nomes:  Brenno Pereira Machado
            Bianca Sanches Portella
            Felipe Francolin Janowitzer
            Lucas Antonio de Sousa Ribeiro

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

from timeit import default_timer as timer
from math import gcd
USE_GCD = True

def HF( n ):
    ''' (int) -> Fraction 
    Calcula o valor harmônico de n
    '''
    soma = Fraction(0,1)
    for i in range(1, n+1):
        soma = soma + Fraction(1,i)
    return soma

def main( ):
    ''' 
    Mede o tempo da função HF() para n crescendo de forma exponencial.
    Os tempos são dados em segundos.
    '''

    for n in range( 10, 20 ):
        inicio = timer()
        hfn = HF( n )
        fim    = timer()
        print(f"H( {n} ) = {hfn} : {fim - inicio} s")



def main_velha():
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


    #=============================================================================
    print("\n   # Testes para MENOR ou IGUAL")
    fracao1 = Fraction(0)
    fracao2 = 0
    print(f"      {fracao1}  <= {fracao2}    : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = Fraction(0)
    fracao2 = 1
    print(f"      {fracao1}  <= {fracao2}    : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = 0
    fracao2 = Fraction(0)
    print(f"      {fracao1}    <= {fracao2}  : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = 0
    fracao2 = Fraction(1,1)
    print(f"      {fracao1}    <= {fracao2}  : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = Fraction(2,3)
    fracao2 = Fraction(5,3)
    print(f"      {fracao1}  <= {fracao2}  : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = Fraction(3,3)
    fracao2 = Fraction(6,6)
    print(f"      {fracao1}  <= {fracao2}  : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = Fraction(5,1)
    fracao2 = 5
    print(f"      {fracao1}  <= {fracao2}    : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = Fraction(7,5)
    fracao2 = Fraction(23,3)
    print(f"      {fracao1}  <= {fracao2} : {fracao1 <= fracao2}  ==> Esperado: True")
    fracao1 = Fraction(23,3)
    fracao2 = Fraction(7,5)
    print(f"      {fracao1} <= {fracao2}  : {fracao1 <= fracao2} ==> Esperado: False")
    fracao1 = 28
    fracao2 = Fraction(9,2)
    print(f"      {fracao1}   <= {fracao2}  : {fracao1 <= fracao2} ==> Esperado: False")
    
    #=============================================================================
    print("\n   # Testes para ESTRITAMENTE MAIOR")
    fracao1 = Fraction(0,1)
    fracao2 = 0
    print(f"      {fracao1} > {fracao2}   : {fracao1 > fracao2} ==> Esperado: False")
    fracao1 = Fraction(1,1)
    fracao2 = 0
    print(f"      {fracao1} > {fracao2}   : {fracao1 > fracao2}  ==> Esperado: True")
    fracao1 = 0
    fracao2 = Fraction(0)
    print(f"      {fracao1}   > {fracao2} : {fracao1 > fracao2} ==> Esperado: False")
    fracao1 = 0
    fracao2 = Fraction(1,1)
    print(f"      {fracao1}   > {fracao2} : {fracao1 > fracao2} ==> Esperado: False")
    fracao1 = Fraction(5,3)
    fracao2 = Fraction(2,3)
    print(f"      {fracao1} > {fracao2} : {fracao1 > fracao2}  ==> Esperado: True")
    fracao1 = Fraction(9,3)
    fracao2 = Fraction(3,3)
    print(f"      {fracao1} > {fracao2} : {fracao1 > fracao2}  ==> Esperado: True")
    fracao1 = Fraction(5,1)
    fracao2 = 5
    print(f"      {fracao1} > {fracao2}   : {fracao1 > fracao2} ==> Esperado: False")
    fracao1 = 5
    fracao2 = Fraction(5,1)
    print(f"      {fracao1}   > {fracao2} : {fracao1 > fracao2} ==> Esperado: False")
    fracao1 = 6
    fracao2 = Fraction(5,1)
    print(f"      {fracao1}   > {fracao2:} : {fracao1 > fracao2}  ==> Esperado: True")
    

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
        n = self.meu_mdc(cima,baixo)

        self.num = cima // n
        self.den = baixo // n
        
    #------------------------------------
    def meu_mdc( self, a, b ):
      ''' (Fraction, int, int) -> int 
      recebe dois inteiros a e b, e 
      retorna o mdc entre a e b.
      '''
      if USE_GCD:
          return gcd(a, b)

      aa = abs(a)
      ab = abs(b)
      mdc = min(aa, ab)
      if mdc == 0: return max(aa, ab)
      while (aa % mdc != 0) or (ab % mdc != 0): 
          mdc -= 1
      return mdc

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
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        
        if type(other) is int:
            return (self.num == self.den*other)
        else :
            return self.num == other.num and self.den == other.den

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> bool

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int == Fraction
        """
        return self == other

    #-------------------------------------
    def __gt__(self, other):
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação de > da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction > Fraction ou
                                            Fraction > int
        """

        if type(other) is int:
            return self.num > self.den*other
        else :
            return self.num*other.den > self.den*other.num

    def __lt__(self, other): # Funcionaria como o __rgt__ especificado no enunciado
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação de < da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction < Fraction ou
                                            Fraction < int
        """

        if type(other) is int:
            return self.num < self.den*other
        else :
            return self.num*other.den < self.den*other.num

    #-------------------------------------
    def __le__(self, other):
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação de <= da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction <= Fraction ou
                                            Fraction <= int
        """

        if type(other) is int:
            return self.num < self.den*other or self.num == self.den*other
        else :
            return self.num*other.den < self.den*other.num or self.num == self.den*other.num

    #-------------------------------------
    def __ge__(self, other): # Funcionaria como o __rle__ especificado no enunciado
        """ (Fraction, Fraction ou int) -> bool

        Retorna a comparação de >= da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction >= Fraction ou
                                            Fraction >= int
        """

        if type(other) is int:
            return self.num > self.den*other or self.num == self.den*other
        else :
            return self.num*other.den > self.den*other.num or self.num == self.den*other.num

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()