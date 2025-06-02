numeros = []

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Ingresar Numero")
    print("2. Mostrar Mayor")
    print("3. Mostrar menor")
    print("4. Salir")

while True:
    menu()
    opcion = input("ingrese una opcion: ")

    if opcion == "1":
            try:
                entrada = input("Ingrese numero entero entre 0 y 100: ")
                numero = int(entrada)
                if 0 <= numero <= 100:
                    numeros.append(numero)
                    print("Ingresado correctamente")   
                else:
                    print("Debe ingresar un numero entre 0 y 100!!")
            except ValueError:
                print("Debe ingresar un numero entero!!")
    elif opcion == "2":
        if numeros:
            print("el numero mayor ingresado es: ", max(numeros))
        else:
            print("No hay numeros ingresados")
    elif opcion == "3":
        if numeros:
            print("el numero menor ingresado es: ", min(numeros))
        else:
            print("No hay numeros ingresados")
    elif opcion == "4":
        print ("Gracias por usar el programa")
        break
    else:
        print ("opcion invalida, reintente")