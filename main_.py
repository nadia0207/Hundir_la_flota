import random
#from funciones import crea_tablero
import funciones

def iniciar_juego():
    '''
    Inicializa el juego creando y preparando los tableros del jugador y del ordenador.

    Crea un tablero vacío de 15x15 y genera dos tableros independientes con los
    barcos colocados aleatoriamente: uno para el jugador y otro para el ordenador.

    Returns:
        tuple: Tupla con tres elementos en el siguiente orden:
            - tablero_juego (numpy.ndarray): Tablero vacío base de 15x15.
            - tablero_jugador (numpy.ndarray): Tablero del jugador con los barcos colocados.
            - tablero_ordenador (numpy.ndarray): Tablero del ordenador con los barcos colocados.
    '''

    tablero_juego = funciones.crea_tablero(10)
    tablero_jugador = funciones.colocar_todos_barcos_en_tablero(tablero_juego) 
    tablero_ordenador = funciones.colocar_todos_barcos_en_tablero(tablero_juego)
    
    return tablero_juego,tablero_jugador,tablero_ordenador
