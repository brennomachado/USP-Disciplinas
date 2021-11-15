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
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    
    listas = [[[],[-5, 7, 99, 104]],
              [[7, 11, 56, 58],[]],
              [[],[]],
              [[7, 11, 56, 58],[7, 11, 56, 58]],
              [[7, 11, 56, 58],[-5, 7, 99, 104]],
              [[7, 11, 56, 58, 58, 58, 60, 80, 90],[-5, 7, 99, 104]],
              [[7, 11, 56],[-5, 7, 99, 104, 201, 201, 202]],
              [[-15, -10, -5, -1],[-30, -20, -10, -5]],
              [[-15, -10, -5, -1],[5, 7, 99, 104]],
              [[7, 11, 56, 58, 58],[-15, -10, -5, -1]],
              [[7, 11, 56, 58],[5, 7, 99, 104]]]
    
    descricao = ["Lista 1 vazia",
                 "Lista 2 vazia",
                 "Duas Listas Vazias",
                 "Duas listas de mesmo tamanho e iguais",
                 "Duas listas de mesmo tamanho diferentes",
                 "Lista 1 maior que a lista 2",
                 "Listas 2 maior que lista 1",
                 "Listas só com numeros negativos",
                 "Lista 1 só com negativos",
                 "Lista 2 só com negativos",
                 "Listas só com positivos"]
    
    numero_de_testes = len(listas)
    i=0
    for lista in listas:
        seq1 = lista[0]
        seq2 = lista[1]
        
        print(f"## Teste {i+1}: {descricao[i]} ##")
        print(f"  Lista 1: {seq1}\n  Lista 2: {seq2}")
        lista = intercale_seqs(seq1, seq2)
        print(f"    Junção das listas: {lista}\n\n")
        i += 1

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2):
    ''' (list, list) -> list

        Recebe seq1 e seq2, duas listas tal que:

            - seq1 é crescente com n1 >= 0 elementos e
            - seq2 é crescente com n2 >= 0 elementos
            
        Retorna uma lista com n1+n2 elementos, contendo
        os elementos de seq1 e seq2 em ordem crescente.

        Exemplo para 
            seq1 = [7, 11, 56] e 
            seq2 = [-5, 7, 99, 104]
            
            
            seq1 = [-, -, -] e 
            seq2 = [-, -, 99, 104]
        
        a função deve retornar a lista:
            [-5, 7, 7, 11, 56, 99, 104]
    '''
    
    indice_seq1 = 0
    indice_seq2 = 0
    tamanho_seq1 = len(seq1)
    tamanho_seq2 = len(seq2)
    lista = []
    tamanho_nova_lista = tamanho_seq1+tamanho_seq2+1
    
    if tamanho_seq1 == 0 or tamanho_seq2 == 0:
        if tamanho_seq1 == 0:
            lista = seq2[:]
        else:
            lista = seq1[:]
        return lista
    
    for i in range(tamanho_nova_lista):
        if indice_seq1 >= tamanho_seq1:
            for j in range(indice_seq2, tamanho_seq2):
                lista.append(seq2[indice_seq2])
                indice_seq2 += 1
            i = tamanho_nova_lista
        elif indice_seq2 >= tamanho_seq2:
            for j in range(indice_seq1, tamanho_seq1):
                lista.append(seq1[indice_seq1])
                indice_seq1 += 1
            i = tamanho_nova_lista
        elif seq1[indice_seq1] <= seq2[indice_seq2]:
            lista.append(seq1[indice_seq1])
            indice_seq1 += 1
        else:
            lista.append(seq2[indice_seq2])
            indice_seq2 += 1
            
    return lista

#--------------------------------------------
if __name__ == '__main__':
    main()