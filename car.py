import matplotlib.pyplot as plt
from pygame.locals import *
from process import process
import numpy as np
import cv2
import pygame
import sys
_proc = process()
vid = "media/car1.mp4"
pic = "media/snap1.png"

class car:
	def vid(self):
		pygame.init()
		pygame.display.set_caption("result")
		screen = pygame.display.set_mode([1280,720])
		
		cap = cv2.VideoCapture(vid)
		while cap.isOpened():
			ret,frame = cap.read()
			frame = _proc._canny(frame)
			crop= _proc._roi(frame)
			frame = cv2.addWeighted(frame,0.9,crop,1,1)
			#frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
			frame = frame.swapaxes(0,1)
			frame = pygame.surfarray.make_surface(frame)
			screen.blit(frame,(20,20))
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					sys.exit(1)

