from ArvoreDeHuffman import ArvoreDeHuffman
from NodoDaArvore import NodoDaArvore
from ordenador import Ordenator

ordenador = Ordenator()

def SelecionaNodoMenorChave(array_nodos):
    menor_nodo = array_nodos[0]
    for nodo in array_nodos:
        if(nodo.frequencia < menor_nodo.frequencia):
            menor_nodo = nodo
    
    return menor_nodo

nome_arquivo = "compactacao1M.txt"
arquivo = open(nome_arquivo, encoding='latin-1')

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

ordenador.insercao(array_nodos)
while len(array_nodos)!=1:
    menor_nodo = array_nodos[0]
    segundo_menor_nodo = array_nodos[1]
    novo_nodo = NodoDaArvore(None, menor_nodo.frequencia+segundo_menor_nodo.frequencia)
    
    novo_nodo.esquerdo = menor_nodo
    novo_nodo.direito = segundo_menor_nodo
    
    menor_nodo.pai = novo_nodo
    segundo_menor_nodo.pai = novo_nodo
    
    array_nodos.remove(menor_nodo)
    array_nodos.remove(segundo_menor_nodo)
    array_nodos.append(novo_nodo)

    ordenador.insercao(array_nodos)

arvoreHuffman.raiz = array_nodos[0]

arvoreHuffman.printArvore(arvoreHuffman.raiz)

#tabela= arvoreHuffman.criaTabelaDeSimbolo(arvoreHuffman.raiz)

arvoreHuffman.compactaArquivo(nome_arquivo, "arquivo_saida.txt")
arvoreHuffman.converteBinario("arquivo_saida.txt")

#arquivo_compactado = open("arquivo_saida.txt", "r")
#conteudo = arquivo_compactado.readline()

#arvoreHuffman.raiz = None

#arvoreHuffman.descompactaArquivo("arquivo_saida.txt")