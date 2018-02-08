# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:00:36 2018

@author: Administrador
"""

import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
                print('Total de erros: ' + str(erroTotal))
                print('0 e 0 - Esperado: 0 | Saída: ' +str(calculaSaida(entradas[0])))
                print('0  e 1 - Esperado: 0 | Saída: ' +str(calculaSaida(entradas[1])))
                print('1 e 0 - Esperado: 0 | Saída: ' +str(calculaSaida(entradas[2])))
                print('1 e 1 - Esperado: 1 | Saída: ' +str(calculaSaida(entradas[3])))

treinar()
print('Aprendido!')
print('0 e 0 - Esperado: 0 | Saída: ' +str(calculaSaida(entradas[0])))
print('0 e 1 - Esperado: 0 | Saída: ' +str(calculaSaida(entradas[1])))
print('1 e 0 - Esperado: 0 | Saída: ' +str(calculaSaida(entradas[2])))
print('1 e 1 - Esperado: 1 | Saída: ' +str(calculaSaida(entradas[3])))