import math
import cv2
import numpy as np

START_POINT = (191, 48, 0) #x, y
END_POINT = (260, 508, 0)
MAX_COR = 255.0

def draw_point(point):
	cv2.line(img,point,(point),(0,255,255),2)

def open_image(name):
	global img, width, height
	img = cv2.imread(name)
	width, height, h = img.shape
	cv2.line(img,(START_POINT[0],START_POINT[1]),(START_POINT[0],START_POINT[1]),(0,0,255),8)
	cv2.line(img,(END_POINT[0],END_POINT[1]),(END_POINT[0],END_POINT[1]),(0,0,255),8)
	#cv2.imshow('image', img)

def g(pixel):
	return (1.0 - pixel / 255.0)

def h(point):
	return math.sqrt(pow(point[0] - END_POINT[0], 2) + pow(point[1] - END_POINT[1], 2))

DIST_RECT = h(START_POINT)

def a_star():
	pai = START_POINT
	global closed_nodes
	closed_nodes = [START_POINT]
	while not (pai[0] == END_POINT[0] and pai[1] == END_POINT[1]):
		open_nodes = [(pai[0] + x, pai[1] + y) for x in xrange(-1,2) for y in xrange(-1,2)
			if not (x == 0 and y == 0)]
		f_pai = g(img[open_nodes[0][0], open_nodes[0][1]][0]) + h(open_nodes[0]) / DIST_RECT
		for x in open_nodes:
			if closed_nodes.count(x) == 0:
				f = g(img[x[0], x[1]][0]) + h(x)
				if f_pai >= f:
					pai = x
		closed_nodes.append(pai)


if __name__ == '__main__':
	open_image('peppersgrad.pgm')
	a_star()
	for x in closed_nodes:
		draw_point((x[0], x[1]))
	cv2.imshow('image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()