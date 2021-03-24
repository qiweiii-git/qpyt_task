#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy
import cv2

def gen():
   img = numpy.array([[[255, 0, 0],     [0, 255, 0],     [0, 0, 255]],
                      [[255, 255, 0],   [255, 0, 255],   [0, 255, 255]],
                      [[255, 255, 255], [128, 128, 128], [0, 0, 0]],], dtype = numpy.uint8)

   cv2.imwrite('testPattern.png', img)
