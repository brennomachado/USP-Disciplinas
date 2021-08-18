nome_arquivo = input("Insira o nome do arquivo txt para leitura: ")
arquivo = open(nome_arquivo, 'r', encoding = 'utf-8')

linha = arquivo.readlines()


print(linha)
