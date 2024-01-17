arquivo = open("arquivo-entrada.txt", encoding='latin-1')

dicionario_frequencia ={}

for linha in arquivo:
    for caracter in linha:
        if caracter not in dicionario_frequencia.keys():
            dicionario_frequencia[caracter]=1
        elif caracter in dicionario_frequencia.keys():
            dicionario_frequencia[caracter]+=1

print(dicionario_frequencia)
        

        