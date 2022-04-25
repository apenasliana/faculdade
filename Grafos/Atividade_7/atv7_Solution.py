class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Grafo:
    def __init__(self, num):
        self.V = 50050
        self.graph = [None] * self.V
        self.cc = [-1] * self.V

    def adicionarAresta(self, func1, func2):
        node = AdjNode(func2)
        node.next = self.graph[func1]
        self.graph[func1] = node

        node = AdjNode(func1)
        node.next = self.graph[func2]
        self.graph[func2] = node


    def print_agraph(self):
        for i in range(self.V):
            print("Vertice [" + str(i) + "]|", end="")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
    def printcoisa(self):

        aux = self.graph[2]
        print(aux.vertex)


    def caminhoMaisCurto(self): 

        id = 0
        for v in range(self.V):
            if (self.cc[v]== -1):
                id+=1
                self.dfsRconComps( v, id)
        return id
    def dfsRconComps(self, vertice , id):

        self.cc[vertice] = id
        adjacente = self.graph[vertice]
        while adjacente:
            #print(adjacente.vertex)
            if (self.cc[adjacente.vertex] == -1):
                self.dfsRconComps(adjacente.vertex, id)
            adjacente = adjacente.next


def main():

    entrada = input()
    entrada = entrada.split(' ')
    numVertices = int(entrada[0])
    numArestas = int(entrada[1])

    meugrafo = Grafo(numVertices)


    for i in range(numArestas):
        entrada = input()
        entrada = entrada.split(' ')
        elemento1 = int(entrada[0])
        elemento2 = int(entrada[1])
        meugrafo.adicionarAresta((elemento1-1), (elemento2-1))

    #meugrafo.print_agraph()
    print(meugrafo.caminhoMaisCurto())






main()