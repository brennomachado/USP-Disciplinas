"""
  INCLUIR O CABEÇALHO USUAL COM AS SUAS INFORMAÇÕES.

"""

#-----------------------------------------------------------------------
# DEFINIÇÃO DAS CONSTANTES
#-----------------------------------------------------------------------

TAMANHO =  8   
BOLA    = 'O'
XIS     = 'X'
VAZIA   = '.'
MOLDURA = '*'

#-----------------------------------------------------------------------

def main():
    '''  escreva aqui seu comentário para a função main
    '''
      
    # escreva a função principal a seguir ...
    
       
#-----------------------------------------------------------------------
#............ Definição das outras funções do programa .................
#-----------------------------------------------------------------------

def cria_matriz(nlinhas, ncolunas, valor):
    ''' (int, int, tipo do valor) -> matriz 
   
    Cria uma matriz com nlinhas linhas e ncolunas colunas,
    sendo que cada elemento é igual a valor.
    Retorna a matriz criada.
    '''

    # escreva a sua função a seguir

#-----------------------------------------------------------------------

def inicializa_tabuleiro():
    ''' (NoneType) -> matriz

    Cria e retorna uma matriz (com uma moldura) com a configuração
    inicial de um tabuleiro para o jogo Otelo.
    '''

    # escreva a sua função a seguir
    # utilize a função cria_matriz
 
#-----------------------------------------------------------------------
   
def exibe_tabuleiro(tabuleiro):
    ''' (matriz) -> NoneType

    Recebe uma matriz representando um tabuleiro do jogo Otelo
    e imprime esse tabuleiro com as linhas e colunas numeradas
    e tracejadas para facilitar a visualização do usuário.
    '''
 
    print()
    print('      ', end='')
    for i in range(1, TAMANHO+1, 1):
        print('   %d  ' %i, end='')
    print()
   
    print('      ', end='')
    for i in range(1, TAMANHO+1, 1):
        print('+-----', end='')
    print('+')

    for i in range(1, TAMANHO+1, 1):
        print('%5d ' %i, end='')
        for j in range(1, TAMANHO+1, 1):
            print("|  %s  " %(tabuleiro[i][j]), end='')
        print('|')
        
        print('      ', end='')
        for j in range(1, TAMANHO+1, 1):
            print('+-----', end='')
        print('+')
    print()
    
#----------------------------------------------------------------------
   
def numero_reversoes(tabuleiro, jogador, indlin, indcol):
    ''' (matriz, str, int, int) -> int

    Recebe uma matriz tabuleiro, uma marca jogador e uma posição 
    (indlin, indcol).
    A função retorna 0 (zero), se (indlin, indcol) é uma posição 
    fora do tabuleiro ou se esta posição já tiver alguma marca
    ou se o jogador não puder colocar a sua marca nessa posição.
    Em caso contrário, a função retorna o número total de 
    reversões que serão realizadas se o jogador puder colocar
    a sua marca na posição (indlin, indcol).
    '''

    # escreva a sua função a seguir
        
#----------------------------------------------------------------------

def existe_movimento(tabuleiro, jogador):
    ''' (matriz, str) -> bool

    Recebe uma matriz tabuleiro e uma marca jogador.
    A função retorna True, se existir algum movimento válido para o
    jogador; em caso contrário, retorna False.
    '''

    # escreva a sua função a seguir
    # utilize a função num_reversoes
        
#----------------------------------------------------------------------
   
def estrategia_jogo(tabuleiro, jogador):
    ''' (matriz, str) -> int, int, int

    Recebe uma matriz tabuleiro e uma marca jogador.
    Nesta função, supõe-se que jogador é o programa.
    A função determina uma posição (indlin, indcol) para o jogador colocar
    a sua marca, de modo que o número de reversões resultante seja o
    maior possível, e retorna o número de reversões, indlin e indcol.
    Obs.: A função pode supor que, quando ela é chamada, existe algum
    movimento válido para jogador.
    '''

    # escreva a sua função a seguir
    # utilize a função num_reversoes
           
#----------------------------------------------------------------------
   
def coloca_reverte_marca(tabuleiro, jogador, indlin, indcol):  
    ''' (matriz, str, int, int) -> Nonetype

    Recebe uma matriz tabuleiro, uma marca jogador e uma posição
    (indlin, indcol) em que o jogador pode colocar a sua marca.
    A função coloca a marca do jogador na posição (indlin, indcol)
    do tabuleiro e faz todas as reversões necessárias.
    '''

    # escreva a sua função a seguir
             
#----------------------------------------------------------------------
   
def troca_jogador(jogador):
    ''' (str) -> str

    Recebe uma marca jogador e retorna a marca de seu adversário.
    '''

    # escreva a sua função a seguir
             
#----------------------------------------------------------------------
main()
