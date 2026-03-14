

def menu_principal():
    '''
    Muestra el menú principal del juego.

    Returns:
        str: Opción elegida por el usuario.
    '''
    print("\n" + "="*40)
    print("Bienvenido al juego de hundir la flota")
    print("="*40)
    print("1- Iniciar jugada")
    print("2- Salir")
    print("="*40)

    Opcion = input("Selecciona una opcion: ")
    return Opcion



def menu_juego():
    '''
    Muestra el menú durante la partida.
    
    Returns:
        str: Opción elegida por el usuario.
    '''
    print("\n" + "="*40)
    print("  Ingresa las coordenadas *(fila,columna): ")
    print("="*40)
    print("1- Ver tablero de jugador")
    print("2- Salir")
    print("3- Ver tablero de ordenador")
    print("="*40)
    opcion = input("Selecciona una opción: ")
    return opcion


def ejecutar_juego():
    '''
    Controla los menus del juego
    '''
    
    while True:
        opcion = menu_principal()

        if opcion == "1":

            print("\n¡Iniciando partida 🎮 a jugar...!")
            #Aqui ira la logica del juego
            


            while True:
                opcion_juego = menu_juego()

                if opcion_juego == "1":
                     print("\nTablero del jugador:")
                    # print(tablero_jugador)
                    
                elif opcion_juego == "2":
                    print("\nSaliendo del juego...👋 ¡Hasta luego!")
                    break
                    
                elif opcion_juego == "3":
                    print("\nTablero del ordenador:")
                    # print(tablero_ordenador)
                else:
                    print("\n⚠️ Opción no válida, intenta de nuevo")
        
        elif opcion == "2":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n⚠️ Opción no válida, intenta de nuevo")
        
# Ejecutar el juego
tablero_juego = funciones.crea_tablero(15)
ejecutar_juego()
