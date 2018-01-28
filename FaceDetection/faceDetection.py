import cv2
import sys

imagePath = "footballTeam.jpg"
faceCascade = cv2.CascadeClassifier("C:\\Python27\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.1, 5);
"""
i = 0
for (x, y, w, h) in faces:
    name = "i" + str(i) + ".jpg"
    crop_img = image[y:y+h, x:x+w]
    crop_img = cv2.resize(crop_img, (128, 128))
    cv2.imwrite(name, crop_img)
    i = i+1
"""
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
"""
f = open("index.html", "w")
f.write("<html><head><title>Faces</title></head><body>")
for x in range (0,i):
    f.write("<div><img src=\"i" + str(x) + ".jpg\" /></div>")
f.write("</body></html>")
f.close()
"""
cv2.imshow("Faces", image)
cv2.waitKey(0)
