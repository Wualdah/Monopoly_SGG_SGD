#Orden de tirada
import random
#Definimos los jugadores: V (Vermell), G (Groc), T (Taronja), B (Blau)
jugadores = ['V', 'G', 'T', 'B']
#Mezclamos aleatoriamente el orden de los jugadores
random.shuffle(jugadores)

def tablero_monopoly():
    # Definimos las casillas del tablero en el orden correcto
    fila_arriba = ["Parking", "Urquinoa", "Fontan", "Sort", "Rambles", "Pl. Cat", "Anr pró"]
    fila_abajo = ["Presó", "Consell", "Marina", "Suerte", "Rosell", "Lauria", "Sortida"]
    columna_izquierda = ["Aragó", "Sant Joan", "Caixa", "Aribau", "Muntaner"]
    columna_derecha = ["Angel", "Augusta", "Caixa", "Balmes", "Gracia"]

    # Función para hacer una fila de casillas
    def fila(casillas):
        arriba = "+---------" * len(casillas) + "+"
        medio = "".join([f"|{casillas:^9}" for casillas in casillas]) + "|"
        vacio = "|" + "         |" * len(casillas)
        return f"{arriba}\n{medio}\n{vacio}\n{arriba}"
        
    
    # Imprimir la fila superior
    print(fila(fila_arriba))

    # Imprimir las filas intermedias (combinando izquierda y derecha con espacio en el medio)
    for izquierda, derecha in zip(columna_izquierda, columna_derecha):
        print(f"+---------+{' ' * 49}+---------+")
        print(f"|{izquierda:^9}|{' ' * 49}|{derecha:^9}|")
        print(f"|         |{' ' * 49}|         |")
        print(f"+---------+{' ' * 49}+---------+")

    

    # Modificar la casilla "Sortida" en fila_abajo para incluir el orden de los jugadores
    fila_abajo[-1] = f'Sortida: {"".join(jugadores)}'  # Cambiamos la última posición (Sortida)
    
    # Imprimir la fila inferior
    print(fila(fila_abajo))


# Aqui lo que se ha hecho es llamara a la funcion anterior
tablero_monopoly()

#Banco del juego del Monopoly
def banco(cap_ini, cap_actual):
    # Capital inicial
    cap_actual = cap_ini

    # Verificar si el capital inicial es menor a 500.000
    if cap_actual < 500000:

        # Suma al capital 1.000.000 actual si es menor a 500.000 
        cap_actual += 1000000

        print(f'Se han sumado 1.000.000€ el capital actual es de : {cap_actual}')
    else:
        print(f'El capital actual es suficiente: {cap_actual}€')





#Mostramos el orden de tirada y el formato de salida
print(f"Significa que primer tira el {jugadores[0]}")
print(f"després el {jugadores[1]}, després el {jugadores[2]}")
print(f"finalment el {jugadores[3]}")

#Capital inicial de cada jugador
dinero_inicial = {}
for jugador in jugadores:
    dinero_inicial[jugador] = 2000