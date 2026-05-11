import random
def salir():
    print("Gracias por jugar. ¡Hasta luego!")
    exit()

print("CARRERA NUMERICA")
print("Reglas")
print("1. El primer jugador en llegar a la meta gana.")
print("3. Si un jugador lanza dobles tres veces consecutivas, gana automáticamente.")
print("4. solo se pemite jugar entre 2 y 4 jugadores")
print("QUE LA SUERTE ESTE DE SU LADO")

while True:
    jugadores = int(input("Cantidad de jugadores (2-4): "))
    if 2 <= jugadores <= 4:
        break
    print("Ingrese entre 2 y 4 jugadores")
opcion = input("Elija el nivel deseado: \n1. nivel 1  = 20.\n2. nivel 2  = 30.\n3. nivel 3  = 50.\n4. nivel 4  = 100.")
if opcion == "1":
    meta = 20
elif opcion == "2":
    meta = 30
elif opcion == "3":
    meta = 50
else:
    meta = 100
posiciones = [0] * jugadores
dobles = [0] * jugadores
turno = 0
while True:
    if turno == jugadores:
        turno = 0
    print("\nJugador", turno + 1)
    input("Presione ENTER")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print("Dado 1:", dado1)
    print("Dado 2:", dado2)
    posiciones[turno] = posiciones[turno] + dado1 + dado2
    print("Posición:", posiciones[turno])
    if dado1 == dado2:
        dobles[turno] = dobles[turno] + 1
        print("Dobles consecutivos:", dobles[turno])
        if dobles[turno] == 3:
            print("\nJugador", turno + 1, "gana por 3 dobles consecutivos")
            salir()
    else:
        dobles[turno] = 0
    if posiciones[turno] >= meta:
        print("\nJugador", turno + 1, "ganó la carrera")
        salir()
    turno = turno + 1
