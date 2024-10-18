# ud1_ejercicio_obligatorio_Manuel_Mas_Lopez.py

# Lista inicial de vuelos
vuelos = [
    {"origen": "Valencia", "destino": "Menorca", "dia": "15-08", "clase": "turista"},
    {"origen": "Valencia", "destino": "Tenerife", "dia": "20-08", "clase": "turista"},
    {"origen": "Paris", "destino": "Valencia", "dia": "15-08", "clase": "primera"},
    {"origen": "Atenas", "destino": "Valencia", "dia": "20-08", "clase": "primera"},
]
# Imprime todos los datos de los vuelos
def imprimir(vuelos):
    for vuelo in vuelos:
        print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Dia: {vuelo['dia']}, Clase: {vuelo['clase']}")
# Busca y muestra los vuelos segun el origen introducido por el usuario
def buscar_origen(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    encontrados = [vuelo for vuelo in vuelos if vuelo['origen'].lower() == origen.lower()]
    if encontrados:
        for vuelo in encontrados:
            print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Dia: {vuelo['dia']}, Clase: {vuelo['clase']}")
    else:
        print("No se encontraron vuelos desde ese origen.")
# Imprime el vuelo correspondiente al origen y destino introducido por usuario
def imprimir_vuelo(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    destino = input("Introduce el destino del vuelo: ")
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower() and vuelo['destino'].lower() == destino.lower():
            print(f"Origen: {vuelo['origen']}, Destino: {vuelo['destino']}, Dia: {vuelo['dia']}, Clase: {vuelo['clase']}")
            return
    print("No se encontro el vuelo.")
# Cambia la fecha de un vuelo existente
def cambiar_fecha(vuelos):
    origen = input("Introduce el origen del vuelo: ")
    destino = input("Introduce el destino del vuelo: ")
    for vuelo in vuelos:
        if vuelo['origen'].lower() == origen.lower() and vuelo['destino'].lower() == destino.lower():
            nueva_fecha = input("Introduce la nueva fecha: ")
            vuelo['dia'] = nueva_fecha
            print(f"La fecha del vuelo de {origen} a {destino} ha sido cambiada a {nueva_fecha}.")
            return
    print("No se encontro el vuelo.")
# Muestra el menu y sus opciones
def menu():
    while True:
        print("\nMenu:")
        print("1. Imprimir todos los vuelos")
        print("2. Buscar por origen")
        print("3. Imprimir vuelo especifico")
        print("4. Cambiar fecha de vuelo")
        print("0. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == '1':
            imprimir(vuelos)
        elif opcion == '2':
            buscar_origen(vuelos)
        elif opcion == '3':
            imprimir_vuelo(vuelos)
        elif opcion == '4':
            cambiar_fecha(vuelos)
        elif opcion == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opcion no valida, por favor intenta de nuevo.")

# Ejecuta el menu al iniciar
if __name__ == "__main__":
    menu()
