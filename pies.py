import numpy
import random
from PIL import Image, ImageDraw
image = Image.open("joga.jpg").convert("RGBA")
iA = numpy.asarray(image)
w, h = image.size
cW = int(w/2)
cH = int(h/2)
t1 = [(0,0), (cW,cH), (w,0)]
t2 = [(cW,cH), (w,h), (w,0)]
t3 = [(cW,cH), (0,h), (w,h)]
t4 = [(0,0),(cW,cH),(0,h)]
mI = Image.new('L', (iA.shape[1], iA.shape[0]), 0)
mI2 = Image.new('L', (iA.shape[1], iA.shape[0]), 0)
mI3 = Image.new('L', (iA.shape[1], iA.shape[0]), 0)
mI4 = Image.new('L', (iA.shape[1], iA.shape[0]), 0)
ImageDraw.Draw(mI).polygon(t1, 1, 1)
ImageDraw.Draw(mI2).polygon(t2, 1, 1)
ImageDraw.Draw(mI3).polygon(t3, 1, 1)
ImageDraw.Draw(mI4).polygon(t4, 1, 1)
m = numpy.array(mI)
m2 = numpy.array(mI2)
m3 = numpy.array(mI3)
m4 = numpy.array(mI4)
newIA = numpy.empty(iA.shape, 'uint8')
newIA2 = numpy.empty(iA.shape, 'uint8')
newIA3 = numpy.empty(iA.shape, 'uint8')
newIA4 = numpy.empty(iA.shape, 'uint8')
newIA[:,:,:3] = iA[:,:,:3]
newIA2[:,:,:3] = iA[:,:,:3]
newIA3[:,:,:3] = iA[:,:,:3]
newIA4[:,:,:3] = iA[:,:,:3]
newIA[:,:,3] = m* 255
newIA2[:,:,3] = m2 * 255
newIA3[:,:,3] = m3 * 255
newIA4[:,:,3] = m4 * 255
newI = Image.fromarray(newIA, "RGBA")
newI2 = Image.fromarray(newIA2, "RGBA")
newI3 = Image.fromarray(newIA3, "RGBA")
newI4 = Image.fromarray(newIA4, "RGBA")
swapAngle = 180
out = Image.new("RGBA", (w,h), 0)
choice = random.randint(1,2)
if choice == 1:
	newI = newI.rotate(swapAngle)
	newI3 = newI3.rotate(swapAngle)
	print("1 z 3")
else:
	newI2 = newI2.rotate(swapAngle)
	newI4 = newI4.rotate(swapAngle)
	print("2 z 4")
	
out.paste(newI, (0,0))
out.paste(newI2, (0,0), mask=newI2)
out.paste(newI3, (0,0), mask=newI3)
out.paste(newI4, (0,0), mask=newI4)

out.save("out.png", format="PNG")
