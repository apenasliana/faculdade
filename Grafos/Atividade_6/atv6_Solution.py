class Graph:
	Inf = 9999
	somapreco = 0
	def __init__(self, vertices):
		self.V = vertices 
		self.graph = []


	def addEdge(self, u, v, w):
		self.graph.append([u-1, v-1, w])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		print("Vertex | Distance ")
		for i in range(self.V):
			if dist[i] == 0:
				print('[', i, '] |->','Source')
			else:
				print('[', i, '] |->',dist[i])

	def BellmanFord(self, src):


		dist = list()
		for i in range(self.V):
			if i == 0:
				dist.append([[],0])
			else:
				dist.append([[],self.Inf])

		for _ in range(self.V - 1):

			index = 0
			for u, v, w in self.graph:
				if w != -1:

					if dist[u][1] != self.Inf and dist[u][1] + w < dist[v][1]:
						dist[v][0] = dist[v][0] + dist[u][0]
						dist[v][0].append(u)
						dist[v][1] = dist[u][1]+w
						print('trefco?', dist[v])
						#self.printArr(dist)

				
				index+=1

		return dist.pop()


	def precoFinal(self,numAmigos,numAssentos):
		self.somapreco = 0
		print('dogao 5 real')
		while numAmigos > 0:
			variavel = self.BellmanFord(0)
			print('opameubom', variavel)
			#print(variavel[0], ' || ',print(variavel[1]))
			#if len(variavel[0]) == 0 :
			#	return 'impossivel'
			for i in variavel[0]:
				self.graph[i][2] = -1
			for i in self.graph:
				print(i)
			if numAmigos >= numAssentos:
                #multiplicar o custo total pelo numAssentos*arestas_ate_destino
                #subtrair numAssentos de numAmigos
				soma = variavel[1]*(numAssentos)
				print('soma if: ', soma)
				self.somapreco += soma
				numAmigos = numAmigos - numAssentos

			else:
                #multiplicar o custo total pelo numAmigos*arestas_ate_destino
				soma = variavel[1]*(numAmigos)
				print('soma else: ', soma)
				self.somapreco += soma
				numAmigos = 0
		print('ue', self.somapreco)
		return int(self.somapreco)




def main():

	instancia= 1

	while True:
		try:
			entrada = input()
			entrada = entrada.split(' ')
			numCidades = int(entrada[0])
			numRotas = int(entrada[1])

			meuGrafo = Graph(numCidades)

			for i in range(numRotas):
				entradas = input()
				entradas = entradas.split(' ')
				cidade1 = int(entradas[0])
				cidade2 = int(entradas[1])
				preco = int(entradas[2])
				meuGrafo.addEdge(cidade1,cidade2, preco)

			entrada_pessoas = input()
			entrada_pessoas = entrada_pessoas.split(' ')
			numAmigos = int(entrada_pessoas[0])
			numAssentos = int(entrada_pessoas[1])
			print('Instancia', instancia)
			print(meuGrafo.precoFinal(numAmigos,numAssentos))
			print('')
			instancia+=1
		except EOFError:
			return

main()
