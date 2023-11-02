class Nodo:
    def __init__(self, matriz, posicion, estado_fuego, estado_hidrante, recorrido, nodo_visitado):
        self.matriz = matriz
        self.posicion = posicion
        #self.estado_inicial = estado_inicial
        self.estado_fuego = estado_fuego #Si esta [False, False] No se han apagado los fuegos
        self.estado_hidrante = estado_hidrante #Solo puede haber 1 hidrante
        self.recorrido = recorrido
        self.nodo_visitado = nodo_visitado  # evita devolverse

    def encontrarCubeta1(self):
        return self.estado_fuego[0] and self.estado_fuego[1]

    def encontrarFuegos(self):
        return self.estado_fuego[0] and self.estado_fuego[1]

    def encontrarHidrante(self):
        return self.estado_hidrante[0] or self.estado_hidrante[1]

    def encontrarFuego(self):
        return self.estado_inicial[0] and self.estado_inicial[1]

    def marcar(self):
        casilla_actual = self.matriz[self.posicion[1], self.posicion[0]]
        #Encontrar la cubeta (Caulquera) - condicionar si la cubeta es de 1L o 2L
        if casilla_actual == 3 or casilla_actual == 4 and not (self.estado_inicial[0]):
            nuevo_estado = self.estado_inicial.copy()
            nuevo_estado[0] = True
            self.estado_inicial = nuevo_estado
            self.nodo_visitado = []
            #print('cubeta')
        #Si tiene cubeta y esta en la 6, recargue su cubeta rey
        if self.estado_inicial[0] and casilla_actual == 6:
            nuevo_estado = self.estado_inicial.copy()
            nuevo_estado[1] = True
            self.estado_inicial = nuevo_estado
            self.nodo_visitado = []

        if casilla_actual == 6 and not (self.estado_fuego[0]):
            nuevo_estado = self.estado_fuego.copy()
            nuevo_estado[0] = True
            self.estado_fuego = nuevo_estado
            self.nodo_visitado = []

        if self.estado_fuego[0] and casilla_actual == 2:
            nuevo_estado = self.estado_fuego.copy()
            nuevo_estado[1] = True
            self.estado_fuego = nuevo_estado
            self.nodo_visitado = []

        if casilla_actual == 2 and (self.estado_hidrante[0]):
            nuevo_estado = self.estado_hidrante.copy()
            nuevo_estado[0] = True
            #   nuevo_estado[1] = True
            self.estado_hidrante = nuevo_estado
            self.nodo_visitado = []

        if self.estado_hidrante[0] and casilla_actual == 4:
            #print('hidrante encontrado', self.estado_hidrante)
            nuevo_estado = self.estado_hidrante.copy()
            nuevo_estado[1] = True
            self.estado_hidrante = nuevo_estado
            self.nodo_visitado = []
