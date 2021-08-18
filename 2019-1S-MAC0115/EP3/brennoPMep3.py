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
Exercício-Programa EP3
"""
def main():
    print("Este programa recebe uma data e imprime o dia da semana e o calendário do mês.")
    dia = int(input("\nDigite um dia (inteiro entre 1 e 31): "))
    mes = int(input("\nDigite um mês (inteiro entre 1 e 12): "))
    ano = int(input("\nDigite um ano (inteiro >= 1600): "))
    data_valida = False

    #Verificando a validade da data como todo
    if ano >= 1600:
        ano_bissexto = (ano % 400 == 0) or ((ano % 4 ==0) and (ano % 100 != 0))
        if (mes >0 and mes < 13):
            #No if seguir verifico se o dia é válido de acordo com mês e ano
            if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and (dia >0  and (dia >0  and dia <= 31)):
                data_valida = True
                ultimoDiaMes = 31
            elif (mes==4 or mes==6 or mes==9 or mes==11) and (dia > 0  and dia <=30):
                data_valida = True
                ultimoDiaMes = 30
            elif (ano_bissexto and (dia > 0  and dia <= 29)) or (dia > 0  and dia <=28):
                data_valida = True
                if ano_bissexto:
                    ultimoDiaMes = 29
                else:
                    ultimoDiaMes = 28
            else:
                print("\nData fornecida tem o dia inválido.")

        else:
            print("\nData fornecida tem o mês inválido.")
    else:
        print("\nData fornecida tem o ano inválido.")

    #Seguência de impressão da data válida, dia da semana e do caledário
    if (data_valida):
        print("\nData: %02i/%02i/%i" % (dia, mes, ano))
        a = ano - (14-mes)//12
        k = a + a//4 - a//100 + a//400
        m = mes + 12*((14-mes)//12) - 2
        d = dia + k + ((31*m)//12)
        ds = d % 7
        if(ds==0):
            semana = "Domingo"
        elif(ds==1):
            semana = "Segunda-feira"
        elif(ds==2):
            semana = "Terça-feira"
        elif(ds==3):
            semana = "Quarta-feira"
        elif(ds==4):
            semana = "Quinta-feira"
        elif(ds==5):
            semana = "Sexta-feira"
        elif(ds==6):
            semana = "Sábado"
        print("\nDia da semana:", semana)

        print("\nCalendário: Mês %02d - Ano %d" %(mes, ano))

        print("\n Dom   Seg   Ter   Qua   Qui   Sex   Sáb")
        #Encontrar o primeiro dia da semana do mês para iniciar a impressão do calendário
        a = ano - (14-mes)//12
        k = a + a//4 - a//100 + a//400
        m = mes + 12*((14-mes)//12) - 2
        d = 1 + k + ((31*m)//12)
        ds2 = d % 7

        #Impressão dos espaços no ínicio do calendário
        cont_dia=1
        cont_semana = ds2
        espaco = 0
        while espaco < ds2:
            print("      ", end="")
            espaco = espaco + 1

        #Término da impressão dos dias do calendário
        while cont_dia <= ultimoDiaMes:
            while (cont_semana < 7) and (cont_dia <= ultimoDiaMes):
                print("  %2d  " % cont_dia, end="")
                cont_dia = cont_dia + 1
                cont_semana = cont_semana + 1
            print("")
            cont_semana = 0

main()
