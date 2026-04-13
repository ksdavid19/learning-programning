while True:
    opcion = input("CALCULADORAV3\n1. suma \n2. resta\n3. multiplicacion\n4. division\n5. todas las operaciones\n6. promedio\nElija una opcion: ")
    num1 = float(input("Ingrese num1: "))
    num2 = float(input("Ingrese num2: "))
    if opcion == "1":
        print("La suma es: ", num1 + num2)
    elif opcion == "2":
        print("La resta es: ", num1 - num2)
    elif opcion == "3":
        print("La multiplicacion es: ", num1 * num2)
    elif opcion == "4":
        if num2 != 0:
            print("La division es: ", num1 / num2)
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == "5":
        print("La suma es: ", num1 + num2)
        print("La resta es: ", num1 - num2)
        print("La multiplicacion es: ", num1 * num2)
        if num2 != 0:
            print("La division es: ", num1 / num2)
        else:
            print("Error: No se puede dividir por cero.")
    elif opcion == "6":
        print("El promedio es: ", (num1 + num2) / 2)
    else:
        print("Opcion no valida. Por favor, elija una opcion del 1 al 6.")
         if continuar.lower() != 's':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
     
