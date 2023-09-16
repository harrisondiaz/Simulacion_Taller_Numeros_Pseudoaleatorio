import random
import math
from _pydecimal import Decimal

import numpy as np
'''
    Clase para generar números pseudoaleatorios
'''
class pseudorandom:

    def __init__(self, semilla):
        self.semilla = semilla
        self.Xi = semilla

    def cuadrados_medios(self, n):
        numeros_generados = []
        for _ in range(n):
            self.Xi = int(str(self.Xi ** 2).zfill(8)[2:6])
            Ri = self.Xi / 10000.0
            numeros_generados.append(Ri)
        return numeros_generados

    def congruenciales(self, n, a, c, m):
        numeros_generados = []
        for _ in range(n):
            self.Xi = (a * self.Xi + c) % m
            Ri = self.Xi / m
            numeros_generados.append(Ri)
        return numeros_generados

    def distribucion_uniforme(self, n, a, b):
        numeros_generados = self.congruenciales(n, 1664525, 1013904223, 2 ** 32)
        uniformes = [a + (b - a) * x for x in numeros_generados]
        return uniformes

    def distribucion_normal(self, n, media, desviacion):
        uniformes = self.distribucion_uniforme(n, 0, 1)
        normales = []
        for i in range(0, n, 2):
            u1 = uniformes[i]
            u2 = uniformes[i + 1]
            z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
            z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
            x1 = media + desviacion * z1
            x2 = media + desviacion * z2
            normales.extend([x1, x2])
        return normales
