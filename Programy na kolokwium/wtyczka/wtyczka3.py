from pyx import *

c = canvas.canvas()

#wtyczka

circ1 = path.circle(0, 0, 3)
c.fill(circ1, [color.rgb.black])

rect1 = path.rect(-3,0,6,3)
c.fill(rect1, [color.rgb.black])

rect2 = path.rect(-2,0,0.5,6)
c.fill(rect2, [color.rgb.black])

rect3 = path.rect(1.5,0,0.5,6)
c.fill(rect3, [color.rgb.black])

circ2 = path.circle(0, -3, 1)
c.fill(circ2, [color.rgb.black])

rect4 = path.rect(-0.28,-3,0.5,-3)
c.fill(rect4, [color.rgb.black])


c.stroke(circ1,[style.linewidth(0.65), color.rgb.black])
c.stroke(rect1,[style.linewidth(0.65), color.rgb.black])
c.stroke(rect2,[style.linewidth(0.65), color.rgb.black])
c.stroke(rect3,[style.linewidth(0.65), color.rgb.black])
c.stroke(circ2,[style.linewidth(0.65), color.rgb.black])
c.stroke(rect4,[style.linewidth(0.65), color.rgb.black])
#koniec wtyczka


#E
duzeE = path.path(path.arcn(0,0,2,270,360))
duzeEfala1 = path.curve(-0.7,-0.2,-0.3,0.3,0.1,0.3,0.5,-0.21)
duzeEfala2 = path.curve(0.5,-0.2,0.9,-0.7,1.3,-0.7,1.6,-0.2)

c.stroke(duzeE,[style.linewidth(0.65), color.cmyk.Blue])
c.stroke(duzeEfala1,[style.linewidth(0.35), color.cmyk.Orange])
c.stroke(duzeEfala2,[style.linewidth(0.35), color.cmyk.Orange])

# koniec E

c.writePDFfile("wtyczka")
