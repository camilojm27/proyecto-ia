import tkinter as tk
import time as t
import busqueda as bf
import numpy as np

nombre_archivo = "mundos/prueba1.txt"
def cargar_mapa_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        mapa = []
        for linea in lineas:
            fila = list(map(int, linea.strip().split()))
            mapa.append(fila)
        return np.array(mapa)

mapa = cargar_mapa_desde_archivo(nombre_archivo)

recorrido = bf.bfs(mapa)
print(recorrido)
tamano_celda = 40
filas = len(mapa)
columnas = len(mapa[0])

# Función para mostrar la mapa
def mostrar_mapa():
    for i in range(filas):
        for j in range(columnas):
            valor = mapa[i][j]
            color = 'green' if valor == 0 else 'black' if valor == 1 else 'red' if valor == 2 else 'green' if valor == 3 else 'blue' if valor == 4 else 'yellow' if valor == 5 else 'orange' if valor == 6 else 'white'
            canvas.create_rectangle(j * tamano_celda, i * tamano_celda, (j + 1) * tamano_celda, (i + 1) * tamano_celda, fill=color)
            if (j, i) in recorrido:
                canvas.create_text(j * tamano_celda + tamano_celda // 2, i * tamano_celda + tamano_celda // 2, text=str(mapa[i][j]), fill='white', font=('Helvetica', 14))
    ventana.update()

# Crear una ventana
ventana = tk.Tk()
ventana.title("Recorrido en mapa")

# Crear un lienzo (canvas) para mostrar la mapa
canvas = tk.Canvas(ventana, width=columnas * tamano_celda, height=filas * tamano_celda)
canvas.pack()

# Botón para comenzar la visualización del recorrido
boton = tk.Button(ventana, text="Mostrar Recorrido", command=mostrar_mapa)
boton.pack()

def animar_recorrido():
    for paso in recorrido:
        mapa[paso[1]][paso[0]] = 8  # Marcamos la posición actual como 8
        mostrar_mapa()
        t.sleep(0.2)  # Espera 0.5 segundos entre pasos (ajusta según lo desees)
        mapa[paso[1]][paso[0]] = 0  # Restauramos el valor original
        mostrar_mapa()
    mostrar_mapa()  # Asegurarse de mostrar la mapa final

# Botón para iniciar la animación
boton_animacion = tk.Button(ventana, text="Iniciar Animación", command=animar_recorrido)
boton_animacion.pack()

ventana.mainloop()
