import Menu
import Gestion_Stock
def main():
    Gestion_Stock.inicializar()
    while True:
        opcion = Menu.mostrar_menu()
        if opcion == 1:
            Gestion_Stock.cargar_stock()
        elif opcion == 2:
            Gestion_Stock.mostrar_stock()
        elif opcion == 3:
            cat = input("Ingrese el tipo de producto a contar (enlatados, frutas, congelados, panadería): ")
            if cat in Gestion_Stock.cantidad:
                Gestion_Stock.contar(Gestion_Stock.cantidad[cat])
            else:
                print("Categoría no válida.")
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción incorrecta.")
if __name__ == "__main__":
    main()