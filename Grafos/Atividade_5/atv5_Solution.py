class Grafo(object):
    
    def __init__(self):
        self.grafo = list([] for i in range(100))

    def adiciona_arestas(self, arestas):
        for partida, destino in arestas:
            self.adiciona_arco(partida, destino)


    def adiciona_arco(self, partida, destino):
        self.grafo[int(partida)].append(int(destino))


    def comparar(self,ListadeComparacao, Voos):

        for i in range(Voos):
            partida = int(ListadeComparacao[i][0])
            destino = int(ListadeComparacao[i][1])
            if partida == destino:
                return False
            #  informacoes para entendimento e Debug das comparacoes               ##
            #print("comparar com i =",i,"| partida =",partida,"| destino =",destino)#
            if not(self.dfs(partida, destino)):
                return False
        
        return True
    
    def dfs_recursiva(self, vertice, visitados):
        visitados.add(vertice)
        #print("vertice ", vertice)

        #print("visitados ", visitados)
        for vizinho in self.grafo[vertice]:
            #print("vizinho: ",vizinho)


            if vizinho not in visitados:
                self.dfs_recursiva(vizinho,visitados)

    

    def dfs(self, vertice, destino):
        visitados = set()

        self.dfs_recursiva(vertice,visitados)
        if destino not in visitados:
            return False
        else:
            return True


    def printLista(self):
        for i in range(len(self.grafo)):
            print(i," -> ", self.grafo[i])


def main():
    ## para melhorar legibilidade ###
    #print("inserir numCasos: ")   ##
    #################################

    numCasos = int(input())
    resultadoAB = list()
    resultadoBA = list()


    for i in range(numCasos):
        ## para debug e legibilidade do codigo ###
        #print("inserir numero de Voos 1: ")    ##
        ##########################################
        numVoo1 = int(input())

        ####### para debug e legibilidade do codigo ##########
        #print("inserir ", numVoo1,"s partidas e destinos") ##
        ######################################################
        ListaDeComparacao1 = list()
        for i in range(numVoo1):

            entrada = input()
            listaVoos1 = entrada.split(' ')
            int(listaVoos1[0])
            int(listaVoos1[1])
            ListaDeComparacao1.append(listaVoos1)

        meuGrafo1 = Grafo()
        meuGrafo1.adiciona_arestas(ListaDeComparacao1)

        
        ## para debug e legibilidade do codigo ##
        #meuGrafo1.printLista()                ##
        #print('inserir numero de Voos 2')     ##
        #########################################

        numVoo2 = int(input())
        
        if numVoo1 == 0 or numVoo2 ==0:
            return print(0)
        

        ######## para debug e legibilidade do codigo #########
        #print("inserir ", numVoo2,"s partidas e destinos") ##
        ######################################################

        ListaDeComparacao2 = list()
        for i in range(numVoo2):
            entrada = input()
            listaVoos2 = entrada.split(' ')
            int(listaVoos2[0])
            int(listaVoos2[1])
            ListaDeComparacao2.append(listaVoos2)

        meuGrafo2 = Grafo()
        meuGrafo2.adiciona_arestas(ListaDeComparacao2)
        #meuGrafo2.printLista()

        resultadoAB.append(int(meuGrafo1.comparar(ListaDeComparacao2,numVoo2)))
        resultadoBA.append(int(meuGrafo2.comparar(ListaDeComparacao1, numVoo1)))
            ####### imprimir se encontrou para debug #######
            #print(meuGrafo1.GrafoReach(partida, destino)) #
            ################################################

        ############# para debug #############
        #meuGrafo2.printArquivo("Matriz_2") ##
        ######################################
        

    for i in range(numCasos):
        if resultadoAB[i] == resultadoBA[i]:
            print(resultadoAB[i])
        else:
            print(0)



main()