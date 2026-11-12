import Menu
import Gestion_Stock

def main():
    Gestion_Stock.inicializar()
    opcion = Menu.mostrar_menu()
    if opcion == 1:
        Gestion_Stock.cargar_stock()
    elif opcion == 2:
        Gestion_Stock.mostrar_stock()
    elif opcion == 3:
        # pedir la categoría y llamar a Gestion_stock.contar(...)
        ...

if __name__ == "__main__":
    main()