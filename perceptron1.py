# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:17:10 2018

@author: Administrador
"""

import numpy as np

entradas = np.array([1, 2, 5])
pesos = np.array([0.7, 0.1, 0]) #sinapses

def soma(e, p):
    return e.dot(p)
#dot product/ produto escalar
    
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)