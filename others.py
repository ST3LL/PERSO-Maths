#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:32:07 2020

@author: tinou_99
"""

import numpy as np

#MOYENNE
def moyenne(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return (s/len(l))

def numpy_moyenne(l):
    return np.mean(l)
   
    

#ECART-TYPE 
def nympy_ecarttype(x):
    return np.std(x)



#PRODUIT SCALAIRE
def produit_scalaire(u,v):
    return sum([x * y for x, y in zip(u, v)])

def numpy_produit_scalaire(u,v):
    return np.dot(u,v)



#VARIANCE
def variance(a):
    m = moyenne(a)
    v = 0
    for i in (len(a)):
        v += (a[i]-m)**2
    return (v/len(a))

def nympy_variance(a):
    return np.var(a)



#COVARIANCE
def covariance(x):
    return np.cov(x)