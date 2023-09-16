import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest, chisquare


def cargar_numeros():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        numeros = np.loadtxt(archivo)
        return numeros
    return None


def prueba_medias(numeros):
    media = np.mean(numeros)
    resultado = f"Media: {media:.4f}"
    return resultado


def prueba_varianza(numeros):
    varianza = np.var(numeros)
    resultado = f"Varianza: {varianza:.4f}"
    return resultado


def prueba_ks(numeros):
    ks_statistic, ks_pvalue = kstest(numeros, 'uniform')
    resultado = f"KS Estadística: {ks_statistic:.4f}\nKS Valor p: {ks_pvalue:.4f}"
    return resultado


def prueba_chi2(numeros):
    observed, _ = np.histogram(numeros, bins=10)
    expected = np.ones(10) * len(numeros) / 10
    chi2_statistic, chi2_pvalue = chisquare(observed, expected)
    resultado = f"Chi2 Estadística: {chi2_statistic:.4f}\nChi2 Valor p: {chi2_pvalue:.4f}"
    return resultado


def prueba_poker(numeros):
    digitos = set([tuple(sorted(str(int(x)))) for x in numeros])
    poker_statistic = len(digitos)
    resultado = f"Póker Estadística: {poker_statistic}"
    return resultado


def ejecutar_pruebas():
    numeros = cargar_numeros()
    if numeros is None:
        return

    resultados.delete(1.0, tk.END)
    resultados.insert(tk.END, "Resultados de las pruebas:\n\n")

    pruebas = [prueba_medias, prueba_varianza, prueba_ks, prueba_chi2, prueba_poker]
    for prueba in pruebas:
        resultado = prueba(numeros)
        resultados.insert(tk.END, resultado + "\n\n")

    # Graficar los números pseudoaleatorios
    plt.hist(numeros, bins=20)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de números pseudoaleatorios')
    plt.show()


# Crear la interfaz gráfica
root = tk.Tk()
root.title("Validación de Números Pseudoaleatorios")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

cargar_button = tk.Button(frame, text="Cargar Números", command=ejecutar_pruebas)
cargar_button.pack(fill=tk.BOTH)

resultados = tk.Text(frame, height=15, width=50)
resultados.pack(fill=tk.BOTH, padx=10, pady=10)

root.mainloop()
