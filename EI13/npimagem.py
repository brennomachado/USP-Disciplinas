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
        - Revisão do AR12: https://edisciplinas.usp.br/mod/quiz/view.php?id=3900750

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''

## ==================================================================

import numpy as np

## ------------------------------------------------------------------
def main():

    print("======Teste operadores\n")

    imgA = NPImagem( (2,3), 5)
    imgB = NPImagem( (), np.arange(20).reshape(5,4) )
    imgC = imgB.crop(2,1,4,4)
    imgD = imgA + imgC
    print(f"imgA:\n{imgA}")
    print(f"imgB:\n{imgB}")
    print(f"imgC:\n{imgC}")
    print(f"imgD:\n{imgD}")

    print("\n===== Crop ========\n")

    lista = list(range(30))
    ar = np.array(lista).reshape(6,5) 
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 88)
    img3 = img2.crop() ## cria uma cópia
    img2[2,1] = -10
    print(f"img2[2,1]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")

    print("======Teste pinte_retangulo\n")
    img1.pinte_retangulo(1,2,3,5,77)
    print(f"img1.pinte_retangulo(1,2,3,5,99):\n{img1}\n")

    img2.pinte_retangulo(-1,-2,2,3,99)
    print(f"img2.pinte_retangulo(-1,-2,1,2,88):\n{img2}\n")

    img3.pinte_retangulo(1,0,3,4,66)
    print(f"img3.pinte_retangulo(1,0,3,4,77):\n{img3}\n")

    print("======Teste paste\n")
    ar = np.array(lista).reshape(6,5) # É isso que tá faltando na main() de testes descrito no EG13 para os exemplos baterem
    img1 = NPImagem( (0, 0), ar)  # 
    img2 = NPImagem( (2, 3), 99)
    img3 = img1.crop(2,1,5,3) ## cria uma cópia
    print(f"img1:\n{img1}")
    print(f"img2:\n{img2}")
    print(f"img3:\n{img3}")

    img1.paste(img2, 2, 3)
    print(f"img1.paste(img2,2,3):\n{img1}\n")

    img1.paste(img3, 4, 2 )
    print(f"img1.paste(img3,4,2):\n{img1}\n")

    img1.paste(img3, -1, 2)
    print(f"img1.paste(img3,-1,2):\n{img1}\n")

## ------------------------------------------------------------------
class NPImagem():

    def __init__(self, shape, val=0):
        ''' (NPImagem, tuple, obj) -> None
        Constrói um objeto do tipo NPImagem com os atributos:
        self.data : variavel do tipo np.darray, valor(es) de 'val'
        self.shape: tupla que armazena as dimensões da matriz
        '''

        if type(val) is np.ndarray:
            self.data = val
        else:
            self.data = np.full(shape, val)
        
        self.shape = self.data.shape

    def pinte_retangulo(self, sup, esq, inf, dir, v=0):
        ''' (NPImagem, int, int, int, int, int) -> None 
        Recebe 4 inteiros que definem o canto superior-esquerdo (sup, esq) e
        o canto inferior-direito (inf,dir) de uma região retangular com 
        relação a posição (0,0) de self, ou seja, os cantos são "deslocamentos" 
        em pixeis com relação à origem.
        Esse método pinta, com o valor v, os pixeis de self que tenham sobreposição com o retângulo (sup,esq)x(inf,dir). 
        '''

        self_nlins, self_ncols = self.shape
        other_nlins, other_ncols = inf - sup, dir - esq

        # Caso as regiões retangulares não se sobreponham.
        if (sup >= self_nlins) or (esq >= self_ncols) or (inf <= 0) or (dir <= 0): return

        # Verifica se a região retangular dada começa antes da posição (0,0) e pega a posição maior, 
        # que é o início da intersecção a ser pintada
        self_sup = max(sup, 0)
        self_esq = max(esq, 0)

        # Verifica se a região retangular dada termina após a posição final de self. Pega o menor 
        # entre eles, que é o término da interseção a ser pintada
        self_inf = min(sup + other_nlins, self_nlins)
        self_dir = min(esq + other_ncols, self_ncols)
      
        self.data[self_sup:self_inf, self_esq:self_dir] = v

    def paste(self, other, sup=0, esq=0):
        '''(NPImagem, NPImagem, int, int) -> None
        Recebe um objeto NPImagem other e um par de inteiros (sup, esq) 
        que indica um deslocamento em relação à origem de self (posição (0,0)) 
        onde a NPImagem other deve ser sobreposta sobre self. Observe que
        esse deslocamento pode ser negativo. Nesse caso, a dimensão de other
        define o canto inferior-direito do retângulo.
        ''' 

        self_nlins, self_ncols = self.shape
        other_nlins, other_ncols = other.shape

        # posição relativa à (0,0) de onde terminar other.
        inf = sup + other_nlins
        dir = esq + other_ncols

        # Caso as regiões retangulares não se sobreponham.
        if (sup >= self_nlins) or (esq >= self_ncols) or (inf <= 0) or (dir <= 0): return

        # Verifica se a região retangular dada começa antes da posição (0,0) e pega a posição maior, 
        # que é o início da intersecção a ser trocada
        self_sup = max(sup, 0)
        self_esq = max(esq, 0)

        # Verifica se a região retangular dada termina após a posição final de self. Pega o menor 
        # entre eles, que é o término da interseção a ser trocada
        self_inf = min(sup + other_nlins, self_nlins)
        self_dir = min(esq + other_ncols, self_ncols)

        # Não entendi, tinha feito a função toda de outra forma e que funciona, mas vou usar
        # a solução dos profs.
        other_sup = -min(0, sup)
        other_esq = -min(0, esq)
        other_inf = other_sup + self_inf - self_sup
        other_dir = other_esq + self_dir - self_esq
      
        # sobrepondo os retângulos efetivamente
        self.data[self_sup:self_inf, self_esq:self_dir] = other.data[other_sup:other_inf, other_esq:other_dir]


    def __add__(self, other):
        ''' (NPImagem, NPImagem) -> NPImagem
        Recebe dois objetos NPImagem e retorna a soma, elemento-a-elemento,
        dos pixels de self e other.
        '''

        return NPImagem((), self.data + other.data)

    def __mul__(self, other):
        ''' (NPImagem, NPImagem) -> NPImagem
        Recebe dois objetos NPImagem e retorna o produto, elemento-a-elemento,
        dos pixels de self e other.
        '''

        return NPImagem((), self.data * other.data)
    
    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (NPImagem, tupla) -> self.data.dtype
        Recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição em NPImagem.data[lin,col].
        '''

        return self.data[key]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (NPImagem, tupla, obj) -> None
        Recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor na posição self.data[lin,col].
        '''

        self.data[key] = valor

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
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
