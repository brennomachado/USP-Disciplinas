# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: -

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
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' (string) -> bool

    Verifica se a string recebida é um palíndromo,
    retorna True caso sim e False caso não.

    **IMPORTANTE** essa função diferencia caracteres acentuados e maiúsculos
    '''

    s_invertido = Pilha()

    for i in s:
        s_invertido.empilhe(i)
    
    for i in s:
        if i != s_invertido.desempilhe():
            return False
    
    return True


## ==================================================================
##
class Pilha:
    ''' Classe utilizada para montar pilha do tipo LIFO (Last In, First Out)
    '''

    def __init__(self):
        ''' (Pilha) -> None
        Chamado pelo construtor da classe

        Recebe uma referência 'self' do objeto que tá sendo montado, 
        o qual será uma pilha vazia.
        '''

        self.dados = []

    def vazia(self):
        ''' (Pilha) -> bool

        Recebe uma referência 'self' da classe Pilha e retorna
        'True' se a pilha é vazia e 'False' se a pilha tem ao menos 1 elemento.
        '''

        return self.dados == []
    
    def empilhe(self, a):
        ''' (Pilha, type(a)) -> None

        Recebe uma referência 'self' da classe Pilha e um objeto do tipo 'type(a)'
        e adiciona 'a' na lista 'self.dados'.
        '''

        self.dados.append(a)
    
    def desempilhe(self):
        '''(Pilha) -> type(self.dados.pop())

        Recebe uma referência 'self' da classe Pilha e 
        remove-o da pilha e retorna esse item removido.
        '''

        return self.dados.pop()

    def topo(self):
        ''' (Pilha) -> type(self.dados.pop())

        Recebe uma referência 'self' da classe Pilha e 
        retorna o último item da pilha.
        '''

        return self.dados[-1]

    def __len__(self):
        ''' (Pilha) -> int

        Recebe uma referência 'self' da classe Pilha e 
        retorna o número de elementos da pilha.
        '''

        return len(self.dados)
    

## ==================================================================
## Escreva outras funções e classes caso desejar


## ==================================================================

def testes(): #função dada no enunciado do exercício

    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")

def main():
    '''  Função principal que testa a classe Pilha com alguns palíndromos
    '''

    print()
    print("###############################################################")
    print("###           CLASSE PILHA E TESTES DE PALINDROMOS          ###")
    print("###   Esse programa testa a classe pilha fazendo checagem   ###")
    print("###   de palíndromos                                        ###")
    print("###############################################################\n")

    palindromos = ["hanah", "coelho", "Hitoshi", "metem", "mirim", "omissíssimo", "osso", "Ovo", "ovo"]

    for palavra in palindromos:
        if palindromo(palavra):
            resultado = 'É'
        else:
            resultado = 'NÃO É'

        print(f"   {palavra:20} {resultado:8} um palíndromo")

    print("\n\n##### Testes feitos com a função testes() do enunciado do EI07 #####\n")
    testes()
    print()

if __name__ == '__main__':
    palindromo( '' )
    main()
