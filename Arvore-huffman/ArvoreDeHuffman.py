from NodoDaArvore import NodoDaArvore
class ArvoreDeHuffman:
    def __init__(self):
        self.raiz = None

    def FundeChave(self, nodo):
        if(self.raiz == None):
            self.raiz = nodo
        else:
            novo_pai = NodoDaArvore(None, self.raiz.frequencia + nodo.frequencia)
            novo_pai.esquerdo = self.raiz
            novo_pai.direito = nodo
            self.raiz = novo_pai


    def EscreveArvoreBinario(self, nodo, arquivo_saida):
        if nodo is not None:
            if nodo.caractere is not None:
                arquivo_saida.write("1" + format(ord(nodo.caractere), '08b'))
            else:
                arquivo_saida.write("0")
                self.EscreveArvoreBinario(nodo.esquerdo, arquivo_saida)
                self.EscreveArvoreBinario(nodo.direito, arquivo_saida)

    def SalvaArvoreBinario(self, nome_arquivo_saida):
        with open(nome_arquivo_saida, "a") as arquivo_saida:
            self.EscreveArvoreBinario(self.raiz, arquivo_saida)
    
    def criaTabelaDeSimbolo(self, nodo, estadoAtual="", tabelaSimbolo={}):
        if nodo is not None:
            if nodo.caractere is not None:
                tabelaSimbolo[nodo.caractere] = estadoAtual
            else: 
                self.criaTabelaDeSimbolo(nodo.esquerdo, estadoAtual+"0", tabelaSimbolo)
                self.criaTabelaDeSimbolo(nodo.direito, estadoAtual+"1", tabelaSimbolo)
        return tabelaSimbolo


    def compactaArquivo(self,caminho_arquivo_entrada, caminho_arquivo_compactado):
        
        tabela_simbolo = self.criaTabelaDeSimbolo(self.raiz)
        arquivo_entrada = open(caminho_arquivo_entrada, "r")
        arquivo_saida = open(caminho_arquivo_compactado, "a")

        self.SalvaArvoreBinario(caminho_arquivo_compactado)
        
        print(tabela_simbolo)
        for linha in arquivo_entrada:
            for caractere in linha:
                arquivo_saida.write(tabela_simbolo[caractere])

        arquivo_saida.close()
        arquivo_entrada.close()
    
    def descompactaArquivo(self, arvoreBinario, arquivocompactado):
        pass

    def printArvore(self, nodo, prefixo="", is_esquerdo=True):
        if nodo is not None:
            print(prefixo + ("|-- " if is_esquerdo else "`-- ") + str(nodo.caractere))
            
            self.printArvore(nodo.esquerdo, prefixo + ("|   " if is_esquerdo else "    "), True)
            self.printArvore(nodo.direito, prefixo + ("|   " if is_esquerdo else "    "), False)