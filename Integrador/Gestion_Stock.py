stock = {
    "frutas":['Manzana', 'Pera', 'Banana'],
    "congelados": ["pescado", ""], 
    "panadería":["pan", "Magdalenas", "facturas"], 
    "enlatados":['Salsa de tomate', 'atún']
}
cantidad = {
    "frutas":[0, 3, 20],
    "congelados": [6, 7], 
    "panadería":[25, 7, 8], 
    "enlatados":[5, 10]
}
global Cat
def cargar_stock():
    Cat= input("Ingrese una categoria de producto: ")
    nom = input("Ingrese el nombre del producto: ")
    cant= int(input("ingrese la cantidad que quiere añadir del producto: "))
    if Cat not in stock:
        sasd=(f"La categoria seleccionada no existe, desea crearla con el nombre {Cat}?(si/no): ")
        if sasd == "si":
            listaprod = []
            listacont = []
            nom.append(listaprod)
            cant.append(listacont)
            cantidad[Cat] += listacont
            stock[Cat] = listaprod
        else: 
            print("pos nada")
    else:
        prod = input("Ingrese de vuelta el nombre el producto: ")
        if prod not in Cat:
            print("El producto no esta en la categoria") 
        else:
            canting = int(input("Ingrese la cantidad que quiere añadir: "))
            listaprod.append(canting)
def contar(listaprod):
    Cat = input("Ingrese el tipo de producto que desea contar: ")
    if Cat in cantidad:
        print (cantidad[Cat])
        print (sum(listaprod))
def mostrar_stock():
    print(stock)
    print(cantidad)
def inicializar():
    """Deja los diccionarios de stock vacíos, listos para cargar productos."""
    for categoria in stock:
        stock[categoria] = []
    for categoria in cantidad:
        cantidad[categoria] = []