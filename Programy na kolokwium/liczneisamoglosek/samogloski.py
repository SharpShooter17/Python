import matplotlib.pyplot as plt

myFile=open("a.txt",'r')

aCount=0
eCount=0
iCount=0
oCount=0
uCount=0
yCount=0

for line in myFile:
    for word in line.split():
        current=word.lower()
        aCount=aCount+current.count('a')
        eCount=eCount+current.count('e')
        iCount=iCount+current.count('i')
        oCount=oCount+current.count('o')
        uCount=uCount+current.count('u')
        yCount=yCount+current.count('y')


print(aCount)
print(eCount)
###
# Data to plot
labels = 'Letter A', 'Letter E', 'Letter I', 'Letter O'
sizes = [aCount, eCount, iCount, oCount]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

