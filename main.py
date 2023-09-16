import tkinter as tk
from tkinter import ttk
from Pseudoaleatorio import *



# Función para mostrar los resultados en una ventana de Tkinter
def mostrar_resultados():
    metodo = metodo_combo.get()
    n = int(n_entry.get())
    seed = int(seed_entry.get())

    if metodo == "Cuadrados Medios":
        pseudoaleatorios = pseudorandom.cuadrados_medios(seed, n)
    elif metodo == "Congruencial Lineal":
        a = int(a_entry.get())
        c = int(c_entry.get())
        m = int(m_entry.get())
        pseudoaleatorios = pseudorandom.congruencial_lineal(a, c, m, seed, n)
    elif metodo == "Distribución Uniforme":
        a = float(a_entry.get())
        b = float(b_entry.get())
        pseudoaleatorios = pseudorandom.distribucion_uniforme(a, b, n)
    elif metodo == "Distribución Normal":
        media = float(media_entry.get())
        desviacion = float(desviacion_entry.get())
        pseudoaleatorios = pseudorandom.distribucion_normal(media, desviacion, n)


    final_pseudoaleatorios = ""
    for i in range(len(pseudoaleatorios)):
        final_pseudoaleatorios += str(i+1) + " - " + str(pseudoaleatorios[i]) + "\n"

    resultado_label.config(text="Resultados: " +  final_pseudoaleatorios)

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Números Pseudoaleatorios")

# Crear y configurar etiquetas y entradas
metodo_label = tk.Label(root, text="Método:")
metodo_label.pack()
metodo_combo = ttk.Combobox(root, values=["Cuadrados Medios", "Congruencial Lineal", "Distribución Uniforme", "Distribución Normal"])
metodo_combo.pack()

n_label = tk.Label(root, text="Número de Iteraciones:")
n_label.pack()
n_entry = tk.Entry(root)
n_entry.pack()

seed_label = tk.Label(root, text="Semilla:")
seed_label.pack()
seed_entry = tk.Entry(root)
seed_entry.pack()

a_label = tk.Label(root, text="Parámetro 'b' (solo para Congruencial Lineal):")
a_label.pack()
a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="Parámetro 'a' (solo para Congruencial Lineal):")
b_label.pack()
b_entry = tk.Entry(root)
b_entry.pack()

c_label = tk.Label(root, text="Parámetro 'c' (solo para Congruencial Lineal):")
c_label.pack()
c_entry = tk.Entry(root)
c_entry.pack()

m_label = tk.Label(root, text="Parámetro 'm' (solo para Congruencial Lineal):")
m_label.pack()
m_entry = tk.Entry(root)
m_entry.pack()

a_uniforme_label = tk.Label(root, text="Valor 'a' (solo para Distribución Uniforme):")
a_uniforme_label.pack()
a_uniforme_entry = tk.Entry(root)
a_uniforme_entry.pack()

b_uniforme_label = tk.Label(root, text="Valor 'b' (solo para Distribución Uniforme):")
b_uniforme_label.pack()
b_uniforme_entry = tk.Entry(root)
b_uniforme_entry.pack()

media_label = tk.Label(root, text="Media (solo para Distribución Normal):")
media_label.pack()
media_entry = tk.Entry(root)
media_entry.pack()

desviacion_label = tk.Label(root, text="Desviación Estándar (solo para Distribución Normal):")
desviacion_label.pack()
desviacion_entry = tk.Entry(root)
desviacion_entry.pack()

# Botón para generar números pseudoaleatorios
generar_button = tk.Button(root, text="Generar", command=mostrar_resultados)
generar_button.pack()

# Etiqueta para mostrar los resultados
resultado_label = tk.Label(root, text="Resultados:")
resultado_label.pack()

root.configure(background="#97004e")

root.mainloop()
