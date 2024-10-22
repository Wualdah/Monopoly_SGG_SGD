import monopoly

# Precios de alquiler, compra, de: casas, hoteles y terrenos
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

