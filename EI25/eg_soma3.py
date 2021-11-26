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

# https://docs.python.org/3/library/bisect.html
from bisect import bisect_left

## ==================================================================
# 
def main():
    '''
    Testes da classe Soma 3

    inclua mais 10 testes usando listas diferentes. Por exemplo, 
    o que deve acontecer com listas vazias, listas com números negativos,
    listas ordenadas, etc.
    '''
    print("Testes do EI25 - Soma3")

    testes = [
        [44, 11, 77, 33],
        [30, -30, -20, -10, 40 ,0,10,15]
    ]

    for t in testes:

        s3 = Soma3(t)
        print(f"\nCriação usando a lista:\nent : {t}")
        print(f"{s3}")

        print("\nDicionário de posições:")
        s3.monte_dicio_pos()
        print(f"{s3}")

        print("\nPares")
        s3.imprima_pares()

        print("\nTrios")
        s3.imprima_trios()
        
        print("TESTE SOMA ZERO")
        s3 = Soma3(t)
        print(f"  Força bruta: {s3.forca_bruta()} trios somam Zero")
        s3 = Soma3(t)
        print(f"  Busca binária: {s3.busca_binaria()} trios somam Zero")
        s3 = Soma3(t)
        print(f"  Dicionário: {s3.dicionario()} trios somam Zero")
        s3 = Soma3(t)
        print(f"  Mistério: {s3.misterio()} trios somam Zero")

#---------------------------------------------------------
# Função auxiliar 
def index(a, x, e, d):
    '''(list, obj, int, int) -> int ou None
    RECEBE uma lista a um objeto x e dois inteiros lo e hi.
    RETORNA um índice i, e <= i < d, tal que a[i]==x 
        ou retorna None se um tal índice não existe. 
    NOTA: o consumo de tempo da função é O(lg n) em que
        n = d-e. Ver https://docs.python.org/3/library/bisect.html  
    '''
    i = bisect_left(a, x, e, d)
    if i != len(a) and a[i] == x: return i
    return None # raise ValueError
        
# ===================================================================

class Soma3:
    def __init__(self, seq):
        ''' (Soma3, list) -> None
        '''
        self.data = seq  # faz referência, não copia.
        self.pos = {}

    # -------------------------------------------------------------------       
    def __str__(self):
        ''' (Soma3) -> None
        '''
        return f'data: {self.data}\npos : {self.pos}\n'

    # -------------------------------------------------------------------
    def imprima_pares(self):
        ''' (Soma3) -> None

            Imprime todos os pares da lista self.data.
            Exemplo: para self.data = [44, 11, 77, 88]
            o método deve imprimir:
            44  11
            44  77 
            44  88
            11  77
            11  88
            77  88
        '''
        tamanho = len(self.data)
        for i in range(tamanho):
            for j in range(i+1, tamanho):
                print(f"{self.data[i]} {self.data[j]}")

    # -------------------------------------------------------------------

    def imprima_trios(self):
        ''' (Soma3) -> None

            Imprime todos os trios da lista self.data.
            Exemplo: para self.data = [44, 11, 77, 88]
            o método deve imprimir:
            44  11  77
            44  11  88
            44  77  88
            11  77  88
        '''
        tamanho = len(self.data)
        for i in range(tamanho):
            for j in range(i+1, tamanho):
                for k in range(j+1, tamanho):
                    print(f"{self.data[i]} {self.data[j]} {self.data[k]}")

    # -------------------------------------------------------------------

    def monte_dicio_pos(self):
        ''' (Soma3) -> None
            Monta o dicionário self.pos a partir do conteúdo em self.data. 
            Usando cada elemento de self.data como chave, self.pos armazena
            o índice desse elemento na lista self.data. 

            Exemplo: para self.data = [44, 11, 77, 88]
            então self.pos deve conter {44:0, 11:1, 77:2, 88:3}
        '''
        for i in range(len(self.data)):
            self.pos[self.data[i]] = i
    #---------------------------------------------------------
    def forca_bruta(self):
        '''(Soma3) -> int
            RECEBE um objeto Soma3 self.
            RETORNA o número de trios em self.data que somam zero. 

            Para projetar este método procure seguir as recomendações 
                do EG.

            EXEMPLOS

            In [17]: v = [30, -30, -20]
            In [18]: t = Soma3(v)
            In [19]: t.forca_bruta()
            Out[19]: 0

            In [20]: v = [30, -30, -20, -10]
            In [21]: t = Soma3(v)
            In [22]: t.forca_bruta()
            Out[22]: 1

            In [23]: v = [30, -30, -20, -10, 40]
            In [24]: t = Soma3(v)
            In [25]: t.forca_bruta()
            Out[25]: 2

            In [26]: v = [30, -30, -20, -10, 40, 0]
            In [27]: t = Soma3(v)
            In [28]: t.forca_bruta()
            Out[28]: 3

            In [29]: v = [30, -30, -20, -10, 40, 0, 10]
            In [30]: t = Soma3(v)
            In [31]: t.forca_bruta()
            Out[31]: 4

            In [32]: v = [30, -30, -20, -10, 40, 0, 10, 15]
            In [33]: t = Soma3(v)
            In [34]: t.forca_bruta()
            Out[34]: 4
        '''
        tamanho = len(self.data)
        trios = 0
        dt = self.data
        for i in range(tamanho):
            for j in range(i+1, tamanho):
                dupla = dt[i] + dt[j]
                for k in range(j+1, tamanho):
                    if (dupla + dt[k]) == 0 :
                        trios += 1 
        return trios
    
    #---------------------------------------------------------        
    def busca_binaria(self):
        '''(Soma3) -> int
            RECEBE um objeto Soma3 self.
            RETORNA o número de trios em self.data que somam zero. 

            EXEMPLOS

            In [35]: v = [30, -30, -20]
            In [36]: t = Soma3(v)
            In [37]: t.busca_binaria()
            Out[37]: 0

            In [38]: v = [30, -30, -20, -10]
            In [39]: t = Soma3(v)
            In [40]: t.busca_binaria()
            Out[40]: 1

            In [41]: v = [30, -30, -20, -10, 40]
            In [42]: t = Soma3(v)
            In [43]: t.busca_binaria()
            Out[43]: 2

            In [44]: v = [30, -30, -20, -10, 40, 0]
            In [45]: t = Soma3(v)
            In [46]: t.busca_binaria()
            Out[46]: 3

            In [47]: v = [30, -30, -20, -10, 40, 0, 10]
            In [48]: t = Soma3(v)
            In [49]: t.busca_binaria()
            Out[49]: 4

            In [50]: v = [30, -30, -20, -10, 40, 0, 10, 15]
            In [51]: t = Soma3(v)
            In [52]: t.busca_binaria()
            Out[52]: 4
        '''
        dt = self.data # apelido 
        n = len(dt)
        conta = 0
        dt.sort()
        for i in range(n):
            for j in range(i+1, n):
                k = index(dt, -(dt[i] + dt[j]), j+1, n)
                if k != None: conta += 1 
        return conta
            
    #---------------------------------------------------------        
    def dicionario(self):
        '''(Soma3) -> int
            RECEBE um objeto Soma3 self.
            RETORNA o número de trios em self.data que somam zero. 

            Para projetar este método procure seguir as recomendações 
                do EG.

            EXEMPLOS

            In [2]: v = [30, -30, -20]
            In [3]: t = Soma3(v)
            In [4]: t.dicionario()
            Out[4]: 0

            In [5]: v = [30, -30, -20, -10]
            In [6]: t = Soma3(v)
            In [7]: t.dicionario()
            Out[7]: 1

            In [8]: v = [30, -30, -20, -10, 40]
            In [9]: t = Soma3(v)
            In [10]: t.dicionario()
            Out[10]: 2

            In [11]: v = [30, -30, -20, -10, 40, 0]
            In [12]: t = Soma3(v)
            In [13]: t.dicionario()
            Out[13]: 3

            In [14]: v = [30, -30, -20, -10, 40, 0, 10]
            In [15]: t = Soma3(v)
            In [16]: t.dicionario()
            Out[16]: 4

            In [17]: v = [30, -30, -20, -10, 40, 0, 10, 15]
            In [18]: t = Soma3(v)
            In [19]: t.dicionario()
            Out[19]: 4
        '''
        self.monte_dicio_pos()
        tamanho = len(self.data)
        trios = 0
        dt = self.data
        for i in range(tamanho):
            for j in range(i+1, tamanho):
                val = -(dt[i] + dt[j])
                if val in self.pos:
                    if self.pos[val] > j:
                        trios += 1
        return trios
    
    #---------------------------------------------------------        
    def misterio(self):
        '''(Soma3) -> int
        RECEBE um objeto Soma3 self.
        RETORNA o número de trios em self.data que somam zero. 
        '''
        dt = self.data
        n = len(dt)
        conta = 0
        dt.sort()
        for i in range(n-2):
            x = dt[i]
            e = i+1
            d = n-1
            while e < d:
                y = dt[e]
                z = dt[d]
                soma = x + y + z 
                if soma == 0:
                    conta += 1
                    e += 1
                    d -= 1
                elif soma > 0: d -= 1
                else: e += 1
        return conta
        
# ===================================================================

if __name__ == '__main__':
    main()
