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

def main():
    print("Executando a main() no arquivo horario.py")

    print("Teste da classe Horario")
    t0 = Horario()      ### 
    print("t0 = ", t0)

    print(f"__name__ dentro do arquivo horario.py = {__name__}")
    print("Fim da main() no arquivo horario.py")

def main_velha():
    
    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')

    
class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" como* ilustrado* no enunciado.
    '''
    def __init__(self, h=0, m=0, s=0):
        '''(int, int, int) -> None
        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros "h", "m" e "s" que representam
        hora, minuto e segundos para construção do objeto
        '''
        hora, min, seg = self.padroniza_horario(h,m,s)

        self.dados = [seg, min, hora]
        
    def __str__(self):
        '''(Horario) -> str

        Recebe uma referencia `self` a um objeto da classe Horario e
        cria e retorna a string que representa o objeto.
        '''

        return f"{self.dados[2]:02d}:{self.dados[1]:02d}:{self.dados[0]:02d}"
        
    def padroniza_horario(self, hora, min, seg):
        ''' (Horario, int, int, int) -> int, int, int

        Recebe valores de horas, minutos e segundos e retorna os 3 
        valores correspondentes a horas, minutos e segundos, 
        respectivamente, no formato inteiro: [0,24[ , [0,60[ , [0,60[
        '''

        if seg < 0 or min < 0 or hora < 0:
            return 0, 0, 0

        if seg >= 60:
            min += seg//60
            seg = seg%60
        if min >= 60:
            hora += min//60
            min = min%60
        if hora >= 24:
            hora = hora%24

        return hora, min, seg

    def __add__(self, other):
        ''' (Horario, Horario) -> Horario

        Retorna a soma da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario + Horario
        '''

        return Horario(self.dados[2]+other.dados[2], self.dados[1]+other.dados[1],self.dados[0]+other.dados[0])

    def __sub__(self, other):
        '''(Horario, Horario) -> Horario

        Retorna a substração da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario - Horario
        Retorna 00:00:00 se o valor da substração for < 0
        '''

        min, hora = 0, 0

        seg = self.dados[0] - other.dados[0]
        if seg < 0:
            seg = 60 + seg
            min -= 1
        min += self.dados[1] - other.dados[1]
        if min < 0:
            min = 60 + min
            hora -= 1
        hora += self.dados[2] - other.dados[2]
        
        if hora < 0:
            return Horario()
        else:
            return Horario(hora, min, seg)

    def transforma_em_segundos(self):
        '''(Horario) -> int
        
        Recebe uma referencia `self` a um objeto da classe Horario e
        retorna o valor do Horario convertido em segundos
        '''

        return self.dados[2]*3600 + self.dados[1]*60 + self.dados[0]

    def __eq__(self, other):
        '''(Horario, Horario) -> bool

        Retorna a comparação da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario == Horario
        '''

        return self.dados[0] == other.dados[0] and  self.dados[1] == other.dados[1] and self.dados[2] == other.dados[2]

    def __le__(self, other):
        '''(Horario, Horario) -> bool

        Retorna a comparação da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario <= Horario
        '''

        return self.transforma_em_segundos() <= other.transforma_em_segundos()

    def __ge__(self, other):
        '''(Horario, Horario) -> bool

        Retorna a comparação da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario >= Horario
        '''

        return self.transforma_em_segundos() >= other.transforma_em_segundos()

    def __gt__(self, other):
        '''(Horario, Horario) -> bool

        Retorna a comparação da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario > Horario
        '''

        return self.transforma_em_segundos() > other.transforma_em_segundos()

    def __lt__(self, other):
        '''(Horario, Horario) -> bool

        Retorna a comparação da Horario `self` com Horario `other`.
        Usado pelo Python quando escrevemos Horario < Horario
        '''

        return self.transforma_em_segundos() < other.transforma_em_segundos()


if __name__ == "__main__":
    main_velha()
