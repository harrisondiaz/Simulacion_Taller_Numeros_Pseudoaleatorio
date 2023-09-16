import tkinter as tk
from tkinter import ttk

import Pseudoaleatorio


class GeneradorAleatorioGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Números Pseudoaleatorios")

        # Crear una pestaña para cada método
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Pestaña para Cuadrados Medios
        self.cuadrados_medios_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.cuadrados_medios_tab, text="Cuadrados Medios")
        self.cuadrados_medios_output = tk.Text(self.cuadrados_medios_tab, wrap=tk.WORD)
        self.cuadrados_medios_output.pack()

        # Pestaña para Métodos Congruenciales
        self.congruenciales_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.congruenciales_tab, text="Métodos Congruenciales")
        self.congruenciales_output = tk.Text(self.congruenciales_tab, wrap=tk.WORD)
        self.congruenciales_output.pack()

        # Pestaña para Distribución Uniforme
        self.distribucion_uniforme_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.distribucion_uniforme_tab, text="Distribución Uniforme")
        self.distribucion_uniforme_output = tk.Text(self.distribucion_uniforme_tab, wrap=tk.WORD)
        self.distribucion_uniforme_output.pack()

        # Pestaña para Distribución Normal
        self.distribucion_normal_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.distribucion_normal_tab, text="Distribución Normal")
        self.distribucion_normal_output = tk.Text(self.distribucion_normal_tab, wrap=tk.WORD)
        self.distribucion_normal_output.pack()

        # Entradas para los parámetros
        self.parametros_frame = ttk.LabelFrame(root, text="Parámetros")
        self.parametros_frame.pack(pady=10)

        self.semilla_label = ttk.Label(self.parametros_frame, text="Semilla:")
        self.semilla_label.grid(row=0, column=0, padx=5, pady=5)
        self.semilla_entry = ttk.Entry(self.parametros_frame)
        self.semilla_entry.grid(row=0, column=1, padx=5, pady=5)

        self.a_label = ttk.Label(self.parametros_frame, text="a:")
        self.a_label.grid(row=1, column=0, padx=5, pady=5)
        self.a_entry = ttk.Entry(self.parametros_frame)
        self.a_entry.grid(row=1, column=1, padx=5, pady=5)

        self.c_label = ttk.Label(self.parametros_frame, text="c:")
        self.c_label.grid(row=2, column=0, padx=5, pady=5)
        self.c_entry = ttk.Entry(self.parametros_frame)
        self.c_entry.grid(row=2, column=1, padx=5, pady=5)

        self.m_label = ttk.Label(self.parametros_frame, text="m:")
        self.m_label.grid(row=3, column=0, padx=5, pady=5)
        self.m_entry = ttk.Entry(self.parametros_frame)
        self.m_entry.grid(row=3, column=1, padx=5, pady=5)

        self.a_uniforme_label = ttk.Label(self.parametros_frame, text="a (Uniforme):")
        self.a_uniforme_label.grid(row=4, column=0, padx=5, pady=5)
        self.a_uniforme_entry = ttk.Entry(self.parametros_frame)
        self.a_uniforme_entry.grid(row=4, column=1, padx=5, pady=5)

        self.b_uniforme_label = ttk.Label(self.parametros_frame, text="b (Uniforme):")
        self.b_uniforme_label.grid(row=5, column=0, padx=5, pady=5)
        self.b_uniforme_entry = ttk.Entry(self.parametros_frame)
        self.b_uniforme_entry.grid(row=5, column=1, padx=5, pady=5)

        self.media_normal_label = ttk.Label(self.parametros_frame, text="Media (Normal):")
        self.media_normal_label.grid(row=6, column=0, padx=5, pady=5)
        self.media_normal_entry = ttk.Entry(self.parametros_frame)
        self.media_normal_entry.grid(row=6, column=1, padx=5, pady=5)

        self.desviacion_normal_label = ttk.Label(self.parametros_frame, text="Desviación (Normal):")
        self.desviacion_normal_label.grid(row=7, column=0, padx=5, pady=5)
        self.desviacion_normal_entry = ttk.Entry(self.parametros_frame)
        self.desviacion_normal_entry.grid(row=7, column=1, padx=5, pady=5)

        # Botón para generar números pseudoaleatorios
        self.generate_button = ttk.Button(root, text="Generar", command=self.generar_numeros)
        self.generate_button.pack()

        # Objeto GeneradorAleatorio
        self.generador = None

    def obtener_parametros(self):
        semilla = int(self.semilla_entry.get())
        a = int(self.a_entry.get())
        c = int(self.c_entry.get())
        m = int(self.m_entry.get())
        a_uniforme = int(self.a_uniforme_entry.get())
        b_uniforme = int(self.b_uniforme_entry.get())
        media_normal = float(self.media_normal_entry.get())
        desviacion_normal = float(self.desviacion_normal_entry.get())
        return semilla, a, c, m, a_uniforme, b_uniforme, media_normal, desviacion_normal

    def generar_numeros(self):
        semilla, a, c, m, a_uniforme, b_uniforme, media_normal, desviacion_normal = self.obtener_parametros()

        # Crear el objeto GeneradorAleatorio con los parámetros ingresados
        self.generador = Pseudoaleatorio.pseudorandom(semilla=semilla)

        # Cuadrados Medios
        cuadrados_medios_result = self.generador.cuadrados_medios(10)
        self.mostrar_resultado(self.cuadrados_medios_output, "Cuadrados Medios:", cuadrados_medios_result)

        # Métodos Congruenciales
        congruenciales_result = self.generador.congruenciales(10, a, c, m)
        self.mostrar_resultado(self.congruenciales_output, "Métodos Congruenciales:", congruenciales_result)

        # Distribución Uniforme
        uniformes_result = self.generador.distribucion_uniforme(10, a_uniforme, b_uniforme)
        self.mostrar_resultado(self.distribucion_uniforme_output, "Distribución Uniforme:", uniformes_result)

        # Distribución Normal
        normales_result = self.generador.distribucion_normal(10, media_normal, desviacion_normal)
        self.mostrar_resultado(self.distribucion_normal_output, "Distribución Normal:", normales_result)

    def mostrar_resultado(self, output_widget, label, resultados):
        output_widget.delete(1.0, tk.END)  # Limpiar el widget de texto
        output_widget.insert(tk.END, label + "\n")
        for resultado in resultados:
            output_widget.insert(tk.END, str(resultado) + "\n")


def main():
    root = tk.Tk()
    app = GeneradorAleatorioGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
