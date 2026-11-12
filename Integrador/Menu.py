def mostrar_menu():
    print("1. Cargar stock")
    print("2. Mostrar total del stock")
    print("3. Mostrar cantidad de productos")
    opcion = int(input("Elija una opción: "))
    return opcion
    if mostrar_menu == "1":
        from Gestion_Stock import cargar_stock
        cargar_stock
    if mostrar_menu == "2":
        from Gestion_Stock import mostrar_stock
    if mostrar_menu == "3":
        from Gestion_Stock import contar