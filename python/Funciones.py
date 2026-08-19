nombre = input("Ingresar un nombre: ")

nota1 = float(input("Ingresar nota 1: "))
nota2 = float(input("Ingresar nota 2: "))
nota3 = float(input("Ingresar nota 3: "))


def calcularPromedio():
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


def determinarEstado():
    promedio = calcularPromedio()

    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"


def mostrarDatos():
    promedio = calcularPromedio()
    estado = determinarEstado()

    print("\nRESULTADOS")
    print("Nombre:", nombre)
    print("Nota 1:", nota1)
    print("Nota 2:", nota2)
    print("Nota 3:", nota3)
    print("Promedio:", promedio)
    print("Estado:", estado)


mostrarDatos()
