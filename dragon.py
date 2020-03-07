# Este es el juego del dragón, donde se va a escoger a que cueva entrar, una buena y otra mala

import random
import time

def mostrarIntroduccion():
    print('Estas en una tierra llena de dragones.  Frente a ti ')
    print('hay dos cuevas.  En una de ellas, el dragón es generoso y ')
    print('amigable y compartirá su tesoro contigo.  El otro dragón ')
    print('es codicioso y esta hambriento, y te devolverá inmediatamente.')
    print()

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('A que cueva te quieres meter? (1 ó 2)')
        cueva = input()

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡Un gran dragón aparece súbitamente frente a tí!  Abre sus fauces y...')
    print()
    time.sleep(2)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida == str(cuevaAmigable):
        print('Te regala su tesoro!')
    else:
        print('¡Te engulle de un solo bocado!')

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's'

    mostrarIntroduccion()

    numeroDeCueva = elegirCueva()

    explorarCueva(numeroDeCueva)

    print('¿Quieres jugar de nuevo? (Sí o No)')
    jugarDeNuevo = input()