#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:39:26 2020

@author: tinou_99
"""

import numpy as np
from math import sqrt


def ps(x,y):
    return np.dot(x,y)

def e1(x):
    return (x / np.sqrt(x.dot(x)))


#def g_s(X):
    

if __name__ == "__main__":
    a = np.array([1, 0, -1])
    b = np.array([1/sqrt(2), -1/sqrt(2), 0])
    print(e1(a))
    