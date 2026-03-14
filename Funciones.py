
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
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero.copy()

    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]
    
    for pieza in barco: #barco = [(3,5),(3,4),(3,3),(3,2)]
        fila = pieza[0] #3
        columna = pieza[1] #5
        if fila < 0  or fila >= num_max_filas:
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            #print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            #print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp


#*****************************************************************************************************

def crea_barco_aleatorio(tablero,eslora = 4, num_intentos = 100):
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
    Crea coordenada aletoria para turno de disparo del ordenador
    
    Args:
        tablero (numpy.ndarray): Tablero del orderador 
        
    Returns:
        coordenada(tupla): Tupla generedada con 2 elemenetos
    '''
    num_max_filas = tablero.shape[0] #numero maximo filas = 15
    num_max_columnas = tablero.shape[1] #numero maximo columnas = 15

    coordenada_aleatoria = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1)) #(randon.randint(0,15),randon.randint(0,15)
    return coordenada_aleatoria   
 
#*****************************************************************************************************
def recibir_coordenada_jugador(tablero,coordenada):
    num_max_filas = tablero.shape[0]
    num_max_columnas = tablero.shape[1]

    tupla = tuple(int(x.strip()) for x in coordenada.split(".")) #Split convierte a una lista[3.4] -> (3,4), strip() elimina los espacios extras
            
    if tupla[0] < num_max_filas and tupla[1]<num_max_columnas:
        return tupla
            
    if tupla[0] >= num_max_filas or tupla[1] >= num_max_columnas:
        raise ValueError(f"⚠️  Numeros fuera del rango del tablero, maximo indicar {num_max_columnas-1}")

#*****************************************************************************************************
def recibir_disparo(tablero, coordenada,participante):
    print(" ")
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"

        if participante == "ordenador":
            print("💥💥 Fuiste Tocado......")
        else:
            print("💥💥 En hora buena tocaste......")

    elif tablero[coordenada] == "X":
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")

    else:
        tablero[coordenada] = "-"
        if participante == "ordenador":
            print(" 🌊🌊 Agua...Suerte!! no te dieron")
        else:
            print(" 🌊🌊 Mala suerte diste al Agua....")

#*****************************************************************************************************

def ver_tablero_jugador(tablero):
    print("\n" + "="*60)
    print(" 🔢 Tablero del jugador ")
    print("="*60)
    print(tablero)

#*****************************************************************************************************

def ver_tablero_ordenador(tablero):
    print("\n" + "="*60)
    print(" 🔢 Tablero del Ordenador ")
    print("="*60)
    print(tablero)

#*****************************************************************************************************
def tablero_tiene_barcos_o(tablero):
    for fila in range(tablero.shape[0]):
        for columna in range(tablero.shape[1]):
            if tablero[fila,columna] == "O":
                return True
    return False          


#*****************************************************************************************************
def muestra_coordenadas_barcos_O(tablero):
    lista = []
    for fila in range(tablero.shape[0]):
        for columna in range(tablero.shape[1]):
            if tablero[fila,columna] == "O":
                lista.append((fila,columna))
    
    return lista
#*****************************************************************************************************

#tablero_1 = np.array([["-","-","-","-"],
#                      ["-","x","X","-"],
#                      ["X","-","-","x"]])

#tablero_tiene_barcos_o(tablero_1)
#print(tablero_tiene_barcos_o(tablero_1))

#print(muestra_coordenadas_barcos(tablero_1))

#*****************************************************************************************************

