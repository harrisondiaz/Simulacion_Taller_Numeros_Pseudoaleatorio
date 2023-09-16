import random

'''
    Clase para generar números pseudoaleatorios
'''
class pseudorandom:
    # Función para generar números pseudoaleatorios usando el método de Cuadrados Medios
    def cuadrados_medios(seed, n):
        pseudoaleatorios = []
        for _ in range(n):
            seed = int(str(seed ** 2).zfill(8)[2:6])
            pseudoaleatorios.append(seed / 10000)
        return pseudoaleatorios

    # Función para generar números pseudoaleatorios usando el método congruencial lineal
    def congruencial_lineal(a, c, m, seed, n):
        pseudoaleatorios = []
        for _ in range(n):
            seed = (a * seed + c) % m
            pseudoaleatorios.append(seed / m)
        return pseudoaleatorios

    # Función para generar números pseudoaleatorios uniformemente distribuidos
    def distribucion_uniforme(a, b, n):
        pseudoaleatorios = []
        for _ in range(n):
            pseudoaleatorios.append(random.uniform(a, b))
        return pseudoaleatorios

    # Función para generar números pseudoaleatorios normalmente distribuidos
    def distribucion_normal(media, desviacion, n):
        pseudoaleatorios = []
        for _ in range(n):
            pseudoaleatorios.append(random.normalvariate(media, desviacion))
        return pseudoaleatorios