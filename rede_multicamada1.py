# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 00:31:06 2018

@author: Administrador
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])

saidas = np.array([[0], [1], [1], [0]])

peso0 = np.array([[-0.424, -0.740, -0.961]])
peso1 = np.array([[0.358, -0.577, -0.469]])
pesos1 = np.array([[-0.017, -0.893, 0.148]])

epocas = 100

