lista = list([] for i in range(50001))
cc = list()


def dfs(vertice):
    #print(vertice)
    for index in lista[vertice]:
        if cc[index] == -1:
            cc[index] = cc[vertice]
            dfs(index)

def printLista():
    for i in range(len(lista)):
        print(i," -> ", lista[i])

def main():
    
    entrada = input()
    entrada = entrada.split(' ')
    numVertices = int(entrada[0])
    numArestas = int(entrada[1])

    for comp in range(numVertices):
        
        cc.append(-1)



    for i in range(numArestas):
        entrada = input()
        entrada = entrada.split(' ')
        elemento1 = int(entrada[0])
        elemento2 = int(entrada[1])
        lista[elemento1-1].append(elemento2-1)
        lista[elemento2-1].append(elemento1-1)

    numComp = 0
    #printLista()
    for index in range(numVertices):
        if cc[index] == -1:
            numComp+=1
            cc[index] = numComp

            dfs(index)


    print(numComp)
    
    
main()