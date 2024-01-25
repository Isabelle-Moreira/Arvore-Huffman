class Ordenator:
    def __init__(self):
        pass
    
    def insercao(self, v):
        for i in range(1, len(v)):
            for j in range(i, 0, -1):
                if v[j].frequencia < v[j - 1].frequencia:
                    aux = v[j]
                    v[j] = v[j - 1]
                    v[j - 1] = aux