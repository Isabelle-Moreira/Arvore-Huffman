from NodoDaArvore import NodoDaArvore
import binascii

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


    def compactaArquivo(self,caminho_arquivo_entrada, caminho_arquivo_compactado):
        
        tabela_simbolo = self.criaTabelaDeSimbolo(self.raiz)
        arquivo_entrada = open(caminho_arquivo_entrada, "r")
        arquivo_saida = open(caminho_arquivo_compactado, "a")

        self.SalvaArvoreBinario(caminho_arquivo_compactado)
        
        for linha in arquivo_entrada:
            for caractere in linha:
                arquivo_saida.write(tabela_simbolo[caractere])

        arquivo_saida.close()
        arquivo_entrada.close()

    def constroiArvore(self, nodo, bitString, bitStringIndex):
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
        bitStringIndex+=1
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
                
                caractere_decimal = binario_para_decimal(caractere_bits)
                caractere_ascii = chr(caractere_decimal)
                
                bitStringIndex+=9
                novo_nodo = NodoDaArvore(None, 0)
                novo_nodo.pai = nodo
                novo_nodo.caractere = caractere_ascii

                if nodo.esquerdo == None:
                    nodo.esquerdo = novo_nodo
                elif nodo.direito == None:
                    nodo.direito = novo_nodo
                    nodo = nodo.pai

        return bitStringIndex
        
    def descompactaArquivo(self, caminho_arquivo_compactado):
        arquivo_descompactado = open('arquivo_descompactado.txt', "a")
        arquivo_compactado = open(caminho_arquivo_compactado)

        conteudo_compactado = arquivo_compactado.readline()

        index_do_ultimo_bit_lido = self.constroiArvore(self.raiz, conteudo_compactado, 0)

        tabela = self.criaTabelaDeSimbolo(self.raiz)
        print(tabela)
        print(index_do_ultimo_bit_lido)
        for i in range(13):
            print(conteudo_compactado[index_do_ultimo_bit_lido+i])
        
        
        nodo_busca = self.raiz
        #Então, construa a árvore
        for i in range (index_do_ultimo_bit_lido, len(conteudo_compactado), 1):
            bit = conteudo_compactado[i]

            if bit == "0":
                nodo_busca = nodo_busca.esquerdo
            if bit == "1":
                nodo_busca = nodo_busca.direito
            #Se encontrou uma folha, escreva o caractere correspondente e volte para a raiz
            if nodo_busca.esquerdo is None and nodo_busca.direito is None:
                arquivo_descompactado.write(nodo_busca.caractere)
                nodo_busca = self.raiz
            #Se não é folha, veja o bit lido. Se for 0, desça pela esquerda.
            #Se não, desça pela direita.
            

        arquivo_descompactado.close()
        arquivo_compactado.close()

    def printArvore(self, nodo, prefixo="", is_esquerdo=True):
        if nodo is not None:
            print(prefixo + ("|-- " if is_esquerdo else "`-- ") + str(nodo.caractere))
            
            self.printArvore(nodo.esquerdo, prefixo + ("|   " if is_esquerdo else "    "), True)
            self.printArvore(nodo.direito, prefixo + ("|   " if is_esquerdo else "    "), False)