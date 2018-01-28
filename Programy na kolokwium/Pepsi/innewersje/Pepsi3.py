from pyx import *
from PIL import ImageDraw

c = canvas.canvas()
c.stroke(path.rect(0,0,0.8,1),[deco.filled([color.rgb.red])])
c.stroke(path.rect(0,0,0.8,1),[style.linewidth(0.03), color.gray.white])
c.stroke(path.rect(0.8,0,0.8,1),[deco.filled([color.rgb.blue])])
c.stroke(path.rect(0.8,0,0.8,1),[style.linewidth(0.03), color.gray.white])
c.stroke(path.circle(0.8,0.5,0.5),[deco.filled([color.gray.white])])

red = path.path(path.moveto(0.8,0.5), path.arc(0.8,0.5,0.5,0,180), path.closepath())
blue = path.path(path.moveto(0.8,0.5), path.arc(0.8,0.5,0.5,180,0), path.closepath())

c.stroke(red, [deco.filled([color.rgb.red])])
c.stroke(blue, [deco.filled([color.rgb.blue])])
c.stroke(path.circle(0.8,0.5,0.5),[style.linewidth(0.03), color.gray.white])

#c.stroke(path.rect(0.5,0.5,0.3,0.3), [deco.filled([color.gray.white])])







c.writePDFfile()