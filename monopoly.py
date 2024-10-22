import precios
# Orden de tirada
import random

# Definimos los jugadores: V (Vermell), G (Groc), T (Taronja), B (Blau)
jugadores = ['V', 'G', 'T', 'B']

# Mezclamos aleatoriamente el orden de los jugadores
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

    # Modificar la casilla "Sortida" para que tenga los jugadores en una línea y "Sortida" en la siguiente
    jugadores_concat = "".join(jugadores)  # Concatenamos los jugadores
    fila_abajo[-1] = " " * 9  # Crear una casilla vacía

    # Imprimir la fila inferior con la casilla "Sortida" en el formato adecuado
    arriba = "+---------+---------+---------+---------+---------+---------+---------+"
    print(arriba)
    
    # Imprimir los nombres de los jugadores en la primera línea
    medio = "".join([f"|{casilla:^9}" for casilla in fila_abajo[:-1]]) + f"|{jugadores_concat:^9}|"
    print(medio)
    
    # Imprimir la palabra "Sortida" en la segunda línea
    vacio = "|" + "         |" * (len(fila_abajo) - 1) + f"{'Sortida':^9}|"
    print(vacio)
    print(arriba)

# Aqui lo que se ha hecho es llamar a la funcion anterior
tablero_monopoly()

# Banco del juego del Monopoly
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

# Mostramos el orden de tirada y el formato de salida
print(f"Significa que primer tira el {jugadores[0]}")
print(f"després el {jugadores[1]}, després el {jugadores[2]}")
print(f"finalment el {jugadores[3]}")

# Capital inicial de cada jugador
dinero_inicial = {}
for jugador in jugadores:
    dinero_inicial[jugador] = 2000

def Precios ():
    lista_precios = [
    ["Lauria", 10, 15, 50, 200, 250],
    ["Roselló", 10, 15, 50, 225, 255],
    ["Marina", 15, 15, 50, 250, 260],
    ["C. de cent", 15, 20, 50, 275, 265],
    ["Muntaner", 20, 20, 60, 300, 270],
    ["Aribau", 20, 20, 60, 300, 270],
    ["Sant Joan", 25, 25, 60, 350, 280],
    ["Aragó", 25, 25, 60, 375, 285],
    ["Urquinaona", 30, 25, 70, 400, 290],
    ["Fontana", 30, 30, 70, 425, 300],
    ["Les Rambles", 35, 30, 70, 450, 310],
    ["Pl. Catalunya", 35, 30, 70, 475, 320],
    ["P.Àngel", 40, 35, 80, 500, 330],
    ["Via Augusta", 40, 35, 80, 525, 340],
    ["Balmes", 50, 40, 80, 550, 350],
    ["Pg.de Gràcia", 50, 50, 80, 525, 360]
]
    columnas = ["Carrer", "Ll.Casa", "Ll.Hotel", "Cmp.Trrny", "Cmp.Casa", "Cmp.Hotel"]
    print(f"{columnas[0]:<15} {columnas[1]:<10} {columnas[2]:<10} {columnas[3]:<15} {columnas[4]:<10} {columnas[5]:<10}")
    print("-" * 75)





    # Imprimir cada fila de precios
    for fila in lista_precios:
        print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<15} {fila[4]:<10} {fila[5]:<10}")

# Tirada del Primer jugador:
def interacciones_jugadores(jugador):
    print(f'Juga" {jugador}", opcions: passar, comprar casa, comprar hotel, preus')
    seleccion = input("Selecciona una opció: ")

    if seleccion == "1" :
        print(f"{jugador} ha decidido pasar su turno.")
        
    elif seleccion == "2":
        print(f"{jugador} ha decidido comprar una casa.")

    elif seleccion == "3":
        print(f"{jugador} ha decidido comprar un hotel.")

    elif seleccion == "4":
        print(f"{jugador} está revisando los precios.")
        Precios()
        seleccion == "Salir"
        input(f"Escribe ""Salir"" para salir de la lista de precios: ")
    else:
        print("Opción no válida. Intenta de nuevo.") 


def jugar():
    for jugador in jugadores:
        interacciones_jugadores(jugador)
        print("-" * 30)

# Llamamos a la función para simular los turnos
jugar()
