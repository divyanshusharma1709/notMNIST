#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:12:39 2018

@author: divyanshu
"""

from scipy.misc import imread
import os
arrA = os.listdir("/home/divyanshu/Desktop/notMNIST_small/A/")
arrB = os.listdir("/home/divyanshu/Desktop/notMNIST_small/B/")
arrC = os.listdir("/home/divyanshu/Desktop/notMNIST_small/C/")
arrD = os.listdir("/home/divyanshu/Desktop/notMNIST_small/D/")
arrE = os.listdir("/home/divyanshu/Desktop/notMNIST_small/E/")
arrF = os.listdir("/home/divyanshu/Desktop/notMNIST_small/F/")
arrG = os.listdir("/home/divyanshu/Desktop/notMNIST_small/G/")
arrH = os.listdir("/home/divyanshu/Desktop/notMNIST_small/H/")
arrI = os.listdir("/home/divyanshu/Desktop/notMNIST_small/I/")
arrJ = os.listdir("/home/divyanshu/Desktop/notMNIST_small/J/")

imlistA = []
imlistB = []
imlistC = []
imlistD = []
imlistE = []
imlistF = []
imlistG = []
imlistH = []
imlistI = []
imlistJ = []

labelA = []
labelB = []
labelC = []
labelD = []
labelE = []
labelF = []
labelG = []
labelH = []
labelI = []
labelJ = []

imageA = []
imageB = []
imageC = []
imageD = []
imageE = []
imageF = []
imageG = []
imageH = []
imageI = []
imageJ = []
from skimage.feature import hog
from skimage import data, color, exposure
for i in range(len(arrA)):
    if(arrA[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/A/" + arrA[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistA.append(df)
for q in range(len(arrA)):
    labelA.append('A')
    
for i in range(len(arrB)):
    if(arrB[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/B/" + arrB[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistB.append(df)
for q in range(len(arrB)):
    labelB.append('B')

for i in range(len(arrC)):
    if(arrC[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/C/" + arrC[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistC.append(df)
for q in range(len(arrC)):
    labelC.append('C')
    
for i in range(len(arrD)):
    if(arrD[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/D/" + arrD[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistD.append(df)
for q in range(len(arrD)):
    labelD.append('D')
    
for i in range(len(arrE)):
    if(arrE[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/E/" + arrE[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistE.append(df)
for q in range(len(arrE)):
    labelE.append('E')

for i in range(len(arrF)):
    if(arrF[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/F/" + arrF[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistF.append(df)
for q in range(len(arrF)):
    labelF.append('F')

for i in range(len(arrG)):
    if(arrG[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/G/" + arrG[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistG.append(df)

for q in range(len(arrG)):
    labelG.append('G')

for i in range(len(arrH)):
    if(arrH[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/H/" + arrH[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistH.append(df)

for q in range(len(arrH)):
    labelH.append('H')

for i in range(len(arrI)):
    if(arrI[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/I/" + arrI[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistI.append(df)

for q in range(len(arrI)):
    labelI.append('I')

for i in range(len(arrJ)):
    if(arrJ[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/J/" + arrJ[i])
       im = color.rgb2gray(im)
       df= hog(im)
       imlistJ.append(df)
for q in range(len(arrJ)):
    labelJ.append('J')
            
features = imlistA + imlistB + imlistC + imlistD + imlistE + imlistF + imlistG + imlistH + imlistI + imlistJ
labels = labelA + labelB + labelC + labelD + labelE + labelF + labelG + labelH + labelI + labelJ
dataset = {"features": features, "labels": labels}
import pickle
pickle_out = open("dataset.pickle","wb")
pickle.dump(dataset, pickle_out)
pickle_out.close()