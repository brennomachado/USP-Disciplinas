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

## ==================================================================


import numpy as np

## ------------------------------------------------------------------
def main():

    lista = list(range(20))
    ar = np.array(lista).reshape(4,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1,2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)  
    print(f"img4:\n{img4}\n")

    img5 = NPImagem( (3,2) )
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1,2)
    print(f"img6:\n{img6}\n")

## ------------------------------------------------------------------
class NPImagem:

    def __init__(self, shape, val=0):
        ''' (NPImagem, tuple, obj) -> None
        Constrói um objeto do tipo NPImagem com os atributos:
        self.data : variavel do tipo np.darray, valor(es) de 'val'
        self.shape: tupla que armazena as dimensões da matriz
        '''

        if type(val) is np.ndarray:
            self.data = val
            self.shape = val.shape
        else:
            self.data = np.full(shape, val)
            self.shape = shape
        
    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (NPImagem, tupla) -> self.data.dtype
        Recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição em NPImagem.data[lin,col].
        '''

        lin, col = key
        return self.data[lin, col]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (NPImagem, tupla, obj) -> None
        Recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor na posição self.data[lin,col].
        '''

        lin, col = key
        self.data[lin, col] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (NPImagem) -> str
        Ao ser usada pela função 'print', deve exibir o mesma saída que
        a um objeto do tipo np.darray

        Exemplo: para self.data = np.full((2,3), 0)
        o método deve retornar a string 
        "[[ 0  0  0]
          [ 0  0  0]]" 
        '''

        return f"{self.data}"
        
    # ---------------------------------------------------------------
    def crop(self, sup=None, esq=None, inf=None, dir=None):
        '''(NPImagem, int, int, int int) -> NPImagem
        Recebe uma referência 'self' do tipo NPImagem e quatro numeros 
        inteiros (sup, esq, inf, dir). Retorna uma variavel 'copia' do
        tipo NPimagem que tem dimensões e valores iguais a fatia do 
        tipo np.array self.data[sup:inf,esq:dir]
        '''
        if not (sup or esq or inf or dir):
            copia = self.copia()
        else:
            copia = NPImagem((0,0),self.data[sup:inf,esq:dir].copy())
        
        return copia
    
    # ---------------------------------------------------------------
    def copia(self):
        '''(NPImagem) -> NPImagem
        Recebe uma referência 'self' do tipo NPImagem.
        Retorna uma cópia de 'self'
        '''

        copia_np = NPImagem((0,0), self.data.copy())
        
        return copia_np

## ==================================================================
if __name__ == '__main__':
    main()
