# Exercício Individual 03
**Entrega**: até 22:00 h de 25 de agosto.


# Classe Complexo

# Objetivos

O objetivo deste exercício é promover um primeiro contanto à pratica de programação conhecida como Orientação a Objetos. Para esse fim você implementará parte de uma classe para trabalhar com números complexos.

Os principais elementos presentes nesse exercício são:

- classes, objetos e referências (self)
- classes nativas versus classes definidas pelo usuário
- atributos de estado e métodos
- método especial utilizado pelo construtor: ***\_\_init__()***
- método especial utilizado por print: ***\_\_str__()***
- método especial utilizado pelo operador * (multiplicação): ***\_\_mul__()***
- método comum some: some()

# Estudo preliminar

Mesmas leituras da aula anterior:

    Introdução à Programação Orientada à Objetos
    Uma Classe Fraction

Estude a classe Fraction que você entregou como parte do EX02.

# O que você deve fazer

- faça o download do arquivo complexo.py
- escreva os métodos: ***\_\_init__()***, ***\_\_str__()***, some(), e ***\_\_mul__()*** como especificados no arquivo - complexo.py.
- teste a sua classe Complexo, da forma que desejar. Pode discutir esses testes com seus colegas no Discord.
- após testar, submeta apenas o arquivo complexo.py.

Os atributos e métodos da classe Complexo que você deve implementar nesse exercício estão ilustrados a seguir
```
   c  = Complexo(3.7, 2.5) 

            ATRIBUTOS
 inicio    +---------------------------------+           
   |       |   MÉTODOS:                      |           
   |       |   __init__()                    |           
   +------>|   __str__()                     |
           |                                 |
           |                                 |
           |   +-----------------------+     |           
           |   | ESTADO:               |     |           
   +------>|   |   real (float) -------------------> 3.7   
   |       |   |   imag (float) -------------------> 2.5   
 self      |   +-----------------------+     |           
           |                                 |           
           +---------------------------------+
```

# Arquivos requeridos
**complexo.py**

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
        print("Vixe! Ainda não fiz o método __init__()")
        
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
        return "Vixe! Ainda não fiz o método __str__()"    

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
        print( "Vixe! Ainda não fiz o método some" )

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
        print("Vixe! Ainda não fiz o método __mul__()")
```