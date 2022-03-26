class Grafo(object):
    listaDeFuncionarios = list()
    matriz = list()
    def __init__(self, numFuncionarios, listaFuncionarios): 
        self.matriz  = [[0 for col in range(int(numFuncionarios))] for row in range(int(numFuncionarios))]
        self.listaDeFuncionarios =  listaFuncionarios

    def adicionarGrafo(self, func1, func2):
        self.matriz[func1-1][func2-1] = 1
        #debug- printar matriz
        #for i in self.matriz:
        #    print(i)

    def mudancadegerente(self, func1, func2):

        for index, line in enumerate(self.matriz):
            ind1 = line[int(func1) -1]
            ind2 = line[int(func2) -1]

            line[int(func1) -1] = ind2
            line[int(func2) -1] = ind1

    
        row = self.matriz[int(func1) - 1]
        row2 = self.matriz[int(func2) - 1]
        self.matriz[int(func1) - 1] = row2
        self.matriz[int(func2) - 1] = row

    def AcharMenorRECURSIVO(self, func, menor):
        
        element = func
        for i in range(len(self.matriz)):
            #print("for1: ", i) para fins de debug
            if self.matriz[i][element] == 1:
                if int(menor) > int(self.listaDeFuncionarios[i]) or int(menor) == 0:
                    menor = self.listaDeFuncionarios[i]
                    #print("loop: ", menor) para fins de debug
                menor = self.AcharMenorRECURSIVO(i, menor)

        return menor

    def acharMenor(self, func):

        menor = 0
        gerenciado = False
        for i in range(len(self.matriz)):
            if self.matriz[i][func-1] == 1:
                gerenciado = True
        if gerenciado:
            
            print(self.AcharMenorRECURSIVO(func -1,menor))
        else:
            print('*') 

    #Para debug
        """"
    def getFuncionarios(self):
    
        print("------------------------------------")
        for i in self.matriz:
            print(i)
        print("------------------------------------")

        """




################################################################################################
#                                     Classe para debug
################################################################################################
        """
class dados():
    def getdados(numFunc,numRelacoes,numInstrucao):
        print("------------------------------------")
        print("numFuncionarios || mrelacoes || intrucoes ")
        print(numFunc, numRelacoes, numInstrucao)
        print("------------------------------------")

    def getListaFunc(numFunc,listaFunc):

        print("------------------------------------")
        print("idade ")
        print(listaFunc)
        print("------------------------------------")

    def getAresta(ger,func):   

        print("------------------------------------")
        print("gerente e funcionarios ")
        print(ger, func)
        print("------------------------------------")



    def getInstruT(listaFuncionarios, func1, func2):
            
        print("------------------------------------")
        print("Instrucao T ")
        print(func1,func2)
        print(listaFuncionarios)
        print("------------------------------------")

    def getInstruP( func):
            print("------------------------------------")
            print("Instrucao P ")
            print(func)
            print("------------------------------------")

    def getFuncionarios(listaFuncionarios):
    
        print("------------------------------------")
        print(listaFuncionarios)
        print("------------------------------------")
     """
###############################################################################################
###############################################################################################



def main():

    receber = input()
    listadeinput = receber.split(' ')

    numFuncionarios = listadeinput[0] 
    mrelacoes = listadeinput[1] 
    instrucoes = listadeinput[2]

    #Debug
    #dados.getdados(numFuncionarios,mrelacoes,instrucoes)


    listaFuncionarios = list()
    idade = input()
    listaFuncionarios = idade.split(' ')
    meuGrafo = Grafo(numFuncionarios,listaFuncionarios)
    
    #Debug
    #dados.getListaFunc(numFuncionarios, listaFuncionarios)

    listaFuncionarios = idade.split(' ')
    
    for j in range (int (mrelacoes)):
        relacoes = input()
        listaRelacoes = relacoes.split(' ')
        gerente = int(listaRelacoes[0]) 
        funcionario = int(listaRelacoes[1])
        meuGrafo.adicionarGrafo(gerente, funcionario)

        #Debug
        #dados.getAresta(gerente,funcionario)

    for k in range (int(instrucoes)):
        TipoInstrucao = input()
        listaInstrucao= TipoInstrucao.split(' ')
        if listaInstrucao[0] == 'T':
            func1 = listaInstrucao[1]
            func2 = listaInstrucao[2]

            #Debug
            #dados.getInstruT(listaFuncionarios, func1, func2)

            meuGrafo.mudancadegerente(func1, func2)
            #meuGrafo.getFuncionarios() para fins de debug
        if listaInstrucao[0] == 'P':
            func = listaInstrucao[1]
            #Debug
            #dados.getInstruP(func)
            meuGrafo.acharMenor(int(func)) 

main()