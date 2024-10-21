import random

# Función para tirar los dados
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma_dados = dado1 + dado2
    return dado1, dado2, suma_dados

# Función para dividir un mensaje largo en varias líneas que quepan en el tablero
def dividir_mensaje(mensaje, ancho):
    palabras = mensaje.split()
    lineas = []
    linea_actual = ""
    for palabra in palabras:
        if len(linea_actual) + len(palabra) + 1 > ancho:
            lineas.append(linea_actual)
            linea_actual = palabra
        else:
            if linea_actual:
                linea_actual += " "
            linea_actual += palabra
    if linea_actual:
        lineas.append(linea_actual)
    return lineas

# Función para mostrar el tablero y las posiciones de los jugadores
def mostrar_tablero(posiciones, mensaje):
    # Tablero original dividido en filas y columnas
    fila_arriba = ["Parking", "Urquinoa", "Fontan", "Suerte", "Rambles", "Pl. Cat", "Anr pró"]
    fila_abajo = ["Presó", "Consell", "Marina", "Suerte", "Rosell", "Lauria", "Sortida"]
    columna_izquierda = ["Aragó", "Sant Joan", "Caixa", "Aribau", "Muntaner"]
    columna_derecha = ["Angel", "Augusta", "Caixa", "Balmes", "Gracia"]

    # Función para actualizar las casillas con jugadores
    def actualizar_casillas(casillas, fila_inicial):
        fila_con_jugadores = []
        for i, casilla in enumerate(casillas):
            jugadores_en_casilla = [jugador for jugador, pos in posiciones.items() if pos == fila_inicial + i]
            if jugadores_en_casilla:
                fila_con_jugadores.append(f"{casilla[:7]} ({','.join(jugadores_en_casilla)})")
            else:
                fila_con_jugadores.append(casilla[:7])
        return fila_con_jugadores

    # Actualizar casillas con las posiciones actuales de los jugadores
    fila_arriba = actualizar_casillas(fila_arriba, 0)
    fila_abajo = actualizar_casillas(fila_abajo, 21)
    columna_izquierda = actualizar_casillas(columna_izquierda, 7)
    columna_derecha = actualizar_casillas(columna_derecha, 12)

    # Eliminar duplicados de "Caixa"
    def eliminar_duplicados(columna):
        seen = set()
        for i in range(len(columna)):
            if columna[i] == "Caixa":
                if "Caixa" in seen:
                    columna[i] = " " * 9  # Reemplazar con espacio en blanco
                else:
                    seen.add("Caixa")

    eliminar_duplicados(columna_izquierda)
    eliminar_duplicados(columna_derecha)

    # Dividir el mensaje en líneas de máximo 49 caracteres para que quepa dentro del tablero
    lineas_mensaje = dividir_mensaje(mensaje, 49)

    # Función para hacer una fila de casillas
    def fila(casillas):
        arriba = "+---------" * len(casillas) + "+"
        medio = "".join([f"|{casilla:^9}" for casilla in casillas]) + "|"
        vacio = "|" + "         |" * len(casillas)
        return f"{arriba}\n{medio}\n{vacio}\n{arriba}"

    # Imprimir la fila superior
    print(fila(fila_arriba))

    # Imprimir las filas intermedias con el mensaje en el centro del tablero, pero sin mover los bordes
    for i, (izquierda, derecha) in enumerate(zip(columna_izquierda, columna_derecha)):
        if i == 2:  # En la tercera fila, incluir el mensaje dividido en varias líneas
            print(f"+---------+{'-' * 49}+---------+")
            for linea in lineas_mensaje:
                print(f"|{izquierda:^9}|{linea.center(49)}|{derecha:^9}|")
            print(f"|         |{' ' * 49}|         |")
            print(f"+---------+{'-' * 49}+---------+")
        else:
            print(f"+---------+{' ' * 49}+---------+")
            print(f"|{izquierda:^9}|{' ' * 49}|{derecha:^9}|")
            print(f"|         |{' ' * 49}|         |")
            print(f"+---------+{' ' * 49}+---------+")

    # Imprimir la fila inferior
    print(fila(fila_abajo))

    # Mostrar las fichas de los jugadores
    mostrar_fichas(posiciones)

# Función para mostrar las fichas de los jugadores
def mostrar_fichas(posiciones):
    # Construir la visualización de las fichas
    casillas = [
        "Parking", "Urquinoa", "Fontan", "Suerte", "Rambles", "Pl. Cat", "Anr pró",
        "Aragó", "Sant Joan", "Caixa", "Aribau", "Muntaner",
        "Angel", "Augusta", "Caixa", "Balmes", "Gracia",
        "Presó", "Consell", "Marina", "Suerte", "Rosell", "Lauria", "Sortida"
    ]

    # Crear un diccionario para almacenar las fichas en cada casilla
    fichas_en_casilla = {i: [] for i in range(len(casillas))}

    for jugador, pos in posiciones.items():
        fichas_en_casilla[pos].append(jugador)


# Banco del juego del Monopoly
def banco(cap_ini, cap_actual):
    # Verificar si el capital inicial es menor a 500.000
    if cap_actual < 500000:
        # Sumar al capital 1.000.000 actual si es menor a 500.000 
        cap_actual += 1000000
        print(f'Se han sumado 1.000.000€ el capital actual es de : {cap_actual}')
    else:
        print(f'El capital actual es suficiente: {cap_actual}€')

# Definimos los jugadores: V (Vermell), G (Groc), T (Taronja), B (Blau)
jugadores = ['V', 'G', 'T', 'B']

# Mezclamos aleatoriamente el orden de los jugadores
random.shuffle(jugadores)

# Mostramos el orden de tirada
print(f"Aquest serà l'ordre de tota la partida ({''.join(jugadores)}).")
print(f"Significa que primer tira el {jugadores[0]}, després el {jugadores[1]}, després el {jugadores[2]} i finalment el {jugadores[3]}.")

# Capital inicial de cada jugador
dinero_inicial = {jugador: 2000 for jugador in jugadores}

# Posiciones iniciales de los jugadores en el tablero
posiciones = {jugador: 0 for jugador in jugadores}  # Empiezan en la casilla 0

# Empezamos el juego y vamos turnando a los jugadores
for jugador in jugadores:
    input(f"\nEs el turno del jugador {jugador}. Presiona Enter para tirar los dados...")
    dado1, dado2, mov_casillas = tirar_dados()
    posiciones[jugador] = (posiciones[jugador] + mov_casillas) % 28  # Tablero tiene 28 casillas en total

    # Generar el mensaje completo que incluye el turno, los dados y el movimiento del jugador
    mensaje = (f"Es el turno del jugador {jugador}. Ha salido un {dado1} y un {dado2}. "
               f"El jugador {jugador} se moverá {mov_casillas} casillas.")
    
    # Mostrar el tablero con las posiciones actualizadas y el mensaje en el centro
    mostrar_tablero(posiciones, mensaje)
