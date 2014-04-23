import math
import cv2
import numpy as np
import time

START_POINT = (191, 48) #x, y
END_POINT = (260, 508)
MAX_COR = 255.0

def write_file(name, lista):
	data = open(name, 'w')
	for x in lista:
		data.writelines((str(x[0]), ' , ', str(x[1]), '\n'))
	data.close()

def draw_point(point):
	cv2.line(img,point,(point),(0,255,255),2)

def open_image(name):
	global img
	img = cv2.imread(name)
	print img[260, 508]
	cv2.line(img,(START_POINT[0],START_POINT[1]),(START_POINT[0],START_POINT[1]),(0,0,255),8)
	cv2.line(img,(END_POINT[0],END_POINT[1]),(END_POINT[0],END_POINT[1]),(0,0,255),8)

def g(n):
	return 1 - (img[n[1], n[0]][0] / MAX_COR)

def h(n, pai):
	MEDIUM_POINT = END_POINT
	if multiple_goals[0] != END_POINT:
		if (n[0] >= multiple_goals[0][0] or n[1] >= multiple_goals[0][1]):
			multiple_goals.pop(0)
	return math.sqrt((n[0] - multiple_goals[0][0]) ** 2 + ((multiple_goals[0][1] - n[1]) ** 2))
	#return math.sqrt((n[0] - MEDIUM_POINT[0]) ** 2 + ((MEDIUM_POINT[1] - n[1]) ** 2))

def a_star():
	pai = START_POINT
	closed_nodes = [START_POINT]
	while not (pai[0] == END_POINT[0] and pai[1] == END_POINT[1]):
		open_nodes = [(pai[0] + x, pai[1] + y) for x in xrange(-1,2) for y in xrange(-1,2)
				if (not (x == 0 and y == 0)) and ((pai[0] + x, pai[1] + y) not in closed_nodes)]
		if len(open_nodes) > 0:
			temp = []
			for n in open_nodes: 
				temp.append(g(n) + h(n, pai))
			pai = open_nodes[temp.index(min(temp))]
			closed_nodes.append(pai)
	return closed_nodes

def points():
	l = [START_POINT]
	m = ((END_POINT[1] - START_POINT[1]) / (END_POINT[0] - START_POINT[0]))
	b = START_POINT[1] - m * START_POINT[0]
	for x in xrange(START_POINT[0], END_POINT[0]):
		y = m * x + b
		if x % 3 == 0 and (x, y) not in l:
			l.append((x, y))
	if END_POINT not in l:
		l.append(END_POINT)
	return l

if __name__ == '__main__':
	open_image('peppersgrad.pgm')
	global multiple_goals
	multiple_goals = points()
	for x in multiple_goals:
		draw_point(x)
	res = a_star()
	for x in res:
		draw_point(x)
	write_file('data.txt', res)
	cv2.imshow('Trabalho de EDA', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()