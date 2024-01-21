from NodoDaArvore import NodoDaArvore
import binascii

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

    def constroiArvore(self, pai, nodo, direcao, bitString, bitStringIndex):
        '''
            CRIO O NODO
            - Se a string que estou lendo é 0, ele desce pela esquerda
            - Se a string que estou lendo é 0 e eu DESCI pela esquerda,
              então filho esquerdo do pai vira o novo nodo
            - Se a string que estou lendo é 0 e eu DESCI pela direita,
              então o filho direito do pai recebe o novo nodo
            - Se é 1, é uma folha e eu paro de chamar o método. Eu vejo se ela desceu
               pela esquerda ou pela direita.
        '''
        
        nodo = NodoDaArvore(None, 0)
        if self.raiz == None:
            self.raiz = nodo
            nodo = self.raiz
        
        while self.raiz.direito == None:
            bit = bitString[bitStringIndex]
            if bit=="0":
                novo_nodo = NodoDaArvore(None, 0)
                novo_nodo.pai = nodo
                nodo.esquerdo = novo_nodo

                nodo = nodo.esquerdo

                bitStringIndex+=1

            if bit == "1":
                caractere_bits=''
                for i in range(bitStringIndex+1, bitStringIndex+9, 1):
                    caractere_bits+=bitString[i]
                
                caractere_bits = caractere_bits.encode('ascii')
                caractere_ascii = binascii.b2a_uu(caractere_bits)
                
                bitStringIndex+=9
                novo_nodo = NodoDaArvore(None, 0)
                novo_nodo.pai = nodo
                novo_nodo.caractere = caractere_ascii.decode()

                if nodo.esquerdo == None:
                    nodo.esquerdo = novo_nodo
                elif nodo.direito == None:
                    nodo.direito = novo_nodo
                    nodo = nodo.pai

        
    def descompactaArquivo(self, arvoreBinario, arquivocompactado):
        pass

    def printArvore(self, nodo, prefixo="", is_esquerdo=True):
        if nodo is not None:
            print(prefixo + ("|-- " if is_esquerdo else "`-- ") + str(nodo.caractere))
            
            self.printArvore(nodo.esquerdo, prefixo + ("|   " if is_esquerdo else "    "), True)
            self.printArvore(nodo.direito, prefixo + ("|   " if is_esquerdo else "    "), False)