from pyx import *


c = canvas.canvas()
c.fill(path.rect(-1,-1,2,2),[style.linewidth.THICK, color.rgb.red])
c.fill(path.rect(1,-1,2,2),[style.linewidth.THICK, color.rgb.blue])
c.fill(path.circle(1,0,1.1), [color.cmyk.White])

x=0.2
y=0.2
deltax=0.2666666667
luk1 = path.arc(0,y,0.8,0,180)
c.stroke(path.path(luk1),[color.rgb.red])
falaRed = path.curve(x,y,x+deltax,y+0.1, x+2*deltax, y+0.1, x+3*deltax, y)
x=x+3*deltax
falaRed2 = path.curve(x,y,x+deltax,y-0.1, x+2*deltax, y-0.1, x+3*deltax, y)

gorne = path.path(luk1) + falaRed + falaRed2
c.fill(gorne,[color.rgb.red])
c.fill(gorne,[trafo.rotate(180,1,0),color.rgb.blue])

# P
P1 = path.curve(0.25,-0.15,0.25,0.2,0.25,0.2,0.25,0.2)
P2 = path.curve(0.25,0.18,0.6,0.1,0.6,0.05,0.25,0)

c.stroke(P1,[style.linewidth(0.05), color.rgb.blue])
c.stroke(P2,[style.linewidth(0.05), color.rgb.blue])

# E
E1 = path.curve(0.6,-0.10,0.6,0.2,0.6,0.2,0.6,0.2)
E2 = path.curve(0.575,-0.10,0.8,-0.10,0.8,-0.10,0.8,-0.10)
E3 = path.curve(0.575,0.05,0.8,0.05,0.8,0.05,0.8,0.05)
E4 = path.curve(0.575,0.18,0.8,0.18,0.8,0.18,0.8,0.18)

c.stroke(E1,[style.linewidth(0.05), color.rgb.blue])
c.stroke(E2,[style.linewidth(0.05), color.rgb.blue])
c.stroke(E3,[style.linewidth(0.05), color.rgb.blue])
c.stroke(E4,[style.linewidth(0.05), color.rgb.blue])
# P

P21 = path.curve(0.9,-0.15,0.9,0.2,0.9,0.2,0.9,0.2)
P22 = path.curve(0.9,0.18,1.25,0.1,1.25,0.05,0.9,0)

c.stroke(P21,[style.linewidth(0.05), color.rgb.blue])
c.stroke(P22,[style.linewidth(0.05), color.rgb.blue])
# S
S1 = path.curve(1.2,-0.2,1.6,-0.2,1.6,-0.08,1.3,-0.08)
S2 = path.curve(1.3,-0.08,1.2,-0.08,1.3,0.1,1.55,0.1)

c.stroke(S1,[style.linewidth(0.05), color.rgb.blue])
c.stroke(S2,[style.linewidth(0.05), color.rgb.blue])
# I
I1 = path.curve(1.75,-0.18,1.75,0.18,1.75,0.18,1.75,0.18)

c.stroke(I1,[style.linewidth(0.05), color.rgb.blue])

c.writePDFfile()
