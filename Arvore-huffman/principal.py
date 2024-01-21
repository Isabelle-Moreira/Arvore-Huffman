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


arvoreHuffman = ArvoreDeHuffman()

while len(array_nodos)!=0:
    menor_nodo = SelecionaNodoMenorChave(array_nodos)
    arvoreHuffman.FundeChave(menor_nodo)
    array_nodos.remove(menor_nodo)

tabela= arvoreHuffman.criaTabelaDeSimbolo(arvoreHuffman.raiz)

arvoreHuffman.compactaArquivo("arquivo-entrada.txt", "arquivo_saida.txt")

print("ARVORE ESPERADA")
arvoreHuffman.printArvore(arvoreHuffman.raiz)

arquivo_compactado = open("arquivo_saida.txt", "r")
conteudo = arquivo_compactado.readline()

arvoreHuffman.raiz = None

arvoreHuffman.constroiArvore(None, arvoreHuffman.raiz, '', conteudo, 0)



print("ÁRVORE CONSTRUIDA")
arvoreHuffman.printArvore(arvoreHuffman.raiz)
