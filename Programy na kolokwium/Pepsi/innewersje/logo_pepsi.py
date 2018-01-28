from pyx import *

c = canvas.canvas()

c.stroke(path.curve(-3, 0,-3, 5, -3, 10, -3, 15),[style.linewidth.THICK, color.rgb.red])
c.stroke(path.curve(-3, 0, 2, 0, 4, 0, 5, 0),[style.linewidth.THICK, color.rgb.red])
c.stroke(path.curve(-3, 15,2, 15, 4, 15, 5, 15),[style.linewidth.THICK, color.rgb.red])


r=7.5
r1=6.5
kolo1 = path.arc(8,7.5,r,0,360)
kolo2 = path.arc(8,7.5,r1,-150,-30)
kolo3 = path.arc(8,7.5,r1,30,150)

y=10.7
c.stroke(path.curve(2.3, y,4, y-0.8, 6, y-0.8, 8, y),[style.linewidth.THICK, color.rgb.red])
c.stroke(path.curve(8, y,10, y+0.8, 12, y+0.8, 13.7, y),[style.linewidth.THICK, color.rgb.red])
y2=4.3
c.stroke(path.curve(2.4, y2,4, y2-0.8, 6, y2-0.8, 8, y2),[style.linewidth.THICK, color.rgb.blue])
c.stroke(path.curve(8, y2,10, y2+0.8, 12, y2+0.8, 13.7, y2),[style.linewidth.THICK, color.rgb.blue])

unit.set(xscale=13)

t = c.text(2.7, 6.3, "Pepsi")

kolo1 = path.arc(8,7.5,7.5,0,360)
c.stroke(path.curve(19, 0,19, 5, 19, 10, 19, 15),[style.linewidth.THICK, color.rgb.blue])
c.stroke(path.curve(11, 0,11, 0, 15, 0, 19, 0),[style.linewidth.THICK, color.rgb.blue])
c.stroke(path.curve(11, 15,11, 15, 15, 15, 19, 15),[style.linewidth.THICK, color.rgb.blue])
styl1 = [style.linewidth(0.6), style.linecap.round, color.rgb.red]
styl2 = [style.linewidth(0.3), style.linecap.round, color.rgb.red]
styl3 = [style.linewidth(0.3), style.linecap.round, color.rgb.blue]
c.stroke(path.path(kolo1), styl1)
c.stroke(path.path(kolo2),styl3)
c.stroke(path.path(kolo3),styl2)
c.writePDFfile("pepsi")
