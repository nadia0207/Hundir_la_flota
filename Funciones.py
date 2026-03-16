
import numpy as np
import random

def crea_tablero(lado=15):
    '''
    Crea un tablero vacío como matriz cuadrada.

    Args:
        lado (int): Tamaño del lado del tablero. Por defecto 10.

    Returns:
        numpy.ndarray: Matriz cuadrada de dimensiones (lado x lado) rellena de espacios.

    Raises:
        ValueError: Si lado no es un entero.
    '''
    if type(lado) != int:
        raise ValueError("El numero ingresado no es un entero")
    
    tablero = np.full((lado, lado), " ")
    return tablero

#*********************************************************************************************

def coloca_barco_plus(tablero, barco):
    '''
    Intenta colocar un barco en el tablero validando que no se salga ni colisione.
 
    Args:
        tablero (numpy.ndarray): Tablero actual donde se quiere colocar el barco.
        barco (list): Lista de tuplas (fila, columna) que representan las piezas del barco.
                      Ejemplo: [(3,5), (3,4), (3,3), (3,2)]
 
    Returns:
        numpy.ndarray: Copia del tablero con el barco colocado si es posible.
        bool: False si alguna pieza se sale del tablero o colisiona con otro barco.
    '''
    tablero_temp = tablero.copy() #copia el numpy.ndarray del tablero

    num_max_filas = tablero.shape[0]  #numero de filas del tablero = 15
    num_max_columnas = tablero.shape[1] #numero de columnas del tablero =15
    
    for pieza in barco: #barco = [(3,5),(3,4),(3,3),(3,2)]
        fila = pieza[0] #3
        columna = pieza[1] #5
        if fila < 0  or fila >= num_max_filas: # 3 < 0 or 3 >= 15 
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas: # 5 < 0 or 5 >= 15 
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X": # tablero[3,5]
            #print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp


#*****************************************************************************************************

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
    '''
    Genera y coloca un barco en una posición y orientación aleatoria del tablero.
 
    El proceso se repite hasta encontrar una posición válida donde el barco
    no se salga del tablero ni colisione con otros barcos.
 
    Args:
        tablero (numpy.ndarray): Tablero donde se colocará el barco.
        eslora (int): Número de piezas que tiene el barco. Por defecto 4.
        num_intentos (int): Parámetro reservado para uso futuro. Por defecto 100.
 
    Returns:
        numpy.ndarray: Tablero con el nuevo barco colocado.
    '''

    num_max_filas = tablero.shape[0] #numero maximo filas = 15
    num_max_columnas = tablero.shape[1] #numero maximo columnas = 15

    while True:
        barco = []
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1)) #(randon.randint(0,15),randon.randint(0,15)
        #print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"]) #ramdon choice, elige un aleatorio de la lista
        #print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero, barco) #barco = [(3,5),(3,4),(3,3),(3,2)]
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        #print("Tengo que intentar colocar otro barco")

#*******************************************************************************************************

def colocar_todos_barcos_en_tablero(tablero, esloras = [4,3,3,2,2,2]):
    ''' 
    Coloca todos los barcos en el tablero.

    Args:
        tablero (numpy.ndarray): Tablero vacío donde se colocarán los barcos.
        esloras (list): Lista con el tamaño de cada barco. Por defecto [4, 3, 3, 2, 2, 2].

    Returns:
        numpy.ndarray: Tablero con todos los barcos colocados. 
    '''
    tablero_actual = tablero.copy()

    for eslora in esloras:
        tablero_actual = crea_barco_aleatorio(tablero_actual,eslora)

    return tablero_actual

#*****************************************************************************************************
  
def generar_coordenada_aleatoria(tablero):
    '''
    Genera una coordenada aleatoria válida dentro del tablero para el ordenador.
    
    Args:
        tablero (numpy.ndarray): Tablero sobre el que se generará la coordenada.
        
    Returns:
        Tupla (fila, columna) con valores aleatorios dentro de los límites del tablero.
    '''
    num_max_filas = tablero.shape[0] #numero maximo filas = 15
    num_max_columnas = tablero.shape[1] #numero maximo columnas = 15

    coordenada_aleatoria = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1)) #(randon.randint(0,15),randon.randint(0,15)
    return coordenada_aleatoria   
 
#*****************************************************************************************************
def recibir_coordenada_jugador(tablero,coordenada):
    '''
    Valida y convierte la coordenada introducida por el jugador en una tupla utilizable.
 
    La coordenada se introduce como cadena de texto con formato "fila.columna"
    (por ejemplo "3.4"), y se convierte a una tupla de enteros.
 
    Args:
        tablero (numpy.ndarray): Tablero actual del juego, usado para verificar los límites.
        coordenada (str): Coordenada introducida por el jugador en formato "fila.columna".
 
    Returns:
        tuple: Tupla (fila, columna) si la coordenada está dentro del tablero.
        int: Valor del índice máximo permitido (num_max_columnas - 1) si la coordenada
             se sale de los límites del tablero.
    '''

    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    tupla = tuple(int(x.strip()) for x in coordenada.split(".")) #Split convierte a una lista[3.4] -> (3,4), strip() elimina los espacios extras
            
    if tupla[0] < num_max_filas and tupla[1]<num_max_columnas:
        return tupla
            
    if tupla[0] >= num_max_filas or tupla[1] >= num_max_columnas:
        return num_max_columnas - 1
    
#*****************************************************************************************************
def recibir_disparo(tablero, coordenada,participante):
    '''
    Procesa un disparo sobre el tablero y actualiza su estado según el resultado.
 
    Comprueba si la coordenada impacta un barco ("O"), ya fue disparada ("X"),
    o es agua ("-"). Muestra un mensaje en pantalla indicando el resultado.
 
    Args:
        tablero (numpy.ndarray): Tablero que recibe el disparo.
        coordenada (tuple): Tupla (fila, columna) donde se realiza el disparo.
        participante (str): Indica quién dispara, con la finalidad de mostrar texto
        con el resultado del impacto segun participante.
 
    Returns:
        bool: True si el disparo tocó un barco ("O"), False en cualquier otro caso.
    '''

    continuar_disparo = False
    print(" ")

    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        continuar_disparo = True

        if participante == "ordenador":
            print("💥💥 Fuiste Tocado......")
        else:
            print("💥💥 En hora buena tocaste......")

    elif tablero[coordenada] == "X":
        print("😩 Agonia, deja de perder el tiempo, dispara a otro sitio")

    else:
        tablero[coordenada] = "-"
        if participante == "ordenador":
            print(" 🌊🌊 Agua...Suerte!! no te dieron")
        else:
            print(" 🌊🌊 Mala suerte diste al Agua....")

    return continuar_disparo
#*****************************************************************************************************

def ver_tablero_jugador(tablero):
    '''
    Muestra por pantalla el tablero del jugador con un encabezado decorativo.
 
    Args:
        tablero (numpy.ndarray): Tablero del jugador a mostrar.
 
    Returns:
        None
    '''
    print("\n" + "="*60)
    print(" 🔢 Tablero del jugador ")
    print("="*60)
    print(tablero)

#*****************************************************************************************************

def ver_tablero_ordenador(tablero):
    '''
    Muestra por pantalla el tablero del ordenador con un encabezado decorativo.
 
    Args:
        tablero (numpy.ndarray): Tablero del ordenador a mostrar.
 
    Returns:
        None
    '''
    print("\n" + "="*60)
    print(" 🔢 Tablero del Ordenador ")
    print("="*60)
    print(tablero)

#*****************************************************************************************************
def tablero_tiene_barcos_o(tablero):
    '''
    Comprueba si quedan barcos sin hundir en el tablero.
 
    Recorre todas las celdas del tablero buscando al menos una con valor "O",
    que indica una pieza de barco que aún no ha sido alcanzada.
 
    Args:
        tablero (numpy.ndarray): Tablero a comprobar.
 
    Returns:
        bool: True si existe al menos una pieza de barco ("O") en el tablero,
              False si todos los barcos han sido hundidos.
    '''

    for fila in range(tablero.shape[0]):
        for columna in range(tablero.shape[1]):
            if tablero[fila,columna] == "O":
                return True
    return False          


#*****************************************************************************************************
def muestra_coordenadas_barcos_O(tablero):
    '''
    Devuelve una lista con las coordenadas de todas las piezas de barco sin hundir.
 
    Recorre el tablero y recopila las posiciones de todas las celdas con valor "O",
    que representan piezas de barco que aún no han sido alcanzadas.
 
    Args:
        tablero (numpy.ndarray): Tablero a recorrer.
 
    Returns:
        list: Lista de tuplas (fila, columna) con las posiciones de los barcos restantes.
              Devuelve una lista vacía si no quedan barcos.
    '''
    lista = []
    for fila in range(tablero.shape[0]):
        for columna in range(tablero.shape[1]):
            if tablero[fila,columna] == "O":
                lista.append((fila,columna))
    
    return lista
#*****************************************************************************************************