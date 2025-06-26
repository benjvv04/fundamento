usuarios = {}  # Diccionario para almacenar los usuarios

def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    
    if nombre in usuarios:
        print("El usuario ya existe.")
        return

    sexo = input("Ingrese sexo (M/F): ").upper()
    if sexo not in ["M", "F"]:
        print("Sexo inválido. Debe ser 'M' o 'F'.")
        return

    contraseña = input("Ingrese contraseña: ")

    # Agregar usuario al diccionario
    usuarios[nombre] = {
        "sexo": sexo,
        "contraseña": contraseña
    }
    print(f"Usuario '{nombre}' ingresado correctamente.")

def buscar_usuario():
    nombre = input("Ingrese el nombre del usuario a buscar: ")
    if nombre in usuarios:
        datos = usuarios[nombre]
        print(f"Usuario encontrado: {nombre} - Sexo: {datos['sexo']}")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print(f"Usuario '{nombre}' eliminado correctamente.")
    else:
        print("Usuario no encontrado.")

def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Saliste del programa.")
            break
        else:
            print("Debe ingresar una opción válida (1-4).")

# Iniciar el programa
mostrar_menu()




