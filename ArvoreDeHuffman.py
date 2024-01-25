from NodoDaArvore import NodoDaArvore
import binascii
import os

def binario_para_decimal(string_binario):
    valor = 0
    potencia = 1
    for i in range(len(string_binario)-1, -1, -1):
        valor+=int(string_binario[i])*potencia
        potencia *= 2
    
    return valor

class ArvoreDeHuffman:
    def __init__(self):
        self.raiz = None
    #faz commit
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


    def compactaArquivo(self, caminho_arquivo_entrada, caminho_arquivo_compactado):
        
        tabela_simbolo = self.criaTabelaDeSimbolo(self.raiz)
        arquivo_entrada = open(caminho_arquivo_entrada, "r")
        arquivo_saida = open(caminho_arquivo_compactado, "a")

        self.SalvaArvoreBinario(caminho_arquivo_compactado)
        
        for linha in arquivo_entrada:
            for caractere in linha:
                arquivo_saida.write(tabela_simbolo[caractere])

        arquivo_saida.close()
        arquivo_entrada.close()
    
    def converteBinario(self, caminho_arquivo_compactado):
        arquivo_entrada = open(caminho_arquivo_compactado, "r")

        # Lê o conteúdo do arquivo de texto
        bitString = arquivo_entrada.read().strip()

        # Converte a sequência de 0s e 1s para uma representação binária
        byte_array = bytearray()
        byte = ''
        for bit in bitString:
            byte += bit
            if(len(byte)==8):
                byte = int(byte, 2)
                byte_array.append(byte)
                byte = ''
        
        if(len(byte)<8):
            while len(byte) < 8:
                byte = '0' + byte
        # Adiciona zeros à esquerda para garantir que a quantidade total de bits seja múltiplo de 8

        # Escreve os dados binários em um novo arquivo
        with open('arquivo_binario.bin', 'wb') as file:
            file.write(byte_array)
        
        arquivo_entrada.close()
        os.remove(caminho_arquivo_compactado)

    def printArvore(self, nodo, prefixo="", is_esquerdo=True):
        if nodo is not None:
            print(prefixo + ("|-- " if is_esquerdo else "`-- ") + str(nodo.caractere))
            
            self.printArvore(nodo.esquerdo, prefixo + ("|   " if is_esquerdo else "    "), True)
            self.printArvore(nodo.direito, prefixo + ("|   " if is_esquerdo else "    "), False)