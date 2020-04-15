import matplotlib.pyplot as plt
import cv2
import numpy as np
from car import car
_car = car()
def show_mat():
	img = cv2.imread("media/snap1.png")
	plt.imshow(img)
	plt.show()
if __name__ == "__main__":
	show_mat()
