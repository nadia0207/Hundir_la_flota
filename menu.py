import main_
import funciones

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
    print("  Ingresa las coordenadas (fila.columna)")
    print("="*40)
    print("1- Ver tablero de jugador")
    print("2- Salir")
    print("3- Ver tablero del ordenador")
    print("4- Ver coordenada de barcos del ordenador")
    print("="*40)
    opcion = input("Ingresa las coordenadas (fila.columna) o elije opciones: ")
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
            resultado = main_.iniciar_juego()
            tablero_juego = resultado[0]
            tablero_jugador = resultado[1]
            tablero_ordenador = resultado[2]
            funciones.ver_tablero_jugador(tablero_jugador)
            funciones.ver_tablero_ordenador(tablero_ordenador)


            while True:
                opcion_juego = menu_juego()
            
                if opcion_juego == "1":
                    funciones.ver_tablero_jugador(tablero_jugador)
                    
                elif opcion_juego == "2":
                    print("\nSaliendo del juego...👋 ¡Hasta luego!")
                    break
                    
                elif opcion_juego == "3":
                    funciones.ver_tablero_ordenador(tablero_ordenador)
                
                elif opcion_juego == "4":
                    print(funciones.muestra_coordenadas_barcos_O(tablero_ordenador))
                    
                else:
                    funciones.recibir_disparo(tablero_ordenador,funciones.recibir_coordenada_jugador(tablero_juego,opcion_juego),"jugador") #disparo del jugador hacia tablero del ordenador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador
                    funciones.recibir_disparo(tablero_jugador,funciones.generar_coordenada_aleatoria(tablero_juego),"ordenador") #disparo del ordenador hacia tablero de jugador


                    #verifica si tablero tiene barcos con "O"
                    if funciones.tablero_tiene_barcos_o(tablero_ordenador) == False:
                        print("\n 🎉🎉  Ganaste!!!!! ......")
                        break
                    if funciones.tablero_tiene_barcos_o(tablero_ordenador) == False:
                        print("\n 💀💀 Perdiste!!!!!.......")
                        break
                        
                      
        elif opcion == "2":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n⚠️ Opción no válida, intenta de nuevo")
        
# Ejecutar el juego
#tablero_juego = funciones.crea_tablero(15)
ejecutar_juego()
