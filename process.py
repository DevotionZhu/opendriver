import numpy as np
import cv2
_f = cv2.imread("media/snap1.png")
h,w = _f.shape[0],_f.shape[1]
_trapez = np.array([[[w-w+100, h], [w-w+500, h-h+400], [w-500, h-h+470], [w-450, h]]])
class process:
	def _canny(self,frame):
		_g = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
		_b = cv2.GaussianBlur(_g,(5,5),1)
		_c = cv2.Canny(_b,100,150)
		return _c
	def _roi(self,frame):
		mask_ = np.zeros_like(frame)
		print(_trapez)
		cv2.fillPoly(mask_,_trapez,255)
		return cv2.bitwise_and(frame,mask_)

