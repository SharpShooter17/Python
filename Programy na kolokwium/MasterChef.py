from pyx import *
c=canvas.canvas()

# luki numeruje rosnaco kazdy kolejny ma mniejszy promien

luk1 =  path.path(path.arcn(0,0,3.5,270,90))
luk2 =  path.path(path.arc(0,0.5,3,270,90))
luk3 =  path.path(path.arcn(0,0,2.5,270,90))
luk4 =  path.path(path.arc(0,0.5,2,0,90))

M1 =  path.curve(-1.75,0.5,-1.75,1.5,-0.25,1.5,-0.25,0.5)
M2 =  path.curve(-0.25,0.5,-0.25,1.5,1.25,1.5,1.25,0.5)

M3 =  path.curve(-1.75,0.5,-1.75,-0.5,-1.75,-0.5,-1.75,-0.5)
M4 =  path.curve(-0.25,0.5,-0.25,-0.5,-0.25,-0.5,-0.25,-0.5)
M5 =  path.curve(1.25,0.5,1.25,-0.5,1.25,-0.5,1.25,-0.5)

laczenie = path.curve(1.25,-0.5,1.5,-0.5,2,-0.5,2,0.5)

c.stroke(luk1,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])
c.stroke(luk2,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])
c.stroke(luk3,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])
c.stroke(luk4,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])

c.stroke(M1,[style.linewidth(0.35), color.cmyk.Red])
c.stroke(M2,[style.linewidth(0.35), color.cmyk.Red])
c.stroke(M3,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])
c.stroke(M4,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])
c.stroke(M5,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])

c.stroke(laczenie,[style.linewidth(0.35), color.cmyk.Red , style.linecap.round])

c.writePDFfile("MCLogo")
