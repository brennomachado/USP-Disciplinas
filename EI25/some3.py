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
        [],
        [2, 77],
        [44, 11, 77, 33],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 5, 4, 3],
        [5, 4 ,1, 3, 2],
        [44, 11, 77, 33, 20, 10],
    ]
    i = 0
    for t in testes:
        
        print(f"#### Teste {i} ####")
        s3 = Soma3(t)
        print(f"\nCriação usando a lista:\nent : {t}")
        print(f"  {s3}")
        
        print("\nDicionário de posições:")
        s3.monte_dicio_pos()
        print(f"{s3}")

        print("\nPares")
        s3.imprima_pares()

        print("\nTrios")
        s3.imprima_trios()
        
        i+=1
        print("--------\n")

# ===================================================================

class Soma3:

    def __init__(self, seq):
        ''' (Soma3, list) -> None
        '''
        self.data = seq  # faz referência, não copia.
        self.pos = {}

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

# ===================================================================

if __name__ == '__main__':
    main()