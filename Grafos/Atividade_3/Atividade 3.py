class Grafo(object):
    matriz = list()
    caminhos = 0
    
    def __init__(self, numAtividades): 
        self.matriz  = [[0 for col in range(int(numAtividades))] for row in range(int(numAtividades))]


    def adicionarGrafo(self, func1, func2):
        self.matriz[func1-1][func2-1] = 1
        #debug- printar matriz
        #for i in self.matriz:
        #    print(i)

###########################################################################################

    def AcharMenorRECURSIVO(self, next):
        
        isNext = False
        
        for i in range(len(self.matriz)):
            if self.matriz[next][i] == 1:                
                #print("linha: ", next, "coluna: ", i)
                self.AcharMenorRECURSIVO(i)
                isNext = True
        if isNext != True:
            self.caminhos += 1
            #print("___________________________")
            #print("| caminho:" , self.caminhos, "| linha: ", next, " |")
            #print("---------------------------")
    def acharMenor(self):

        isNext = False
        next = 0
        for i in range(len(self.matriz)):
            if self.matriz[0][i] == 1:
                isNext = True
        if isNext:        
            self.AcharMenorRECURSIVO(next)
        else:
            print(self.caminhos)

    def getCaminhos(self):
        return self.caminhos

############################################################################################

def main():

    numAtividades = input()

    meuGrafo = Grafo(numAtividades)
    aux = 0

    while aux != -1:
        
        relacoes = input()
        listaRelacoes = relacoes.split(' ')
        coiso1 = int(listaRelacoes[0]) 
        coiso2 = int(listaRelacoes[1])

        if coiso1 == -1 or coiso2 == -1:
            aux = -1
        else:
            meuGrafo.adicionarGrafo(coiso1, coiso2)

    meuGrafo.acharMenor()
    print(meuGrafo.getCaminhos())

main()
