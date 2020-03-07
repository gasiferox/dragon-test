# este programa te saluda y adivina un número de 1 a 20 indicando si se esta por arriba o por abajo

from random import randint, uniform, random
#import random

print('Hola Jugador, como es tu nombre?')
nombreJugador1 = input()

#numeroAdivinar = random.randint(1, 20)
numeroAdivinar = randint(1, 20)
intentos = 0

while intentos <= 6:
    print("Listo, " + nombreJugador1 + " estoy pensando un número entre 1 a 20. \nIntenta adivinar")
    numeroJugador1 = input()
    numeroJugador1 = int(numeroJugador1)

    intentos += 1

    if numeroJugador1 < numeroAdivinar:
        print ('Tu número está por debajo del número a adivinar.')
    if numeroJugador1 > numeroAdivinar:
        print ('Tu número está por encima del número a adivinar.')
    if numeroJugador1 == numeroAdivinar:
        break

if numeroJugador1 == numeroAdivinar:
    intentos = str(intentos)
    print("Buen trabajo " + nombreJugador1 +", has adivinado mi número en " + intentos + " intentos.")

if numeroJugador1 != numeroAdivinar:
    numeroAdivinar = str(numeroAdivinar)
    print("Lo siento, estas salad@, has perdido, el número a adivinar era " + numeroAdivinar)