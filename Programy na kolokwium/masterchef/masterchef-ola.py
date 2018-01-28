from pyx import *

c=canvas.canvas()

part1 = path.path(path.arcn(1,1,2,-90,90))
part2 = path.path(path.arcn(1,1.2,1.8,90,-90))
part3 = path.path(path.arcn(1,0.9,1.5,-90,90))
part4 = path.path(path.arcn(1,1.2,1.2,90,0))

part5 = path.path(path.arc(1.35,1.5,0.35,0,180))
part6 = path.path(path.arc(0.65,1.5,0.35,0,180))

part7 = path.line(1.7,1.5,1.7,0.8)
part8 = path.line(1.0,1.5,1.0,0.8)
part9 = path.line(0.3,1.5,0.3,0.8)

part10 = path.path(path.arcn(1.85,1.25,0.35,0,235))


c.stroke(part1,[color.rgb.red,style.linewidth.THICK])
c.stroke(part2,[color.rgb.red,style.linewidth.THICK])
c.stroke(part3,[color.rgb.red,style.linewidth.THICK])
c.stroke(part4,[color.rgb.red,style.linewidth.THICK])
c.stroke(part5,[color.rgb.red,style.linewidth.THICK])
c.stroke(part6,[color.rgb.red,style.linewidth.THICK])
c.stroke(part7,[color.rgb.red,style.linewidth.THICK])
c.stroke(part8,[color.rgb.red,style.linewidth.THICK])
c.stroke(part9,[color.rgb.red,style.linewidth.THICK])
c.stroke(part10,[color.rgb.red,style.linewidth.THICK])

c.writePDFfile()


