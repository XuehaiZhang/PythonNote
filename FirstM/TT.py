#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'bpmacmini01'

from PIL import Image
im = Image.open('/Users/bpmacmini01/Desktop/100.jpeg')
print(im.format, im.size, im.mode)
im.thumbnail((50, 50))
im.save('x.jpg', 'JPEG')