
import Datos_monoply
import precios
# Orden de tirada
import random

# Función para tirar los dados
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma_dados = dado1 + dado2  
    return dado1, dado2, suma_dados

# Definimos los jugadores: V (Vermell), G (Groc), T (Taronja), B (Blau)
jugadores = ['V', 'G', 'T', 'B']

# Mezclamos aleatoriamente el orden de los jugadores
random.shuffle(jugadores)

# Posiciones iniciales de los jugadores
posiciones = {jugador: 0 for jugador in jugadores}

# Dinero inicial de cada jugador
dinero_inicial = {jugador: 2000 for jugador in jugadores}

# Función para actualizar y mostrar el tablero con las posiciones de los jugadores
def mostrar_tablero(posiciones):
    # Tablero original dividido en filas y columnas
    fila_arriba =["Sortida", "Lauria", "Rosell", "Suerte", "Marina", "Consell", "Presó"]
    fila_abajo = ["Anr pró", "Pl. Cat", "Rambles", "Suerte", "Fontan", "Urquinoa", "Parking"]
    columna_izquierda = ["Gracia", "Balmes", "Caixa", "Augusta", "Angel"]
    columna_derecha = ["Muntaner", "Aribau", "Caixa", "Sant Joan", "Aragó"]
   


    # Función para actualizar las casillas con las posiciones de los jugadores
    def actualizar_casillas(casillas, fila_inicial):
        fila_con_jugadores = []
        for i, casilla in enumerate(casillas):
            jugadores_en_casilla = [jugador for jugador, pos in posiciones.items() if pos == fila_inicial + i]
            if jugadores_en_casilla:
                jugadores_str = "".join(jugadores_en_casilla)
                espacio_jugadores = f"({jugadores_str})"
                # Aseguramos que las casillas mantengan tamaño fijo: 9 caracteres
                espacio_total = 9
                contenido = casilla[:7] + espacio_jugadores  # Añadir casilla y jugadores
                fila_con_jugadores.append(contenido[:espacio_total].ljust(espacio_total))  # Cortar y rellenar si es necesario
            else:
                fila_con_jugadores.append(casilla.ljust(9))  # Mantener tamaño fijo
        return fila_con_jugadores

    # Actualizamos las casillas de cada parte del tablero
    fila_arriba = actualizar_casillas(fila_arriba, 0)
    fila_abajo = actualizar_casillas(fila_abajo, 21)
    columna_izquierda = actualizar_casillas(columna_izquierda, 7)
    columna_derecha = actualizar_casillas(columna_derecha, 12)

    # Función para mostrar una fila del tablero
    def fila(casillas):
        arriba = "+---------" * len(casillas) + "+"
        medio = "".join([f"|{casilla:^9}" for casilla in casillas]) + "|"
        vacio = "|" + "         |" * len(casillas)
        return f"{arriba}\n{medio}\n{vacio}\n{arriba}"

    # Mostrar la fila superior del tablero
    print(fila(fila_arriba))

    # Mostrar las columnas izquierda y derecha con espacio en el medio
    for izquierda, derecha in zip(columna_izquierda, columna_derecha):
        print(f"+---------+{' ' * 49}+---------+")
        print(f"|{izquierda:^9}|{' ' * 49}|{derecha:^9}|")
        print(f"|         |{' ' * 49}|         |")
        print(f"+---------+{' ' * 49}+---------+")

    # Mostrar la fila inferior del tablero
    print(fila(fila_abajo))

# Función para consultar los precios de las propiedades
def Precios():
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
    
    for fila in lista_precios:
        print(f"{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<15} {fila[4]:<10} {fila[5]:<10}")

# Función para las interacciones del jugador
def interacciones_jugadores(jugador):
    print(f'\nEs el turno de "{jugador}". Opciones: 1. Pasar, 2. Comprar casa, 3. Comprar hotel, 4. Ver precios')
    seleccion = input("Selecciona una opción (1-4): ")

    if seleccion == "1":
        print(f"{jugador} ha decidido pasar su turno.")
        
    elif seleccion == "2":
        print(f"{jugador} ha decidido comprar una casa.")

    elif seleccion == "3":
        print(f"{jugador} ha decidido comprar un hotel.")

    elif seleccion == "4":
        print(f"{jugador} está revisando los precios.")
        Precios()
        input("Escribe 'Salir' para salir de la lista de precios: ")
    else:
        print("Opción no válida. Intenta de nuevo.") 

# Función principal para simular el juego
def jugar():
    while True:  # Bucle infinito hasta que se decida terminar el juego
        for jugador in jugadores:
            input(f"\nEs el turno del jugador {jugador}. Presiona Enter para tirar los dados...")
            dado1, dado2, mov_casillas = tirar_dados()
            posiciones[jugador] = (posiciones[jugador] + mov_casillas) % 28  # Actualizamos la posición del jugador

            # Mostrar el resultado del turno
            mensaje = (f"{jugador} ha tirado los dados: {dado1} y {dado2}, se mueve {mov_casillas} casillas.")
            print(mensaje)

            # Mostrar el tablero actualizado
            mostrar_tablero(posiciones)

            # Interacción del jugador (opciones de juego)
            interacciones_jugadores(jugador)

            # Separador de turnos
            print("-" * 30)

# Llamamos a la función para comenzar el juego
jugar()
import random

# Datos de jugadores
jugadores = {
    'VermeLl': {
        "CaLles": [],
        "Dinero": 2000,
        "Especial": [],
        "CasiLla": 0,
        "Posicion": 0,
        "Inicial": "V"
    },
    'Blau': {
        "CaLles": [],
        "Dinero": 2000,
        "Especial": [],
        "CasiLla": 0,
        "Posicion": 0,
        "Inicial": "B"
    },
    'Groc': {
        "CaLles": [],
        "Dinero": 2000,
        "Especial": [],
        "CasiLla": 0,
        "Posicion": 0,
        "Inicial": "G"
    },
    'Taronja': {
        "CaLles": [],
        "Dinero": 2000,
        "Especial": [],
        "CasiLla": 0,
        "Posicion": 0,
        "Inicial": "T"
    }
}

# Información de propiedades
casillas = [
    {"nombre": "Sortida", "jugadores": [], "tipo": "especial", "Posicion": 0},
    {"nombre": "Lauria", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 1},
    {"nombre": "Roselló", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 2},
    {"nombre": "Suerte", "jugadores": [], "Posicion": 3},
    {"nombre": "Marina", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 4},
    {"nombre": "Consell", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 5},
    {"nombre": "Prisión", "jugadores": [], "Posicion": 6},
    {"nombre": "Muntaner", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 7},
    {"nombre": "Aribau", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 8},
    {"nombre": "Caixa", "jugadores": [], "Posicion": 9},
    {"nombre": "S.Joan", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 10},
    {"nombre": "Aragó", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 11},
    {"nombre": "Parking", "jugadores": [], "tipo": "especial", "propietario": "Banco", "Posicion": 12},
    {"nombre": "Urquinaona", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 13},
    {"nombre": "Fontana", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 14},
    {"nombre": "Sort", "jugadores": [], "tipo": "especial", "propietario": "Banco", "Posicion": 15},
    {"nombre": "Rambles", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 16},
    {"nombre": "Pl. Catalunya", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 17},
    {"nombre": "Anr pró", "jugadores": [], "tipo": "especial", "Posicion": 18},
    {"nombre": "Angel", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 19},
    {"nombre": "Augusta", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 20},
    {"nombre": "Caixa", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 21},
    {"nombre": "Balmes", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 22},
    {"nombre": "Gracia", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 23},
    {"nombre": "Pl. Cat", "jugadores": [], "tipo": "caLle", "propietario": "Banco", "alquilar casa": 0, "alquilar hotel": 0, "comprar terreno": 0, "comprar casa": 0, "comprar hotel": 0, "Posicion": 24}
]

# Función para tirar los dados
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma_dados = dado1 + dado2  
    return dado1, dado2, suma_dados

# Función para actualizar y mostrar el tablero con las posiciones de los jugadores
def mostrar_tablero():
    # Mostrar el tablero de forma simplificada
    print("\nTablero:")
    for casilla in casillas:
        jugadores_en_casilla = [jugador for jugador, info in jugadores.items() if info['Posicion'] == casilla["Posicion"]]
        casilla_display = f"{casilla['nombre']} - Jugadores: {', '.join(jugadores_en_casilla) if jugadores_en_casilla else 'Nadie'}"
        print(casilla_display)

# Función principal del juego
def jugar():
    turno = 0
    while True:
        jugador_actual = list(jugadores.keys())[turno]
        print(f"\nEs el turno de {jugador_actual}. Dinero: {jugadores[jugador_actual]['Dinero']}")
        
        # Tirar dados
        dado1, dado2, suma = tirar_dados()
        print(f"{jugador_actual} tiró: {dado1} + {dado2} = {suma}")
        
        # Mover al jugador
        posicion_actual = jugadores[jugador_actual]["Posicion"]
        nueva_posicion = (posicion_actual + suma) % len(casillas)
        jugadores[jugador_actual]["Posicion"] = nueva_posicion
        
        # Mostrar el tablero
        mostrar_tablero()
        
        # Acciones en la nueva posición
        casilla_actual = casillas[nueva_posicion]
        
        # Si la casilla es una propiedad
        if "tipo" in casilla_actual and casilla_actual["tipo"] == "caLle":
            print(f"{jugador_actual} cayó en {casilla_actual['nombre']}.")
            if casilla_actual["propietario"] == "Banco":
                # Opción de comprar la propiedad
                comprar = input(f"¿Deseas comprar {casilla_actual['nombre']} por {casilla_actual['comprar terreno']}? (s/n): ")
                if comprar.lower() == 's':
                    if jugadores[jugador_actual]['Dinero'] >= casilla_actual['comprar terreno']:
                        jugadores[jugador_actual]['Dinero'] -= casilla_actual['comprar terreno']
                        casilla_actual['propietario'] = jugador_actual
                        jugadores[jugador_actual]['CaLles'].append(casilla_actual['nombre'])
                        print(f"{jugador_actual} compró {casilla_actual['nombre']}.")
                    else:
                        print(f"{jugador_actual} no tiene suficiente dinero para comprar {casilla_actual['nombre']}.")
                else:
                    print(f"{jugador_actual} decidió no comprar {casilla_actual['nombre']}.")
            else:
                print(f"{jugador_actual} cayó en la propiedad de {casilla_actual['propietario']}.")
                
        # Pasar el turno al siguiente jugador
        turno = (turno + 1) % len(jugadores)

# Iniciar el juego
if __name__ == "__main__":
    jugar()
