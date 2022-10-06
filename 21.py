# Realizar el juego de cartas conocido como "la 21"

#input

import random
#processing
jugador=random.randint(1,10)
pc=random.randint(1,10)
#Numeros aleatorios tanto del jugador como del pc"Representando las cartas del juego"
#sum jugador
#dan pac
suma_de_puntos_repartidor=0
suma_de_puntos_Jugador=0
i=1
diferencia=suma_de_puntos_repartidor-suma_de_puntos_Jugador
while i<= 2:
    suma_de_puntos_Jugador=suma_de_puntos_Jugador+jugador
    suma_de_puntos_repartidor=suma_de_puntos_repartidor+pc
    i=i+1
print("pc",suma_de_puntos_repartidor)
print("Jugador",suma_de_puntos_Jugador)
print("¿Quieres seguir jugando?")
X=int(input("1. para seguir jugando o 2. para parar: "))
if X==1: 
    while suma_de_puntos_Jugador<=21 and X!=2:
        #este whilw lo uso para generar el bucle si el jugador seguir jugando
        d= random.randint(1,10)
        #decidí crear una variable nueva "d" para representar una nueva variable aleatoria  
        suma_de_puntos_Jugador=suma_de_puntos_Jugador +d 
        print("jugador",suma_de_puntos_Jugador)
        if suma_de_puntos_Jugador>21:
            print("volaste")
            break
        #Este break es para parar el programa si el jugador llegase a perder
        print("¿Quieres seguir jugando?")
        X=int(input("1. para seguir jugando o 2. para parar: "))
        if suma_de_puntos_Jugador>21:
            print("volaste")
            break
        elif X==2:
            while suma_de_puntos_repartidor<=suma_de_puntos_Jugador and suma_de_puntos_repartidor< 21:
                p=random.randint(1,10)
                suma_de_puntos_repartidor = suma_de_puntos_repartidor + p
                print("repartidor", suma_de_puntos_repartidor)
            if suma_de_puntos_repartidor>suma_de_puntos_Jugador and suma_de_puntos_repartidor<21:
                if suma_de_puntos_repartidor-suma_de_puntos_Jugador==1:
                    print("El repartidor gana por un punto")
                else:
                    print("gana el repartidor por" , suma_de_puntos_repartidor-suma_de_puntos_Jugador, "Puntos")
            elif suma_de_puntos_repartidor==suma_de_puntos_Jugador:
                print("gana el pc por ser el repartidor")
            if suma_de_puntos_repartidor>21:
                print("El repartidor ah volado")

elif X==2:
            while suma_de_puntos_repartidor<=suma_de_puntos_Jugador and suma_de_puntos_repartidor< 21:
                p=random.randint(1,10)
                suma_de_puntos_repartidor = suma_de_puntos_repartidor + p
                print("repartidor", suma_de_puntos_repartidor)
            if suma_de_puntos_repartidor>suma_de_puntos_Jugador and suma_de_puntos_repartidor<21:
                if suma_de_puntos_repartidor-suma_de_puntos_Jugador==1:
                    print("El repartidor gana por un punto")
                else:
                    print("gana el repartidor por" , suma_de_puntos_repartidor-suma_de_puntos_Jugador, "Puntos")
            elif suma_de_puntos_repartidor==suma_de_puntos_Jugador:
                print("gana el pc por ser el repartidor")
            if suma_de_puntos_repartidor>21:
                print("El repartidor ah volado")
        
