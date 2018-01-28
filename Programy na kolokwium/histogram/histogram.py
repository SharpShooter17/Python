from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

n = 8
path = 'a.png'

im = Image.open(path)

lista = im.histogram()

redStart = 0
blueStart = 256
greenStart = 512

yRed = []
yBlue = []
yGreen = []
start = 0
end = 0
bar_width = 0.3
index = np.arange(n)

div = 256//n

x = []

for i in range(n):
    end = end + div
    yRed.append(sum(lista[redStart+start:redStart+end]))
    yBlue.append(sum(lista[blueStart+start:blueStart+end]))
    yGreen.append(sum(lista[greenStart+start:greenStart+end]))
    x.append(str(start) + '-' + str(end))
    start = start + div
print (x)



plt.bar(index-bar_width,yRed,bar_width,color='r',label="Red")
plt.bar(index,yBlue,bar_width,color='b', label="Blue")
plt.bar(index+bar_width,yGreen,bar_width,color='g', label="Green")

#plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
plt.legend()
plt.xlabel('Pixels')
plt.ylabel('Group')

plt.title('Wykres')
plt.xticks(index, x)

plt.show()
    



