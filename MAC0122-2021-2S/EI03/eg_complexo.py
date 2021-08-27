#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    GRUPO: 6
      Brenno Pereira Machado
      Eduardo Gonçalves
      Vitor Huk Jun Chung

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim ou por meu time 
    cujos nomes estão relacionados abaixo e que, portanto, não 
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
    listadas abaixo, e incluo também os nomes de colegas
    do meu time caso essa tenha sido uma atividade em grupo.

    - LISTA de colegas do time 
        - não foi uma atividade em grupo (substitua essa linha caso tenha sido)

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - 

    - LISTA de outras pessoas que colaboraram na realização do trabalho e
        externas ao grupo.
        - 
'''

# ===================================================================

def main():
    '''  Função principal do programa que calcula soma e multiplicação de dois numeros complexos
    '''

    print()
    print("###############################################################")
    print("###               TESTES DA CLASSE COMPLEXOS                ###")
    print("###############################################################\n")


    print("## TESTES DO ENUNCIADO do EG-3 ##\n")
    cabecalho = '''Testes da classe Complexo
    
        Cada teste ou grupo de testes deve imprimir uma mensagem
        adequada para entender seu propósito, descrevendo a chamada 
        e a saída esperada.

        Exemplo: 
        Teste da criação usando valores default:
        c0 = Complexo( )
        print(f'Complexo( ) deve imprimir 0.0+j0.0. Resposta = {c0}')
        c1 = Complexo(2)
        print(f'Complexo(2) deve imprimir 2.0+j0.0. Resposta = {c0}')
    '''
    print(cabecalho)
    c0 = Complexo( )
    print(f'Complexo( ) deve imprimir 0.0 -- Resposta = {c0}')
    c1 = Complexo(2)
    print(f'Complexo(2) deve imprimir 2.0 -- Resposta = {c1}')
    # coloque a seguir os demais testes do seu grupo


    print("\n\n## TESTES DO GRUPO PARA O EG-3 ##\n")

    c0 = Complexo() # construtor chama _init_()
    print("\nc0 ")
    print(c0.real, c0.imag)
    print(c0)

    c1 = Complexo(9)
    # print(c1.real, c1.imag)
    print("\nc1 ")
    print(c1.real, c1.imag)
    print(c1)

    c2 = Complexo(4,4)
    # print(c2.real, c2.imag)
    print("\nc2 ")
    print(c2.real, c2.imag)
    print(c2)

    c3 = Complexo(1,-24)
    print("\nc3 ")
    print(c3.real, c3.imag)
    print(c3)

    c00 = c0 * c0
    c11 = c1 * c1
    c22 = c2 * c2
    c33 = c3 * c3


    m11 = c1 + c1
    m22 = c2 + c2
    m13 = c1 + c3
    m23 = c2 + c3
    c23 = c2 * c3
    
    c33 = c3.some(c3)

    print("c00 = ",c00)
    print("c11 = ",c11)
    print("c22 = ",c22)
    print("c33 = ",c33)
    print("m11 = ",m11)
    print("m22 = ",m22)
    print("m13 = ",m13)
    print("m23 = ",m23)
    print("c23 = ",c23)
    print("c33 = ",c33)
    
    
    
# ===================================================================
class Complexo:
    '''Classe utilizada para representar um número Complexo.

    Um complexo é representado por dois números reais. 
    Assim, cada objeto dessa classe terá dois atributos de estado:
 
       * `real`: um número real que corresponde à parte real
       * `imag`: um número real que corresponde à parte imaginária
 
    Você deverá escrever os métodos a seguir.
    '''

    #------------------------------------------------------------------------------
    def __init__(self, r = 0.0, i = 0.0):
        '''(Complexo, float, float) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os reais `r` e `i` que 
        representam o número complexo.

        Exemplos:

        >>> c0 = Complexo() # construtor chama __init__()
        >>> c0.real
        0.0
        >>> c0.imag
        0.0
        >>> c1 = Complexo(9)
        >>> print(c1.real, c1.imag)
        9.0 0.0
        >>> c2 = Complexo(9,4)
        >>> print(c2.real, c2.imag)
        9.0 4.0
        >>> 
        '''
        self.real = float(r)
        self.imag = float(i)

    #------------------------------------------------------------------------------        
    def __str__(self):
        '''(Complexo) -> str

        Recebe uma referencia `self` a um objeto da classe Complexo e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplos:

        >>> ini = Complexo(8)
        >>> fim = Complexo(9,4)
        >>> fim.__str__()
        '9.0+j4.0'
        >>> ini.__str__() # chamada do método __str__()
        '8.0'
        >>> str(ini) # função str() exibe a string criada por __str__()
        '8.0'
        >>> str(fim) 
        '9.0+j4.0'
        >>> print(fim) # exibe o string criado por __str__()
        9.0+j4.0
        >>> print(ini)
        8.0
        >>>         
        '''

        ## Faz a impressão do número complexo do jeito que está no enunciado e docstring do EI03
        imaginario = self.imag
        if self.imag < 0 :
                imaginario *= (-1)
                sinal = "-"
        else :
            sinal = "+"
        if self.imag == 0 :
            return f"{self.real}"
        elif self.real == 0 :
            return f"j{self.imag}"
        elif (self.real == 0 and self.imag == 0):
            return f"0.0"
        return f"{self.real}{sinal}j{imaginario}"   
        

    #------------------------------------------------------------------------------        
    def some(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado da soma self + other
        
        Exemplos:

        >>> c0 = Complexo(8)
        >>> c1 = Complexo(9,4)
        >>> c2 = c0.some(c1)
        >>> print(c2)
        17.0+j4.0
        >>>         
        '''

        return Complexo(self.real + other.real, self.imag + other.imag)

    #------------------------------------------------------------------------------  

    def __add__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado da soma self + other
        '''

        return Complexo(self.real + other.real, self.imag + other.imag)

#------------------------------------------------------------------------------  


    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referência `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado do produto self * other
        
        Exemplos:

        >>> comp0 = Complexo(1, 2)
        >>> comp1 = Complexo(3, 4)
        >>> comp2 = comp0 * comp1
        >>> print(c2)
        -5.0+j10.0
        >>>         
        '''
        
        return Complexo(self.real*other.real + (self.imag*other.imag)*(-1) , self.real*other.imag + self.imag*other.real)

#   O teste if __name__ é SEMPRE a última coisa a fazer
if __name__ == '__main__':
    main()

