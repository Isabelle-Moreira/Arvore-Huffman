from ArvoreDeHuffman import ArvoreDeHuffman
from NodoDaArvore import NodoDaArvore

def SelecionaNodoMenorChave(array_nodos):
    menor_nodo = array_nodos[0]
    for nodo in array_nodos:
        if(nodo.frequencia < menor_nodo.frequencia):
            menor_nodo = nodo
    
    return menor_nodo


arquivo = open("arquivo-entrada.txt", encoding='latin-1')

dicionario_frequencia ={}

for linha in arquivo:
    for caractere in linha:
        if caractere not in dicionario_frequencia.keys():
            dicionario_frequencia[caractere]=1
        elif caractere in dicionario_frequencia.keys():
            dicionario_frequencia[caractere]+=1

array_nodos = []

for chave in dicionario_frequencia.keys():
    nodo = NodoDaArvore(chave, dicionario_frequencia[chave])
    array_nodos.append(nodo)

menor_nodo = SelecionaNodoMenorChave(array_nodos)

print(dicionario_frequencia)
print(array_nodos)
print("CARACTERE", menor_nodo.caractere)
print("FREQUENCIA", menor_nodo.frequencia)