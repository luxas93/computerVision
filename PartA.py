# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 14:43:32 2014

@author: Lukas
"""
import numpy as np
from numpy import linalg as LA
import math

def eulerToR(gamma,beta,alpha):

    Rgamma = np.array([[math.cos(gamma),-math.sin(gamma),0],[math.sin(gamma),math.cos(gamma),0],[0,0,1]])
    #print Rgamma
    Rbeta = np.array([[math.cos(beta),0,math.sin(beta)],[0,1,0],[-math.sin(beta),0,math.cos(beta)]])
    #print Rbeta
    Ralpha = np.array([[1,0,0],[0, math.cos(alpha),-math.sin(alpha)],[0, math.sin(alpha),math.cos(alpha)]])
    #print Ralpha
    R= np.dot(Rgamma,Rbeta,Ralpha)
    #print R
    return R
eulerToR(1,2,3)

def expToR(w1,w2,w3):
    w=np.array([[w1],[w2],[w3]])
    MagW= LA.norm(w)
   # print MagW
    wHat = np.array([[0,-w3,w2],[w3,0,-w1],[-w2,w1,0]])
    iMatrix = np.eye(3)
    #print iMatrix
    ExpCoResult = iMatrix + (wHat/MagW)*math.sin(MagW)+(((wHat**2)/(MagW**2))*(1-math.cos(MagW)))
   # print "Exponential Coordinate \n", ExpCoResult
    return ExpCoResult
#expToR(1,2,3)

def eulerToT(x,y,z,gamma,beta,alpha):
    #eulerToR(gamma,beta,alpha)
    lastLine = np.array([[0,0,0,1]])
    t_axis = np.array([[x],[y],[z]])
    newR = np.concatenate((eulerToR(gamma,beta,alpha), t_axis), axis =1)
    homogeneous = np.concatenate((newR, lastLine), axis=0)
    print homogeneous
    return homogeneous
    
#eulerToT(1,2,3,1,1,1)

def expToT(X,Y,Z,w1,w2,w3):
    botLine = np.array([[0,0,0,1]])
    tw_axis = np.array([[X],[Y],[Z]])
    newR = np.concatenate((expToR(w1,w2,w3), tw_axis), axis =1)
    homogeneousT = np.concatenate((newR, botLine), axis=0)
    print homogeneousT
    return homogeneousT
expToT(1,2,3,1,1,1)

#testing the function inside a funciton
'''def newline(x):
    print "hello",x

def newlineagain(x):
    new = newline(x)
    print "suck it ", new
        
newlineagain("you smell ")'''

#array concatanation
'''a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
#remove .T and change axis to 0 to have it the other way
print np.concatenate((a,b.T), axis=1)'''