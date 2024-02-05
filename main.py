import time
import threading
import matplotlib.pyplot as plt
from tkinter import Tk, Frame, Entry, Label, Button, Text, Scrollbar
from logica import logicaBusqueda

class CarreraBusquedasApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Carrera entre Búsquedas")

        self.logica = logicaBusqueda()

        self.carrera_frame = Frame(self.master, width=800, height=400)
        self.carrera_frame.pack()

        self.grafico_pantalla = Label(self.carrera_frame, text="Grafico")
        self.grafico_pantalla.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.texto_resultados = Text(self.carrera_frame, width=50, height=10, wrap="none", state="disabled")
        self.texto_resultados.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.scrollbar_resultados = Scrollbar(self.carrera_frame, command=self.texto_resultados.yview)
        self.scrollbar_resultados.grid(row=1, column=2, sticky="ns")
        self.texto_resultados.config(yscrollcommand=self.scrollbar_resultados.set)

        self.boton_ejecutar = Button(self.master, text="Ejecutar", command=self.codigo_carrera)
        self.boton_ejecutar.pack()

    def codigo_carrera(self):
        datos = self.logica.obtener_datos()
        print("Datos originales:", datos)

        resultados = []
        algoritmos = ["Búsqueda Secuencial", "Búsqueda Binaria", "Bubble Sort", "Quick Sort", "Método de Inserción"]

        texto_resultados = ""

        def ejecutar_algoritmo(algoritmo, texto_resultados):
            tiempo_inicio = time.time()

            try:
                if algoritmo == "Búsqueda Secuencial":
                    self.logica.busqueda_secuencial(datos, max(datos))
                elif algoritmo == "Búsqueda Binaria":
                    datos_ordenados = self.logica.quick_sort(datos.copy())  # Ordenar datos para búsqueda binaria
                    self.logica.busqueda_binaria(datos_ordenados, max(datos))
                elif algoritmo == "Bubble Sort":
                    self.logica.ordenamiento_burbuja(datos.copy())
                elif algoritmo == "Quick Sort":
                    self.logica.quick_sort(datos.copy())
                elif algoritmo == "Método de Inserción":
                    self.logica.metodo_insercion(datos.copy())

                tiempo_fin = time.time()
                tiempo_total = tiempo_fin - tiempo_inicio
                resultados.append((algoritmo, tiempo_total))
                texto_resultados += f"{algoritmo}: {tiempo_total:.6f} segundos\n"

            except Exception as e:
                resultados.append((algoritmo, float('inf')))  # Infinito para los algoritmos que no se ejecutaron
                texto_resultados += f"{algoritmo}: Error - {str(e)}\n"

        threads = []

        for algoritmo in algoritmos:
            thread = threading.Thread(target=ejecutar_algoritmo, args=(algoritmo, texto_resultados))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        resultados_ordenados = sorted(resultados, key=lambda x: x[1])  # Ordenar resultados por tiempo

        texto_resultados += "\nResultados ordenados por tiempo:\n"
        for resultado in resultados_ordenados:
            texto_resultados += f"{resultado[0]}: {resultado[1]:.6f} segundos\n"

        self.texto_resultados.config(state="normal")
        self.texto_resultados.delete(1.0, "end")
        self.texto_resultados.insert("insert", texto_resultados)
        self.texto_resultados.config(state="disabled")

        self.generar_grafico([resultado[0] for resultado in resultados_ordenados], [resultado[1] for resultado in resultados_ordenados])

    def generar_grafico(self, algoritmos, tiempos):
        plt.bar(algoritmos, tiempos, color=['blue', 'green', 'red', 'purple', 'orange'])
        plt.xlabel('Algoritmo')
        plt.ylabel('Tiempo (segundos)')
        plt.title('Tiempos de Ejecución de Algoritmos')
        plt.show()

if __name__ == "__main__":
    carrera_pantalla = Tk()
    app = CarreraBusquedasApp(carrera_pantalla)
    carrera_pantalla.mainloop()
