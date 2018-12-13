#-*-coding:utf-8-*- 
__author__ = 'Chennull'

import pytesseract
from PIL import Image

class GetImageDate(object):
    def m(self):
        image = Image.open(u"img/bmp/1.bmp")
        text = pytesseract.image_to_string(image)
        return text

    def SaveResultToDocument(self):
        text = self.m()
        f = open(u"Verification.txt","w")
        print(text)
        f.write(str(text))
        f.close()

g = GetImageDate()
g.SaveResultToDocument()