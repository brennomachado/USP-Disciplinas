# ===============================================================
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
# ===============================================================

def main():
    '''  Função principal do programa que calcula o número harmônico
    '''
 
    print()
    print("###############################################################")
    print("###                    HARMÔNICO SIMPLES                    ###")
    print("###   Esse programa calcula o número harmônico de ordem N   ###")
    print("###   através de duas formas distintas                      ###")
    print("###############################################################\n")

    n = int(input("\nDigite o número inteiro N para o cálculo do Harmônico de ordem N:"))

    valorHMaior = Hmaior(n)
    valorHmenor = Hmenor(n)

    print("\nValor para Harmônico de ordem", n, "calculado com a função Hmaior() é", valorHMaior)
    print("Valor para Harmônico de ordem", n, "calculado com a função Hmenor() é", valorHmenor)
    
    print("\nA diferença entre os dois cálculos é de %.17f" % (abs(valorHmenor - valorHMaior)))


def Hmaior(n):
    ''' (int) -> float
    Recebe um número inteiro "n" e retorna o harmonico simpĺes para "n" calculado a partir do maior termo.
    '''

    harmonico = 0.0
    for i in range(1, n+1, 1):
        harmonico += 1.0/i

    return harmonico


def Hmenor(n):
    ''' escreva uma documentação para essa função
    '''

    harmonico = 0.0
    for i in range(n, 0, -1):
        harmonico += 1.0/i

    return harmonico

if __name__ == '__main__':
    main()

