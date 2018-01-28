import PIL
from PIL import Image
im = Image.open("audi.jpg")
print im.format, im.size, im.mode

"""PRZY DOWOLNYM MIESZANIU ODKOMENTUJ PONIZSZE"""
"""list_of_regions = [[0 for x in range(0,3)] for y in range(0,3)]
list_of_boxes = [[0 for x in range(0,3)] for y in range(0,3)]
for x in range(0,3):
    for y in range(0,3):
        box = (x+(360*x), y+(360*y), x+(360*(x+1)), y+(360*(y+1)))
        region = im.crop(box)
        list_of_regions[x][y] = region
        list_of_boxes[x][y] = box"""

""" MIESZANIE """
"""temp = list_of_regions[0][0]
list_of_regions[0][0] = list_of_regions[0][2]
list_of_regions[0][2] = temp
temp = list_of_regions[1][1]
list_of_regions[1][1] = list_of_regions[1][2]
list_of_regions[1][2] = temp
temp = list_of_regions[2][0]
list_of_regions[2][0] = list_of_regions[2][1]
list_of_regions[2][1] = temp"""

"""MIESZANIE Z DESATURYZACJA """
"""temp = list_of_regions[0][0].convert('LA')
list_of_regions[0][0] = list_of_regions[0][2].convert('LA')
list_of_regions[0][2] = temp
temp = list_of_regions[1][1]
list_of_regions[1][1] = list_of_regions[1][2].convert('LA')
list_of_regions[1][2] = temp
temp = list_of_regions[2][0]
list_of_regions[2][0] = list_of_regions[2][1].convert('LA')
list_of_regions[2][1] = temp
list_of_regions[2][2] = list_of_regions[2][2].convert('LA')"""

"""PRZY DOWOLNYM MIESZANIU ODKOMENTUJ PONIZSZE"""
"""for x in range(0,3):
    for y in range(0,3):
        im.paste(list_of_regions[x][y], list_of_boxes[x][y])
im.show()"""
  
""" OBRACANIE """
for x in range(0,3):
    for y in range(0,3):
        box = (x+(360*x), y+(360*y), x+(360*(x+1)), y+(360*(y+1)))
        region = im.crop(box)
        region = region.transpose(Image.ROTATE_90)
        im.paste(region, box)
im.show()  
    
