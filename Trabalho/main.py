import math
import cv2
import numpy as np

START_POINT = (191, 48, 0, 0)
END_POINT = (260, 508, 0, 0)
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
	return math.sqrt(pow(point[0] - END_POINT[0], 2) + pow(point[1] - END_POINT[1], 2)) / 100

DIST_RECT = h(START_POINT)

def AStar():
	pai = START_POINT
	global closedNodes
	closedNodes = [START_POINT]
	while not (pai[0] == END_POINT[0] and pai[1] == END_POINT[1]):
		openNodes = []
		for x in xrange(-1,2):
			for y in xrange(-1,2):
				if not(x == 0 and y == 0):
					c = 0
					new_x = pai[0] + x
					new_y = pai[1] + y
					for n in closedNodes:
						if n[0] == new_x and n[1] == new_y:
							c = c + 1;
					if c == 0:
						g_cost = g(img[new_x, new_y][0])
						h_cost = h((new_x, new_y))
						f = g_cost  + h_cost
						openNodes.append((new_x, new_y, f, g_cost))
		pai = openNodes[0]
		for n in openNodes:
			if n[2] < pai[2]:
					pai = n
		closedNodes.append(pai)

if __name__ == '__main__':
	open_image('peppersgrad.pgm')
	AStar()
	for x in closedNodes:
		draw_point((x[0], x[1]))
	cv2.imshow('image', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
