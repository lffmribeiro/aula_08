import csv

# caminho csv
path_arq = ''

# inicializando uma lista
data = []

# usando um gerenciador de contexto
with open(path_arq, mode='r', encoding= 'iso-8859-1') as arquivo:
    #cria o objeto leitor csv
    leitor_csv = csv.DictReader(arquivo)

    #itera as linhas do csv
    for linha in leitor_csv:
        data.append(linha)
    
# Exibe os dados do arquivo csv
for registro in data:
    print(registro)