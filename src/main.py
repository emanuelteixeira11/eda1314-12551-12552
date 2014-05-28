
'''
Algoritmo A* Path Finding para a 
procura de caminhos com menos custo 
em funcao da intensidade.
'''

import math
import cv2
import numpy as np
from astar import AStar
import time

__author__ = '12551 Pedro Santos & 12552 Emanuel Teixeira'
__date__ = '11 de Maior de 2014'

class OpenImage(object):
	"""Classe onde a imagem vai ser
	aberta para estudo e tratamento"""
	def __init__(self, name):
		'''
		Inicializacao de parametros da classe

		@name nome do ficheiro da imagem a abrir
		'''
		super(OpenImage, self).__init__()
		self.name = name
		self.img = None
		self.width = 0
		self.height = 0

	def open_image(self, START_POINT, END_POINT, flag = True):
		'''
		Abertura e desenho na imagem dos pontos inicial e final
		para percepcao clara do caso de estudo

		@param START_POINT ponto incial
		@param END_POINT ponto final
		'''
		start = time.clock()
		self.img = cv2.imread(self.name)
		self.width, self.height = self.img.shape[:2]
		self.time = time.clock() - start
		if flag:
			cv2.line(self.img,(START_POINT[0], START_POINT[1]),(START_POINT[0], START_POINT[1]),(0,0,255),8)
			cv2.line(self.img,(END_POINT[0], END_POINT[1]),(END_POINT[0], END_POINT[1]),(0,0,255),8)

	def show_image(self):
		'''
		Abertura de uma caixa de dialogo com 
		o resultado do algoritmo visivel
		'''
		cv2.imshow('A* - EDA 13/14', self.img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def save_image(self, name):
		'''
		Guarda o conteudo da janela num ficheiro
		de imagem

		@param name nome do ficheiro de imagem a gravar
		'''
		cv2.imwrite(name, self.img)

	def draw_point(self, point):
		'''
		Funcao que desenha um ponto na imagem

		@param point ponto a desenhar na imagem
		'''
		cv2.line(self.img, point, point,(0,255,255), 2)

class WriteFile(object):
	'''
	Classe para a escrita de ficheiros
	'''
	def write_file(self, name, closed_set):
		'''
		Escrita de um ficheiro .txt para o armazenamento dos
		pontos resultantes do algoritmo

		@param name nome do ficheiro .txt onde serao armazenados os dados
		@closed_set lista de pontos resultantes do algoritmo
		'''
		data = open(name, 'w')
		for x in closed_set:
			data.writelines((str(x[0]), ' , ', str(x[1]), '\n'))
		data.close()
		

if __name__ == '__main__':
	open_image = OpenImage('peppersgrad.pgm')
	a_star = AStar()
	open_image.open_image(a_star.START_POINT, a_star.END_POINT)
	start = time.time()
	a_star.a_star(open_image.img)
	finish = time.time() - start
	for point in a_star.closed_set:
		open_image.draw_point(point)
	print 'Tempo de execucao: %.15f' % finish
	print 'Iteracoes:', a_star.count
	print 'Media por cada iteracao: %.15f' % (finish / a_star.count)
	open_image.show_image()
	open_image.save_image('result.png')
	write_file = WriteFile()
	write_file.write_file('data.txt', a_star.closed_set)
			