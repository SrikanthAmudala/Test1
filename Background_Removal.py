'''
@author: Srikanth Amudala
Desc: Separates the background image from the text
'''

import numpy as np
import cv2
import pywt
import math
from scipy import misc

class DWT():

    def w2d(self, img, mode='haar'):
        try:
            i = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
            (h, w) = i.shape
            input_image = i.copy()

        except Exception as e:
            print(e)


