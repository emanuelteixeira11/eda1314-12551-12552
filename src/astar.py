
'''
Algoritmo A* Path Finding para a 
procura de caminhos com menos custo 
em funcao da intensidade.
'''

__author__ = '12551 Pedro Santos & 12552 Emanuel Teixeira'
__date__ = '11 de Maio de 2014'

import math

class AStar():
	"""Classe AStar e responsavel pelo algoritmo da busca
	do melhor caminho com menos custo"""
	def __init__(self):
		'''
		Inicializacao dos parametros da classe Astar
		'''
		self.START_POINT = (191, 48) #x, y
		self.END_POINT = (260, 508)
		self.ALPHA = 1
		self.MAX_COR = 255.0
		self.closed_set = []
		self.count = 0
	
	def g(self, neighbor):
		'''
		Funcao com o custo g, em funcao da intesndidade da cor
		Quanto maior for a intensidade menor sera o custo

		@param neighbor e o ponto vizinho que esta a ser testado 
		@return a normalizacao da cor entre 0 e 1 do ponto neighbor
		'''
		return (1 - (self.img[neighbor[1], neighbor[0]][0] / self.MAX_COR))

	def h(self, neighbor):
		'''
		Funcao com o custo h, em funcao da distancia em linha recta ao ponto final
		Quanto maior for a distancia maior sera o custo

		@param neighbor e o ponto vizinho que esta a ser testado 
		@return a distancia em linha reta do ponto neighbor ao ponto END_POINT
		'''
		return math.sqrt((neighbor[0] - self.END_POINT[0]) ** 2 + ((self.END_POINT[1] - neighbor[1]) ** 2))

	def a_star(self, img):
		'''
		Funcao A* que busca o melhor caminho 
		utilizando a soma das funcoes g e h para um conjuto 
		de pontos e escolhendo o ponto que apresenta um custo mais baixo

		@param img e a matriz da imagem a testar com o valor dos pixeis
		'''
		self.img = img
		current = self.START_POINT
		self.closed_set = [self.START_POINT]
		while not (current[0] == self.END_POINT[0] and current[1] == self.END_POINT[1]):
			self.count = self.count + 1
			open_set = [(current[0] + x, current[1] + y) for x in xrange(-1,2) for y in xrange(-1,2)
					if (not (x == 0 and y == 0)) and ((current[0] + x, current[1] + y) not in self.closed_set)] # procura dos vizinho, se estes ainda nao estiverem na lista fechada
			if len(open_set) > 0:
				try:
					temp = [self.g(neighbor) + self.h(neighbor) / (self.ALPHA * 10) for neighbor in open_set]
					current = open_set[temp.index(min(temp))]
					self.closed_set.append(current) 
				except Exception, e:
					print 'Point out of image borders'