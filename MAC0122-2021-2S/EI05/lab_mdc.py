#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:37:09 2021

@author: fradim
"""
# para timer()
from timeit import default_timer as timer

# para math.gcd(
import math

CABECALHO = " "*7 + "a" + " "*10 + "b    math.gcd()    meu_mdc()"

#-------------------------------------------              
def main():
    a, b = 46368, 75025
    print(CABECALHO) 
    for i in range(20):
        # cronometre math.gcd()
        inicio = timer() 
        d_gcd = math.gcd(a, b)
        fim = timer()
        t_gcd = fim - inicio # tempo em segundos

        # cronometre mdc()
        inicio = timer() 
        d_mdc = meu_mdc(a, b)
        fim = timer()
        t_mdc = fim - inicio # tempo em segundos

        # verifique respostas
        if d_gcd != d_mdc:
            print(f"SOCORRO! math.gcd({a},{b}) != mdc({a},{b})")
            return None # Abandona
        
        # mostre resultados
        print(f"{a:10} {b:10} {t_gcd:8.2f}   {t_mdc:10.2f}")

        # proximos valores
        a, b = b, a+b

    print("Tempos em segundos")    

#-------------------------------------------                      
def meu_mdc(a, b):
    ''' (int, int) -> int 
    RECEBE dois inteiros a e b.
    RETORNA o mdc entre a e b.
    '''
    aa = abs(a)
    ab = abs(b)
    mdc = min(aa, ab)
    if mdc == 0: return max(aa, ab)
    while (aa % mdc != 0) or (ab % mdc != 0): 
        mdc -= 1
    return mdc
        
#-------------------------------        
if __name__ == "__main__":
    main()
