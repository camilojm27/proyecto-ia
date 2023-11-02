import numpy as np
from Nodo import Nodo

nombre_archivo = "mundos/prueba1.txt"


def cargar_mapa_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        matriz = []
        for linea in lineas:
            fila = list(map(int, linea.strip().split()))
            matriz.append(fila)
        return np.array(matriz)


mapa = cargar_mapa_desde_archivo(nombre_archivo)


def bfs(mapa):
    nodos_creados = 0
    nodos_expandidos = 0
    for i in range(0, mapa.shape[0]):
        for j in range(0, mapa.shape[1]):
            if mapa[i][j] == 5:
                posicion = (j, i)
                mapa[i][j] = 0
                break
    raiz = Nodo(mapa, posicion, [False, False], [False, False], [posicion], [posicion])
    cola = [raiz]
    while len(cola) > 0:
        nodo = cola.pop(0)
        # print(nodos_creados)
        # print(nodos_expandidos)

        nodos_expandidos += 1

        if (nodo.encontrarCubeta1()):
            if (nodo.encontrarFuegos() and nodo.encontrarHidrante()):
                return nodo.recorrido  # , nodos_creados, nodos_expandidos   #retorno solucion

        x = nodo.posicion[0]
        y = nodo.posicion[1]
        # arriba
        xI = x
        yI = y - 1

        if yI >= 0 and not ((xI, yI) in nodo.nodo_visitado) and nodo.matriz[y, x] != 1:
            nodo_visitado = nodo.nodo_visitado.copy()  # pasar por valor
            nodo_visitado.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI, yI))
            estado = nodo.estado_inicial.copy()
            estadoFuego = nodo.estado_fuego.copy()
            estadoHidrante = nodo.estado_hidrante.copy()

            hijo = Nodo(
                nodo.matriz, (xI, yI), estadoFuego, estadoHidrante, recorrido, nodo_visitado
            )
            nodos_creados += 1
            hijo.marcar()
            if not (hijo.encontrarFuego()):
                cola.append(hijo)
        # abajo
        xI = x
        yI = y + 1

        if yI < mapa.shape[0] and not ((xI, yI) in nodo.nodo_visitado) and nodo.matriz[y, x] != 1:
            nodo_visitado = nodo.nodo_visitado.copy()  # pasar por valor
            nodo_visitado.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI, yI))
            estado = nodo.estado_inicial.copy()
            estadoFuego = nodo.estado_fuego.copy()
            estadoHidrante = nodo.estado_hidrante.copy()

            hijo = Nodo(
                nodo.matriz, (xI, yI), estadoFuego, estadoHidrante, recorrido, nodo_visitado
            )
            nodos_creados += 1
            hijo.marcar()
            if not (hijo.encontrarFuego()):
                cola.append(hijo)

        # izquierda
        xI = x - 1
        yI = y

        if xI >= 0 and not ((xI, yI) in nodo.nodo_visitado) and nodo.matriz[y, x] != 1:
            nodo_visitado = nodo.nodo_visitado.copy()  # pasar por valor
            nodo_visitado.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI, yI))
            estado = nodo.estado_inicial.copy()
            estadoFuego = nodo.estado_fuego.copy()
            estadoHidrante = nodo.estado_hidrante.copy()

            hijo = Nodo(
                nodo.matriz, (xI, yI), estadoFuego, estadoHidrante, recorrido, nodo_visitado
            )
            nodos_creados += 1
            hijo.marcar()
            if not (hijo.encontrarFuego()):
                cola.append(hijo)

        # derecha
        xI = x + 1
        yI = y

        if xI < mapa.shape[1] and not ((xI, yI) in nodo.nodo_visitado) and nodo.matriz[y, x] != 1:
            nodo_visitado = nodo.nodo_visitado.copy()  # pasar por valor
            nodo_visitado.append((xI, yI))
            recorrido = nodo.recorrido.copy()
            recorrido.append((xI, yI))
            estado = nodo.estado_inicial.copy()
            estadoFuego = nodo.estado_fuego.copy()
            estadoHidrante = nodo.estado_hidrante.copy()

            hijo = Nodo(
                nodo.matriz, (xI, yI), estadoFuego, estadoHidrante, recorrido, nodo_visitado
            )
            nodos_creados += 1
            hijo.marcar()
            if not (hijo.encontrarFuego()):
                cola.append(hijo)

    return "no hay solucion"


print(bfs(mapa))
