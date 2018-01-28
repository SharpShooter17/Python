from pyx import *

c = canvas.canvas()


lineWidth1 = 0.1
lineWidth2 = 0.05

r = 0.8
kolo11 = path.arc(0,2,r,0,360)
#kolo12 = path.arc(0,2,r,180,360)
styl1 = [style.linewidth(lineWidth1), style.linecap.round, color.cmyk.Black,deco.filled([color.rgb.red])]
c.stroke(path.path(kolo11), styl1)
c.stroke(path.curve(0,-1.5, -7,-0.5, 0.5,1, -2.5,2.5), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.curve(0,-1.5, 7,-0.5, -0.5,1, 2.5,2.5), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])

c.stroke(path.curve(-2.5,2.5, -3,3.5, -2,4, -0.6,4), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.curve(2.5,2.5, 3,3.5, 2,4, 0.6,4), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])

c.stroke(path.path(path.moveto(-1, 0), path.lineto(1, 0)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])

c.stroke(path.path(path.moveto(-0.4, 0), path.lineto(-0.4, 9)), [style.linewidth(lineWidth2),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(0, 0), path.lineto(0, 9)), [style.linewidth(lineWidth2),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(0.4, 0), path.lineto(0.4, 9)), [style.linewidth(lineWidth2),style.linecap.round, color.rgb.black])

c.stroke(path.path(path.moveto(-0.6, 3), path.lineto(0.6, 3)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(-0.6, 3), path.lineto(-0.6, 8.5)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(0.6, 3), path.lineto(0.6, 8.5)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(0.6, 8.5), path.lineto(0.8, 10)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(-0.6, 8.5), path.lineto(-0.8, 10)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(-0.8, 10), path.lineto(0.8, 10)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])

c.stroke(path.path(path.moveto(-0.3, 9), path.lineto(-0.5, 9.7)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])
c.stroke(path.path(path.moveto(0.3, 9), path.lineto(0.5, 9.7)), [style.linewidth(lineWidth1),style.linecap.round, color.rgb.black])



#c.stroke(path.path(kolo12), styl1)

c.writePDFfile("gitara.pdf")
