
import cv2
import numpy as np
import matplotlib.pyplot as plt
comet=cv2.imread("comet.jpg")
comet=cv2.resize(comet,(800,600))
s=comet.shape
new_comet=cv2.cvtColor(comet,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Binary',new_comet)
new_comet=cv2.convertScaleAbs(new_comet,alpha=1.10,beta=-20)
#cv2.imshow('Binar',new_comet)
#cv2.waitKey(0)
def Hist(image):
    H=np.zeros(shape=(256,1))
    s=image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            k=image[i,j]
            H[k,0]=H[k,0]+1
    return H
histg=Hist(new_comet)
plt.plot(histg)
x=histg.reshape(1,256)
y=np.array([])
y=np.append(y,x[0,0])
for i in range(255):
    k=x[0,i+1]+y[i]
    y=np.append(y,k)
y=np.round((y/(s[0]*s[1]))*(256-1))
for i in range(s[0]):
    for j in range(s[1]):
        k=new_comet[i,j]
        new_comet[i,j]=y[k]
equal=Hist(new_comet)
plt.plot(equal)
plt.show()
cv2.imshow('myequalize',new_comet)
cv2.waitKey(0)