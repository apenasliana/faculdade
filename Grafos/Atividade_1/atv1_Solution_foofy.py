class Grafo(object):
    listaDeFuncionarios = list()
    matriz = list()
    def __init__(self, numFuncionarios, listaFuncionarios): 
        self.matriz  = [[0 for col in range(int(numFuncionarios))] for row in range(int(numFuncionarios))]
        self.listaDeFuncionarios =  listaFuncionarios

    def adicionarGrafo(self, func1, func2):
        self.matriz[func1-1][func2-1] = 1

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

    def imprimirFuncMaisNovo(self,func):
        
        menor = 1
        
        
        gerenciado = False
        for i in range(len(self.matriz)): 
            if self.matriz[i][func-1] == 1:
                gerenciado = True

        if gerenciado:
            


            element = func - 1
            previous = list()
            i = 0
            while(i < len(self.matriz)):
                if self.matriz[i][element] == 1:
                    
                    previous.append(element)    
                    element = i
                    if int(menor) > int(self.listaDeFuncionarios[i]) or int(menor) == 1:
                        menor = self.listaDeFuncionarios[i]
                    i = 0                        
                else:
                    i = i + 1                    
                    if i == len(self.matriz):
                        if len(previous) > 0:
                            i = element + 1
                            element = previous.pop()
                            

            print(menor)

        else:
            print('*')

        
###############################################################################################
###############################################################################################



def main():

    receber = input()
    listadeinput = receber.split(' ')

    numFuncionarios = listadeinput[0] 
    mrelacoes = listadeinput[1] 
    instrucoes = listadeinput[2]



    listaFuncionarios = list()
    idade = input()
    listaFuncionarios = idade.split(' ')

    meuGrafo = Grafo(numFuncionarios,listaFuncionarios)
    

    listaFuncionarios = idade.split(' ')
    
    for j in range (int (mrelacoes)):
        relacoes = input()
        listaRelacoes = relacoes.split(' ')
        gerente = int(listaRelacoes[0])
        funcionario = int(listaRelacoes[1])

        
        meuGrafo.adicionarGrafo(gerente, funcionario)

    for k in range (int(instrucoes)):
        TipoInstrucao = input()
        listaInstrucao= TipoInstrucao.split(' ')
        if listaInstrucao[0] == 'T':
            func1 = listaInstrucao[1]
            func2 = listaInstrucao[2]
            meuGrafo.mudancadegerente(func1, func2)

        if listaInstrucao[0] == 'P':
            func = listaInstrucao[1]
            meuGrafo.imprimirFuncMaisNovo(int(func)) 
main()