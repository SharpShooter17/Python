import numpy
from PIL import Image, ImageDraw
def cropImg(im, polygon):
    # convert to numpy (for convenience)
    imArray = numpy.asarray(im)

    # create mask70
    maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
    ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
    mask = numpy.array(maskIm)

    # assemble new image (uint8: 0-255)
    newImArray = numpy.empty(imArray.shape, dtype='uint8')

    # colors (three first columns, RGB)
    newImArray[:, :, :3] = imArray[:, :, :3]

    # transparency (4th column)
    newImArray[:, :, 3] = mask * 255
    return Image.fromarray(newImArray, "RGBA")




im = Image.open("pies.jpg").convert("RGBA")
width, height = im.size
right = cropImg (im, ([(width/2, height/2), (width, 0), (width, width)]))
down = cropImg (im, ([(width/2, height/2), (0,width), (width, width)]))
up = cropImg (im, ([(width/2, height/2), (0,0), (width, 0)]))
left = cropImg (im, ([(width/2, height/2), (0,0), (0,width)]))

down1 = down.transpose(Image.FLIP_TOP_BOTTOM)
down1.save("out.png")
