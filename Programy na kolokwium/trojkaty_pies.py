import numpy
import random
from PIL import Image, ImageDraw

# read image as RGB and add alpha (transparency)
im = Image.open("image2.png").convert("RGBA")

# convert to numpy (for convenience)
imArray = numpy.asarray(im)

# maska wielokata (tu trojkaty)
w, h = im.size
centerW = int(w/2)
centerH = int(h/2)

triangle1 = [(0,0), (centerW,centerH), (w,0)]
triangle2 = [(centerW,centerH), (w,h), (w,0)]
triangle3 = [(centerW,centerH), (0,h), (w,h)]
triangle4 = [(0,0),(centerW,centerH),(0,h)]

maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
maskIm2 = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
maskIm3 = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
maskIm4 = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)

ImageDraw.Draw(maskIm).polygon(triangle1, outline=1, fill=1)
ImageDraw.Draw(maskIm2).polygon(triangle2, outline=1, fill=1)
ImageDraw.Draw(maskIm3).polygon(triangle3, outline=1, fill=1)
ImageDraw.Draw(maskIm4).polygon(triangle4, outline=1, fill=1)

mask = numpy.array(maskIm)
mask2 = numpy.array(maskIm2)
mask3 = numpy.array(maskIm3)
mask4 = numpy.array(maskIm4)

# assemble new image (uint8: 0-255)
newImArray = numpy.empty(imArray.shape, dtype='uint8')
newImArray2 = numpy.empty(imArray.shape, dtype='uint8')
newImArray3 = numpy.empty(imArray.shape, dtype='uint8')
newImArray4 = numpy.empty(imArray.shape, dtype='uint8')

# colors (three first columns, RGB)
newImArray[:,:,:3] = imArray[:,:,:3]
newImArray2[:,:,:3] = imArray[:,:,:3]
newImArray3[:,:,:3] = imArray[:,:,:3]
newImArray4[:,:,:3] = imArray[:,:,:3]

# transparency (4th column)
newImArray[:,:,3] = mask * 255
newImArray2[:,:,3] = mask2 * 255
newImArray3[:,:,3] = mask3 * 255
newImArray4[:,:,3] = mask4 * 255

# back to Image from numpy
newIm = Image.fromarray(newImArray, "RGBA")
newIm2 = Image.fromarray(newImArray2, "RGBA")
newIm3 = Image.fromarray(newImArray3, "RGBA")
newIm4 = Image.fromarray(newImArray4, "RGBA")

#LOSOWANIE CZY 1 Z 3 CZY 2 Z 4 - mamy trojkaty i obracamy zeby sie wpasowaly
swapAngle = 180
imFinal = Image.new("RGBA", (w,h), 0)
choice = random.randint(1,2)
if choice == 1:	#i z 3
	newIm = newIm.rotate(swapAngle)
	newIm3 = newIm3.rotate(swapAngle)
	print("zamiana 1 z 3")
else:	#2 z 4
	newIm2 = newIm2.rotate(swapAngle)
	newIm4 = newIm4.rotate(swapAngle)
	print("zamiana 2 z 4")
	
imFinal.paste(newIm, (0,0))
imFinal.paste(newIm2, (0,0), mask=newIm2)
imFinal.paste(newIm3, (0,0), mask=newIm3)
imFinal.paste(newIm4, (0,0), mask=newIm4)

imFinal.save("final.png", format="png")