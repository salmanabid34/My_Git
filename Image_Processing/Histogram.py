import cv2
import numpy as np
import matplotlib.pyplot as plt
comet=cv2.imread("comet.jpg")
comet=cv2.resize(comet,(800,600))
new_comet=cv2.cvtColor(comet,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Binary',new_comet)
new_comet=cv2.convertScaleAbs(new_comet,alpha=-5,beta=5)
#cv2.imshow('Binar',new_comet)
#cv2.waitKey(0)
H=np.zeros(shape=(256,1))
s=comet.shape
for i in range(s[0]):
    for j in range(s[1]):
        k=new_comet[i,j]
        H[k,0]=H[k,0]+1
plt.plot(H)
plt.show()
        

