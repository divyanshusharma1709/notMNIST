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

featuresA = []
labelA = []
featuresB = []
labelB = []
featuresC = []
labelC = []
featuresD = []
labelD = []
featuresE = []
labelE = []
featuresF = []
labelF = []
featuresG = []
labelG = []
featuresH = []
labelH = []
featuresI = []
labelI = []
featuresJ = []
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
for i in range(len(arrA)):
    if(arrA[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/A/" + arrA[i])
       imlistA.append(im)
    for x in range(28):
        for y in range(28):
            imageA.append(imlistA[i][x][y])
    featuresA.append(imageA)
for q in range(len(arrA)):
    labelA.append('A')
    
for i in range(len(arrB)):
    if(arrB[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/B/" + arrB[i])
       imlistB.append(im)
    for x in range(28):
        for y in range(28):
            imageB.append(imlistB[i][x][y])
    featuresB.append(imageB)
for q in range(len(arrB)):
    labelB.append('B')

for i in range(len(arrC)):
    if(arrC[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/C/" + arrC[i])
       imlistC.append(im)
    for x in range(28):
        for y in range(28):
            imageC.append(imlistB[i][x][y])
    featuresC.append(imageC)
for q in range(len(arrC)):
    labelC.append('C')
    
for i in range(len(arrD)):
    if(arrD[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/D/" + arrD[i])
       imlistD.append(im)
    for x in range(28):
        for y in range(28):
            imageD.append(imlistD[i][x][y])
    featuresD.append(imageD)
for q in range(len(arrD)):
    labelD.append('D')
    
for i in range(len(arrE)):
    if(arrE[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/E/" + arrE[i])
       imlistE.append(im)
    for x in range(28):
        for y in range(28):
            imageE.append(imlistE[i][x][y])
    featuresE.append(imageE)
for q in range(len(arrE)):
    labelE.append('E')

for i in range(len(arrF)):
    if(arrF[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/F/" + arrF[i])
       imlistF.append(im)
    for x in range(28):
        for y in range(28):
            imageF.append(imlistF[i][x][y])
    featuresF.append(imageF)
for q in range(len(arrF)):
    labelF.append('F')

for i in range(len(arrG)):
    if(arrG[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/G/" + arrG[i])
       imlistG.append(im)
    for x in range(28):
        for y in range(28):
            imageG.append(imlistG[i][x][y])
    featuresG.append(imageG)

for q in range(len(arrG)):
    labelG.append('G')

for i in range(len(arrH)):
    if(arrH[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/H/" + arrH[i])
       imlistH.append(im)
    for x in range(28):
        for y in range(28):
            imageH.append(imlistH[i][x][y])
    featuresH.append(imageH)

for q in range(len(arrH)):
    labelH.append('H')

for i in range(len(arrI)):
    if(arrI[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/I/" + arrI[i])
       imlistI.append(im)
    for x in range(28):
        for y in range(28):
            imageI.append(imlistI[i][x][y])
    featuresI.append(imageI)

for q in range(len(arrI)):
    labelI.append('I')

for i in range(len(arrJ)):
    if(arrJ[i] != 'notMNIST.py'):
       im = imread("/home/divyanshu/Desktop/notMNIST_small/J/" + arrJ[i])
       imlistJ.append(im)
    for x in range(28):
        for y in range(28):
            imageJ.append(imlistJ[i][x][y])
    featuresJ.append(imageJ)
for q in range(len(arrJ)):
    labelJ.append('J')
            
features = featuresA + featuresB + featuresC + featuresD + featuresE + featuresF + featuresG + featuresH + featuresI + featuresJ
labels = labelA + labelB + labelC + labelD + labelE + labelF + labelG + labelH + labelI + labelJ
dataset = {"features": features, "labels": labels}
import pickle
pickle_out = open("dataset.pickle","wb")
pickle.dump(dataset, pickle_out)
pickle_out.close()