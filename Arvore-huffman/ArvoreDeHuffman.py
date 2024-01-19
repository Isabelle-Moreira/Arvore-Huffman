from NodoDaArvore import NodoDaArvore
class ArvoreDeHuffman:
    def __init__(self):
        self.raiz = None
        self.nodoEsquerdo= None
        self.nodoDireito=None 

    def FundeChave(self):
        nodo = NodoDaArvore(caractere, frequencia)

        if(self.raiz == None):
            self.raiz = nodo
        else:
            novo_pai = NodoDaArvore(None, self.raiz.frequencia + nodo.frequencia)
            novo_pai.esquerdo = self.raiz
            novo_pai.direito = nodo
            self.raiz = novo_pai

    def CriarNodo(self,pai, Esquerdo,Direito,frequencia):
        pass
    def EscreveArvoreBinario(self):
        pass
    def compactaArquivo(self,arquivo):
        pass
    def descompactaArquivo(self, arvoreBinario, arquivocompactado):
        pass