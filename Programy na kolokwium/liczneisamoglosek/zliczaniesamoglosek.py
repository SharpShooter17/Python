# -*- coding: utf-8 -*-
# Zczytać plik tekstowy i policzyć w nim poszczególne samogłoski,
# następnie zrobić wykres kołowy z ilością ich wystąpień

import re
import matplotlib.pyplot as plt



text = open("lorem.txt", "rt").read()
text = re.sub("[^A-Za-z]"," ",text)
text = text.lower()
allWords = text.split()
dlugosc = len(allWords)
litA=0
litE=0
litI=0
litO=0
litU=0
litY=0

for x in range(dlugosc):
    q=list(allWords[x])
    dl=len(q)
    for y in range(dl):
        if "a" in q[y]:
            litA=litA+1
x=0
for x in range(dlugosc):
    q=list(allWords[x])
    dl=len(q)
    for y in range(dl):
        if "e" in q[y]:
            litE=litE+1

x=0
for x in range(dlugosc):
    q=list(allWords[x])
    dl=len(q)
    for y in range(dl):
        if "i" in q[y]:
            litI=litI+1
x=0
for x in range(dlugosc):
    q=list(allWords[x])
    dl=len(q)
    for y in range(dl):
        if "o" in q[y]:
            litO=litO+1

x=0
for x in range(dlugosc):
    q=list(allWords[x])
    dl=len(q)
    for y in range(dl):
        if "u" in q[y]:
            litU=litU+1
x=0
for x in range(dlugosc):
    q=list(allWords[x])
    dl=len(q)
    for y in range(dl):
        if "y" in q[y]:
            litY=litY+1





labels = 'a', 'e', 'i', 'o' , 'u', 'y'
sizes = [litA, litE, litI, litO, litU, litY]
explode = (0, 0, 0, 0, 0, 0) 

def make_autopct(sizes):
    def my_autopct(pct):
        total = sum(sizes)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(p=pct,v=val)
    return my_autopct

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct=make_autopct(sizes),
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.legend(title="samogloski")
plt.show()

print (litA, litE, litI, litO, litU, litY)


