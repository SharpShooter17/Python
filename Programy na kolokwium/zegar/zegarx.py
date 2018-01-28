from PIL import Image, ImageDraw
from random import shuffle
from datetime import datetime
from math import sin, cos, radians
from pyx import *

img = Image.open('zegar.jpg')

a= datetime.now().strftime('%H:%M:%S')

godziny=a[0]+a[1]
minuty=a[3]+a[4]
sekundy=a[6]+a[7]
sekundy=float(sekundy)
minuty=float(minuty)
godziny=float(godziny)
#minuty=minuty+10



mid=150

dlugax=110
dlugay=65


kat1=360*((minuty+90)/60)


if godziny>=12:
    godziny=godziny-12
kat2=360*((godziny-3.3)/12)
kat1=360-kat1
kat2=360-kat2
kat2=kat2+60

katminuty1=int(dlugax*sin(radians(kat1))+mid)
katminuty2=int(dlugax*cos(radians(kat1))+mid)

katminuty3=int(dlugay*sin(radians(kat2))+mid)
katminuty4=int(dlugay*cos(radians(kat2))+mid)


draw = ImageDraw.Draw(img) 
draw.line((150,150, katminuty1,katminuty2), fill=128,width=5)
draw.line((150,150, katminuty3,katminuty4), fill=128,width=8)



img.save('zegar.png','PNG')
