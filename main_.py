import random
#from funciones import crea_tablero
import funciones

def iniciar_juego():
    tablero_juego = funciones.crea_tablero(15)
    tablero_jugador = funciones.colocar_todos_barcos_en_tablero(tablero_juego) 
    tablero_ordenador = funciones.colocar_todos_barcos_en_tablero(tablero_juego)
    
    return tablero_juego,tablero_jugador,tablero_ordenador
