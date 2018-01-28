from pyx import *
from math import *

r=4.0
x=8.0
d=x
beta=270-180/pi*acos(r/d)
c=canvas.canvas()
c.stroke(path.rect(0,2,1,6),[deco.filled([color.rgb(0,0,0)])])
c.stroke(path.rect(10,2,1,6),[deco.filled([color.rgb(0,0,0)])])
c.stroke(path.rect(-2,2.1,15,-8),[deco.filled([color.rgb(0,0,0)])])
c.stroke(path.circle(5.5, -5.4, 7.5),[deco.filled([color.rgb(0,0,0)])])
c.stroke(path.circle(5.5, -12.5, 2),[deco.filled([color.rgb(0,0,0)])])
c.stroke(path.rect(4.55,-12.5,2,-4),[deco.filled([color.rgb(0,0,0)])])

l=1.5
k=-5.2
j=6

c.stroke(path.path(path.arc(5.5,-5,6,0,270)),[color.rgb.blue, style.linewidth(1.2)])
c.stroke(path.curve(l,k,l+1.5*1,k+2*1,l+1.5*2,k+2*1,l+1.5*3,k),[color.rgb(1,0.4,0), style.linewidth(1.2)])
c.stroke(path.curve(j,k,j+1.5*1,k-2*1,j+1.5*2,k-2*1,j+1.5*3,k),[color.rgb(1,0.4,0), style.linewidth(1.2)])
c.writePDFfile("wtyczka.pdf")
