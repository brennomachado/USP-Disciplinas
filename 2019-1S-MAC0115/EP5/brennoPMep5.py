# -*- coding: utf-8 -*-
"""
DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
TODAS AS PARTES ORIGINAIS DESSE EP FORAM DESENVOLVIDAS E
IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES DESSE EP.
DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
SERÃO SEVERAMENTE PUNIDOS.
Nome do aluno: Brenno Pereira Machado
Número USP: 6434401
Curso: Licenciatura em Física
Disciplina: MAC0115 Introdução à Computação
Exercício-Programa EP5
"""

import math

def main():
    print("__________________________________________________________________________")
    print("ALGUMAS APROXIMACOES PARA O VALOR DE PI:\n(utilizamos math.pi que é 3.141592653589793)")

########## Método 1: Retângulos
    print("__________________________________________________________________________")
    print("Método 1 - Valor aproximado para PI utilizando o Método dos Retângulos")
    precisao = float(input("Digite um número (> 0 e < 1) para epsilon: "))

    pi1 = 0.0
    i = 1
    while math.pi - pi1 > precisao :    #como pi1 sempre < que math.pi o módulo da substração não é necessária.
        retangulos = 2**i
        pi1 = 4*areaMetodoRetangulos(0, 1, retangulos)
        i = i + 1

    print("Número de retângulos considerados para o cálculo da última área : ", retangulos)
    print("Valor aproximado para PI :%.15f" %(pi1))

########## Método 2: Trapézios
    print("__________________________________________________________________________")
    print("Método 2 - Valor aproximado para PI utilizando o Método dos Trapézios")
    precisao = float(input("Digite um número (> 0 e < 1) para epsilon:"))

    pi2 = 0.0
    i = 1
    while math.pi - pi2 > precisao :    #como pi2 sempre < que math.pi o módulo da substração não é necessária.
        trapezios = 2**i
        pi2 = 4*areaMetodoTrapezios(0, 1, trapezios)
        i = i + 1

    print("Número de trapézios considerados para o cálculo da última área: ", trapezios)
    print("Valor aproximado para PI : %.15f" %(pi2))

########## Método 3: Série de Wallis
    print("__________________________________________________________________________")
    print("Método 3 - Valor aproximado para PI utilizando a série de Wallis")
    precisao = float(input("Digite um número (> 0 e < 1) para epsilon:"))

    n_termos3, pi3 = piSerieWallis(precisao)
    print("Número de termos da série incluídos no cálculo : ", n_termos3)
    print("Valor aproximado para PI : %.14f" %(pi3))

########## Método 4: Série de Nilakantha
    print("__________________________________________________________________________")
    print("Método 4 - Valor aproximado para PI utilizando a série de Nilakantha")
    precisao = float(input("Digite um número (> 0 e < 1) para epsilon:"))

    n_termos4, pi4 = piSerieNilakantha(precisao)
    print("Número de termos da série incluídos no cálculo : ", n_termos4)
    print("Valor aproximado para PI : %.15f" %(pi4))

################# Função: Semi-circunferência de raio 1 ####################
def f(x):
    """ (float) -> float
    Recebe um número real x e se (1.0-x*x) for positivo, retorna a raiz quadrada de (1.0-x*x); em caso contrário, retorna 0.
    Obs.: para determinar a raiz quadrada é utilizada a função sqrt do módulo math.
    """
    fx = 1.0 - x*x
    if fx > 0:
        return math.sqrt(fx)
    else:
        return 0

################# Função: Método dos Retângulos ####################
def areaMetodoRetangulos(a, b, k):
    """ (float, float, int) -> float
    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x), no intervalo
    a, b], calculada pelo método dos retângulos, utilizando k retângulos.
    """
    i=1
    area = 0.0
    delta = (b - a)/k
    while i <= k:
        area = area + f(a + delta*i)*delta
        i = i + 1
    return area

################# Função: Método dos Trapézios ####################
def areaMetodoTrapezios(a, b, k):
    """ (float, float, int) -> float
    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x), no intervalo [a, b], calculada pelo método dos trapézios, utilizando k trapézios.
    """
    i = 1
    delta = (b - a)/k
    area = 0.0
    termo1 = f(a)
    while i < k :
        termo2 = f(a + i*delta)
        area = area + ((termo1 + termo2)*delta)/2
        termo1 = termo2
        i = i + 1
    return area

################# Função: Série de Wallis ####################
def piSerieWallis(eps):
    """ (float) -> int, float
    Recebe um número real eps, com 0 < eps < 1.
    Esta função calcula um valor aproximado para pi, piAproxWallis, através da série de Wallis, incluindo os primeiros termos até que o valor absoluto da diferença entre o valor calculado piAproxWallis e o valor da constante math.pi seja menor do que eps.
    A função retorna o número de termos considerados e o valor calculado piAproxWallis.
    Obs.: para determinar o valor absoluto é utilizada a função fabs do módulo math.
    """
    i=1
    pi=1.0
    while math.fabs(math.pi - pi*2) > eps :
        pi = pi*(4*(i*i))/((2*i)**2 - 1)     #série de wallis (2n/(2n-1))*(2n/(2n+1)) = pi/2
        i = i + 1
    return i, pi*2
    """Obs: Acredito que a contagem de termos do exemplo do Método 3 dado pelo PDF do Exercício 5 esteja equivocado com o número termos da série de Wallis. Aparentemente o exemplo conta os pares de fatores que se multiplicam  (2/1 * 2/3 ...etc) como sendo cada um 2 termos. Rigosamente pela série de Wallis cada par de fatores que aparece na série multiplicativa é apenas 1 termo.
    Não sei isso explica a precisão do exemplo estar errada, pois o exemplo pede para que epsilon tenha precisão de 1e-5, mas entrega um pi com diferença na quarta casa depois do zero em comparação a math.pi, ou seja, uma precisão de 1e-4"""

################# Função: Série de Nilakantha ####################
def piSerieNilakantha(eps):
    """ (float) -> int, float
    Recebe um número real eps, com 0 < eps < 1.
    Esta função calcula um valor aproximado para pi, piAproxNilakantha, através da série de Nilakantha, incluindo os primeiros termos até que o valor absoluto da diferen¸ca entre o valor calculado piAproxNilakantha e o valor da constante math.pi seja menor do que eps. A função retorna o número de termos considerados e o valor calculado piAproxNilakantha.
    Obs.: para determinar o valor absoluto é utilizada a função fabs do módulo math.
    """
    i=2
    cont=0
    pi=3.0
    sinal = 1
    while math.fabs(math.pi - pi) > eps :
        pi = pi + (sinal*4)/(i*(i + 1)*(i + 2))
        cont = cont + 1
        sinal = sinal*(-1)
        i = i + 2
    return cont, pi

main()
