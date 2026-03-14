import random
#from funciones import crea_tablero
import funciones

def iniciar_juego():
    tablero_juego = funciones.crea_tablero(15)
    tablero_jugador = funciones.colocar_todos_barcos_en_tablero(tablero_juego) 
    tablero_ordenador = funciones.colocar_todos_barcos_en_tablero(tablero_juego)
    return tablero_juego,tablero_jugador,tablero_ordenador


def ver_tablero_jugador(tablero):
    print("\n" + "="*80)
    print(" 🔢 Tablero del jugador ")
    print("="*40)
    print(tablero)

def ver_tablero_ordenador(tablero):
    print("\n" + "="*80)
    print(" 🔢 Tablero del Ordenador ")
    print("="*40)
    print(tablero)

'''    
recibir_disparo(tablero_jugador,generar_coordenada_aleatoria(tablero_juego)) #disparo del ordenador hacia tablero de jugador

print(tablero_jugador)

recibir_disparo(tablero_ordenador,recibir_coordenada_jugador(tablero_juego,"5.5")) #disparo del jugador hacia tablero del ordenador

print(tablero_ordenador)'''


#tablero_juego = crea_tablero(15)

#coordenada_jugador = recibir_coordenada_jugador(tablero_juego,"7.8")
#print(coordenada_jugador)
