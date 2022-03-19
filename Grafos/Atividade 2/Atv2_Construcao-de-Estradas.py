import math

class Grafo(object):
    def __init__(self, numCidades, cidadesCord, rodovias,):
        self.cidades = dict()
        self.numCidades = numCidades
        for i in range(numCidades):
            self.cidades[i + 1] = cidadesCord[i]
        self.rodovias = rodovias
        self.matriz = list()
            

    def getCidades(self):
        return self.cidades

    def getRodovias(self):
        return self.rodovias
    
    def numRodovias(self):
        return len(self.rodovias)

    def getDistancia(self, cidade1, cidade2):
        distancia = math.sqrt((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)
        return round(distancia)

    def getMatrizDeAdjacencia(self):
        for chave in self.cidades:
            distancias = list()
            for novaChave in self.cidades:
                if chave != novaChave:
                    distancias.append(self.getDistancia(self.cidades[chave], self.cidades[novaChave]))
                else:
                    distancias.append(0)
            self.matriz.append(distancias)

        for rodovia in self.rodovias:
            # Trataremos estradas já existentes como tendo peso 0 para efeitos de calculo
            self.matriz[rodovia[0] - 1][rodovia[1] - 1] = 0
            self.matriz[rodovia[1] - 1][rodovia[0] - 1] = 0
        return self.matriz

    def caminhoMaisCurto(self):
        # Variavel responsavel por listar todas as rodovias possiveis e suas respectivas distancias       
        listaDeArestas = list()
        for lin in range(len(self.matriz)):
            for col in range(len(self.matriz[lin])):
                if lin > col:
                    listaDeArestas.append([self.matriz[lin][col], lin + 1, col + 1])
        # listar as rodovias em ordem crescente
        listaDeArestas.sort(key=lambda x: x[0])

        # guardar o valor total de estradas a serem construidas
        valorTotal = 0

        # lista de conjuntos já conectados para o algoritmo de kruskal
        listaDeConjuntos = list()
        for aresta in listaDeArestas:
            if len(listaDeConjuntos) < 1:
                valorTotal += aresta[0]
                listaDeConjuntos.append({aresta[1], aresta[2]})
            elif len(listaDeConjuntos[0]) != self.numCidades:
                # caso 1: vertice 1 pertence há algum conjunto, vertice 2 não pertence há nenhum conjunto
                if self.findSet(listaDeConjuntos, aresta[1]) != -1 and self.findSet(listaDeConjuntos, aresta[2]) == -1:
                    index = self.findSet(listaDeConjuntos, aresta[1])
                    listaDeConjuntos[index] = listaDeConjuntos[index].union({aresta[1], aresta[2]})
                    valorTotal += aresta[0]
                # caso 2: vertice 1 não pertence há nenhum conjunto, vertice 2 pertece há algum conjunto
                elif self.findSet(listaDeConjuntos, aresta[1]) == -1 and self.findSet(listaDeConjuntos, aresta[2]) != -1:
                    index = self.findSet(listaDeConjuntos, aresta[2])
                    listaDeConjuntos[index] = listaDeConjuntos[index].union({aresta[1], aresta[2]})
                    valorTotal += aresta[0]
                # caso 3: tanto vertice 1 quanto 2 não pertecem há nenhum conjunto
                elif self.findSet(listaDeConjuntos, aresta[1]) == -1 and self.findSet(listaDeConjuntos, aresta[2]) == -1:                
                    listaDeConjuntos.append({aresta[1], aresta[2]})
                    valorTotal += aresta[0]
                # caso 4: tanto vertice 1 quanto 2 pertecem há algum conjunto
                elif self.findSet(listaDeConjuntos, aresta[1]) != -1 and self.findSet(listaDeConjuntos, aresta[2]) != -1:
                    index1 = self.findSet(listaDeConjuntos, aresta[1])
                    index2 = self.findSet(listaDeConjuntos, aresta[2])
                    # caso 4.1: vertice 1 e 2 pertencem ao mesmo conjunto
                    if index1 != index2:
                        valorTotal += aresta[0]
                        listaDeConjuntos[index1] = listaDeConjuntos[index1].union(listaDeConjuntos[index2])
                        del listaDeConjuntos[index2]
        print(valorTotal)

    def findSet(self, lista, valor):
        # lista de conjuntos
        for i in range(len(lista)):
            if valor in lista[i]:
                return i
        return -1

                


def main():
    numCidades = int(input())
    listaDeCoordenadas = list()
    listaDeEstradas = list()
     
    for i in range(numCidades):
        parCoordenadas = input()
        coords = parCoordenadas.split(' ')
        coords[0] = int(coords[0])
        coords[1] = int(coords[1].replace('\n', ''))
        listaDeCoordenadas.append(coords)

    for j in range(int(input())):
        estrada = input()
        estrada = estrada.split(' ')
        estrada[0] = int(estrada[0])
        estrada[1] = int(estrada[1].replace('\n', ''))
        listaDeEstradas.append(estrada)


    meuGrafo = Grafo(numCidades, listaDeCoordenadas, listaDeEstradas)
    meuGrafo.getRodovias()
    meuGrafo.caminhoMaisCurto()


        
main()
