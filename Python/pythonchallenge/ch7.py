import re
import urllib.request
import png
import numpy
import itertools
from PIL import Image, ImageFilter

uri = "http://www.pythonchallenge.com/pc/def/%s"

url = "oxygen.html"
content = urllib.request.urlopen(uri % url).read().decode()
print(uri % url)
print("content:\n", content)
#data = re.findall("<!--(.*?)-->", content, re.DOTALL)[-1]
data = re.findall("<!--(.*?)-->", content)
print("comments: ", data)




img = Image.open('oxygen.png')
#img.show()
#First find the grey area. For grey, r = g = b
y = 0
while True:
    r, g, b, a = img.getpixel((0, y)) #x is 0, where grey is apparent
    if r == g == b:
        break
    y += 1
                    
#Each gray area is 7 pixels wide.
message = ''.join([chr(img.getpixel((x, y))[0]) for x in range(0, img.size[0], 7)])
out = re.findall('\d+', message)
print(message)
print(''.join(chr(int(i)) for i in out))


"""
r = png.Reader(filename='oxygen.png')
#png_obj = r.read()
#mapx = list(png_obj[2])
#print(mapx)
#print(mapx[0])
img = r.asDirect()
image_2d = numpy.vstack(map(numpy.uint8, img))
print(image_2d)
"""
"""
png_obj = r.read()
print(png_obj)
mapx = list(png_obj[2])
print(mapx)
print(mapx[0])
"""
