stock = {
    "frutas": ['Manzana', 'Pera', 'Banana'],
    "congelados": ["pescado", ""], 
    "panadería": ["pan", "Magdalenas", "facturas"], 
    "enlatados": ['Salsa de tomate', 'atún']
}

cantidad = {
    "frutas": [0, 3, 20],
    "congelados": [6, 7], 
    "panadería": [25, 7, 8], 
    "enlatados": [5, 10]
}
def inicializar():
    """Deja los diccionarios de stock vacíos, listos para cargar productos."""
    for categoria in stock:
        stock[categoria] = []
    for categoria in cantidad:
        cantidad[categoria] = []
def cargar_stock():
    cat = input("Ingrese una categoría (frutas, congelados, panadería, enlatados): ")
    if cat not in stock:
        respuesta = input(f"La categoría '{cat}' no existe, ¿desea crearla? (si/no): ")
        if respuesta == "si":
            stock[cat] = []
            cantidad[cat] = []
        else:
            print("Operación cancelada.")
            return
    nom = input("Ingrese el nombre del producto: ")
    cant = int(input("Ingrese la cantidad que quiere añadir: "))
    stock[cat].append(nom)
    cantidad[cat].append(cant)
    print(f"Producto '{nom}' cargado correctamente en '{cat}'.")
def mostrar_stock():
    print(stock)
    print(cantidad)
def contar(lista_cantidades):
    cantidad_productos = len(lista_cantidades)
    suma_total = sum(lista_cantidades)
    print(cantidad_productos)
    print(suma_total)