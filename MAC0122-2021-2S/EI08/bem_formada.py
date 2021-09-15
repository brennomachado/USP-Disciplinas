# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Brenno Pereira Machado
    NUSP: 6434401

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

    print("\n###############################################################")
    print("###              LISTA E SEQUÊNCIAS BEM FORMADAS            ###")
    print("###   Esse programa usa uma lista como pilha para testar se ###")
    print("###   uma expressão tem () [] { } de forma balanceada       ###")
    print("###############################################################\n")

    sequencias = ["", " ( { } )", " { } ( - ) [ { } ( ) ]", "(a + { b } )-{2 *[ 3+4 ]}", "{ ( { x } ) } [ y ]",
         "[", "( { ) }", "{ ( { } } )", "( ( ( . ) )", " ] ", "{ ( { x } } [ y ] )"]

    for expressao in sequencias:
        if bem_formada(expressao):
            resultado = 'É'
        else:
            resultado = 'NÃO É'

        expressao+="'"
        print(f"'{expressao:30} {resultado:8} bem formada")

    
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
    >>> bem_formada( "    { ( { x }  } [ y ] )" )
    False
    '''

    pilha = []
    balanceada = True
    i = 0
    tam = len(seq)

    while i < tam and balanceada:
        caracter = seq[i]
        if caracter in ABRE:
            pilha.append(caracter)
        elif caracter in FECHA and pilha == []:
            balanceada = False
        elif caracter in FECHA :
            topo = pilha.pop()
            if not (caracter == ")" and topo == "("  or
                caracter == "]" and topo == "["  or
                caracter == "}" and topo == "{") :
                # Se uma das três operações "AND" for verdadeira.
                #   OBS.: Substitui a função matches() da literatura dada
                
                balanceada = False
        i = i+1

    if balanceada and pilha == []:
      return True
    else:
      return False

# ---------------------------------------------------------

if __name__ == '__main__':
    main()