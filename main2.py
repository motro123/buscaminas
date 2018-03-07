from celda import celda
import random
import sys
from timer import Timer

# Declaración de variables

# Cadena usada para convertir a lista, y traducir y dar nombre a cada celda
from pip._vendor.requests.packages.chardet.langcyrillicmodel import MacCyrillicModel

posibles = "ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&"
# Declaración de la matriz en la que almacenamos objetos de la clase celda
#Matriz = [[celda("", "", False) for x in range(0, 30)] for y in range(0, 30)]
Matriz = []
# Lista en la que irán los numeros de celda en los que hay bomba
numeros = []
fi = 0
co = 0
bo = 0
# Caracteres dados para dibujar el tablero
COE = u'\u2500'  # ─
CNS = u'\u2502'  # │
CES = u'\u250C'  # ┌
CSO = u'\u2510'  # ┐
CNE = u'\u2514'  # └
CON = u'\u2518'  # ┘
COES = u'\u252C'  # ┬
CNES = u'\u251C'  # ├
CONS = u'\u2524'  # ┤
CONE = u'\u2534'  # ┴
CSOM = u'\u2593'  # ▒

# Cadenas de los caracteres dados con los que hacemos las diferentes tres lineas de cada celda, diferenciando
# entre la primera fila de celdas, las pares, las impares y la ultima fila
cTIn0 = "  " + CES + COE + COE + COE + COES
cTC0 = COE + COE + COE + COES
cTFi0 = COE + COE + COE + CSO
cCIn0 = "  " + CNS + " " + " " + " " + CNS
cCC0 = " " + " " + " " + CNS
cBIn0 = CES + COE + CONE + COE + COES + COE + CONE
cBC0 = COE + COES + COE + CONE
cBFi0 = COE + COES + COE + CON
cCIn1 = CNS + " " + " " + " " + CNS
# cCC0 =  " " + " " + " " + CNS
cBIn2 = "  " + CES + COE + CONE + COE + COES + COE + CONE
cBIn1 = CNE + COE + COES + COE + CONE
cBC = COE + COE + COE + CONE
cBCF = COE + COE + COE + CON
cBIn2 = CNE + COE + COE + COE + CONE
cSup = CES + COE * 25 + CSO
cInf = CNE + COE * 25 + CON


# funcion para mostrar el tablero
def imprimemenu():
    print(cSup)
    print(CNS + " " + "BUSCAMINAS" + "              " + CNS)
    print(CNS + " " + "----------------------- " + CNS)
    print(CNS + " " + "1. Principiante" + " (9×9)   " + CNS)
    print(CNS + " " + "2. Intermedio" + " (16×16)   " + CNS)
    print(CNS + " " + "3. Experto" + " (16×30)      " + CNS)
    print(CNS + " " + "4. Leer de fichero" + "      " + CNS)
    print(CNS + " " + "5. Salir " + "               " + CNS)
    print(CNS + "                         " + CNS)
    print(CNS + " Escoja opcion:          " + CNS)

    print(cInf)


def seledificultad():
    imprimemenu()
    sele = input()

    while (int(sele) > 5 or int(sele) < 1):
        print("Numero erroneo, vuelva a intentarlo")
        sele = input()

    if int(sele) == 1:  # n es el numero de filas, FALTA TENER EN CUENTA COLUMNAS !!!
        global fi
        global co
        global bo
        fi = 9
        co = 9
        bo = 10
        nuevaPartida(fi, co , bo)

    else:
        if int(sele) == 2:
            nuevaPartida(16,16,40)
            numbombas = 40
        else:
            if int(sele) == 3:
                fi = 16
                co = 30
                bo = 99
                nuevaPartida(co, fi, bo)  # Anchura 30

            else:
                if int(sele) == 4:  # importar archivo
                    n = 123
                else:
                    if int(sele) == 5:
                        print("Fin del Juego")
                        sys.exit(0)


#################
# Función que inicializa una nueva partida, pasandole un parámetro para darle la dimension i*i adecuada. Siendo i mayor
# que 1
# @param i El tipo esperado es int
#################
def nuevaPartida(i, j, b):
    global Matriz
    global numeros
    global tim
    numeros = [None] * b
    Matriz = [[celda("", "", False) for x in range(0, i)] for y in range(0, j)]
    tim = Timer()
    tim.start()
    crearMatriz(i,j,b)
    salidaTablero()
    generarAdyacentes()
    #seledificultad()



#####################
# Función para dibujar el tablero
# @param n, y numero de filas y de columnas respectivamente
#####################

def salidaTablero():
    tableroFilaInicial(co)
    tableroFila(co,fi)
    ultimaFila(co)
    print("Tiempo transcurrido: " + str(tim.elapsed()) + " segundos" )


#####################
# Función que dibuja con los caracteres dados la primera fila de celdas, con numero de celdas n.
#
# @param n numero de celdas que tiene la fila, tipo esperado int.
####################

def tableroFilaInicial(n):
    suma0 = cTIn0

    suma2 = cBIn0
    for i in range(0, n - 2):
        if i == 0:
            cCC0 = "  "+ CNS+" " + Matriz[0][i].n1 + Matriz[0][i + 1].n2 + CNS
            suma1 = cCC0
        cCC0 = " " + Matriz[0][i].n1 + Matriz[0][i + 1].n2 + CNS
        suma0 = suma0 + cTC0
        suma1 = suma1 + cCC0
        suma2 = suma2 + cBC0
    suma0 = suma0 + cTFi0
    suma1 = suma1 + cCC0
    suma2 = suma2 + cBFi0

    print(suma0)
    print(suma1)
    print(suma2)


#####################
# Función que dibuja con los caracteres dados una fila central del tablero, con numero de celdas n. Diferenciamos entre
# fila par e impar, ya que las filas impares estan desfasadas respecto a las demás.
#
# @param n numero de celdas que tiene la fila, tipo esperado int.
####################


def tableroFila(n,y):
    par = 1
    for j in range(0, y - 2):

        suma2 = cBIn1


        if par == 1:

            for i in range(0, n - 2):
                if i ==0:
                    cCIn1 = CNS + " " + Matriz[j+1][i].n1 + Matriz[j+1][i].n2 + CNS
                    suma1 = cCIn1

                cCC0 = " " + Matriz[j+1][i].n1 + Matriz[j+1][i+1].n2+ CNS
                suma1 = suma1 + cCC0
                suma2 = suma2 + cBC0
            suma1 = suma1 + cCC0
            suma2 = suma2 + cBC0 + COE + CSO

            # print(suma0)
            print(suma1)
            print(suma2)
            par = 0


        elif par == 0:
            suma2 = cBIn0
            for i in range(0, n - 2):
                if i ==0:
                    cCIn1 = "  "+CNS + " " + Matriz[j+1][i].n1 + Matriz[j+1][i].n2 + CNS
                    suma1 = cCIn1
                cCC0 = " " + Matriz[j + 1][i].n1 + Matriz[j + 1][i+1].n2 + CNS
                # suma0 = suma0 + cTC0
                suma1 = suma1 + cCC0
                suma2 = suma2 + cBC0
            # suma0 = suma0 + cTFi0
            suma1 = suma1 + cCC0
            suma2 = suma2 + cBFi0

            # print(suma0)
            print(suma1)
            print(suma2)
            par = 1


#####################
# Función que dibuja con los caracteres dados la ultima fila de celdas, con numero de celdas n.
#
# @param n numero de celdas que tiene la fila, tipo esperado int.
####################


def ultimaFila(n):
    if n % 2 == 0:

        suma2 = cBIn2
        for i in range(0, n - 2):
            # suma0 = suma0 + cTC0

            if i == 0:
                cCIn1 = CNS + " " + Matriz[len(Matriz)-1][i].n1 + Matriz[len(Matriz)-1][i + 1].n2 + CNS
                suma1 = cCIn1
            cCC0 = " " + Matriz[len(Matriz)-1][i].n1 + Matriz[len(Matriz)-1][i + 1].n2 + CNS
            suma1 = suma1 + cCC0
            suma2 = suma2 + cBC
            # suma0 = suma0 + cTFi0
        suma1 = suma1 + cCC0
        suma2 = suma2 + cBCF

        # print(suma0)
        print(suma1)
        print(suma2)

    elif n % 2 != 0:

        suma2 = "  " + cBIn2
        for i in range(0, n - 2):
            if i == 0:
                cCIn1 = "  " +CNS + " " + Matriz[len(Matriz)-1][i].n1 + Matriz[len(Matriz)-1][i].n2 + CNS
                suma1 = cCIn1
            cCC0 = " " + Matriz[len(Matriz)-1][i].n1 + Matriz[len(Matriz)-1][i + 1].n2 + CNS
            # suma0 = suma0 + cTC0
            suma1 = suma1 + cCC0
            suma2 = suma2 + cBC
            # suma0 = suma0 + cTFi0
        suma1 = suma1 + cCC0
        suma2 = suma2 + cBCF

        # print(suma0)
        print(suma1)
        print(suma2)


#####################
# Función que genera una matriz de dos dimensiones n*n de Celdas sobre la variable Matriz del programa y genera diez
# números aleatorios entre 0 y k siendo k=n*n sobre la variable lista numeros, para indicar en que casillas estan las
# bombas. Con esos datos, al generar la matriz se da a las celdas nombre de columna, nombre de fila, y si tiene o no bomba
#
# @param n da a la matriz la longitud n*n necesaria.
####################

def crearMatriz(x, y, b):
    # Matriz = [[0 for x in range(0, n - 1)] for y in range(0, n - 1)]
    # Crea numeros aleatorios para identificar en que celdas estan las bombas, si el numero ya ha sido previamene elegido
    # lo cambia
    #print(x)
    #print(y)
    for i in range(0, b):
        rand = random.randrange(x*y)
        while rand in numeros:
            rand = random.randrange(x*y)
            if rand not in numeros:
                numeros[i] = rand
                break

        numeros[i] = rand
        #print(str(numeros[i]))
    for j in range(0, y):
        for i in range(0, x):
            bool = False
            if (j + 1) * (i + 1) in numeros:
                bool = True
            #print("x es " +str(j))
            #print(" y es " +str(i))
            Matriz[j][i] = celda(posibles[j], posibles[i], bool)


################
# FUNCIÓN QUE AÑADE UNA LISTA DE 6 CELDAS ADYACENTES EN EL ATRIBUTO ADYACENTES DE CADA OBJETO CELDA, SI LA CELDA ESTUVIESE
# EN UN BORDE O ESQUINA, SOLO SE AÑADIRIAN LAS CORRESPONDIENTES A LAS CASILLAS EXISTENTES
################

def generarAdyacentes():
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):

            # COMPROBACIÓN DE ADYACENTES PARA LAS CASILLAS DE COLUMNAS PARES
            #print("i es " + str(i))
            #print("j es " + str(j))
            if (i + 1) % 2 == 0:

                if i - 1 < 0 and j - 1 < 0:
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[4] = Matriz[i + 1][j]
                    Matriz[i][j].adyacentes[5] = Matriz[i + 1][j + 1]
                elif i - 1 < 0 and j + 1 <= len(Matriz) - 1:
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[4] = Matriz[i + 1][j]
                    #Matriz[i][j].adyacentes[5] = Matriz[i -1][j + 1]
                elif j - 1 < 0 and i + 1 <= len(Matriz) - 1:
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                elif i + 1 > len(Matriz) and j + 1 > len(Matriz) - 1:
                    Matriz[i][j].adyacentes[0] = Matriz[i - 1][j]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                elif i + 1 > len(Matriz) and j >= 0:
                    Matriz[i][j].adyacentes[0] = Matriz[i - 1][j]
                    Matriz[i][j].adyacentes[1] = Matriz[i - 1][j + 1]
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]

                elif j + 1 > len(Matriz) and i >= 0:
                    Matriz[i][j].adyacentes[0] = Matriz[i - 1][j - 1]
                    Matriz[i][j].adyacentes[1] = Matriz[i - 1][j]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    #Matriz[i][j].adyacentes[4] = Matriz[i + 1][j]

                elif i - 1 >= 0 and i + 1 <= len(Matriz) - 1 and j - 1 >= 0 and j + 1 <= len(Matriz) - 1:
                    Matriz[i][j].adyacentes[0] = Matriz[i - 1][j - 1]
                    Matriz[i][j].adyacentes[1] = Matriz[i - 1][j]
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[4] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[5] = Matriz[i - 1][j + 1]


            # COMPROBACIÓN DE ADYACENTES PARA LAS CASILLAS DE COLUMNAS IMPARES, QUE CUMPLEN CONDICIONES DISTINTAS A LA
            # HORA DE ELEGIR QUE CASILLAS LE RODEAN

            elif (i + 1) % 2 != 0:

                if i - 1 < 0 and j - 1 < 0:

                    Matriz[i][j].adyacentes[2] = Matriz[i+1][j]
                    Matriz[i][j].adyacentes[4] = Matriz[i + 1][j + 1]
                    Matriz[i][j].adyacentes[5] = Matriz[i][j + 1]

                elif i - 1 < 0 and j + 1 <= len(Matriz) - 1 and (j+1) % 2 == 0:
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[4] = Matriz[i + 1][j]
                   # Matriz[i][j].adyacentes[5] = Matriz[i][j + 1]

                elif i - 1 < 0 and j + 1 <= len(Matriz) - 1 and (j+1) % 2 != 0:
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[4] = Matriz[i + 1][j]
                    Matriz[i][j].adyacentes[5] = Matriz[i][j + 1]

                elif j - 1 < 0 and i + 1 <= len(Matriz) - 1:
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]

                elif i + 1 > len(Matriz) and j + 1 > len(Matriz) - 1:
                    Matriz[i][j].adyacentes[0] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]

                elif i + 1 > len(Matriz) and j >= 0:
                    Matriz[i][j].adyacentes[0] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[1] = Matriz[i + 1][i - 1]
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]

                elif j + 1 > len(Matriz) and i >= 0:
                    Matriz[i][j].adyacentes[0] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[1] = Matriz[i + 1][j - 1]
                    #Matriz[i][j].adyacentes[4] = Matriz[i + 1][j + 1]

                elif i - 1 >= 0 and i + 1 <= len(Matriz) - 1 and j - 1 >= 0 and j + 1 <= len(Matriz) - 1:
                    Matriz[i][j].adyacentes[0] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[1] = Matriz[i + 1][j - 1]
                    Matriz[i][j].adyacentes[2] = Matriz[i][j + 1]
                    Matriz[i][j].adyacentes[3] = Matriz[i][j - 1]
                    Matriz[i][j].adyacentes[4] = Matriz[i + 1][j + 1]
                    Matriz[i][j].adyacentes[5] = Matriz[i][j + 1]

            # COMPRUEBA SI LAS CELDAS ADYACENTES TIENEN BOMBA, Y CAMBIAN EL ATRIBUTO NADY DE CADA OBJETO CELDA.
            for r in Matriz[i][j].adyacentes:
                if isinstance(r, celda) and r.bomba:
                    Matriz[i][j].nady = Matriz[i][j].nady + 1
                    #print("añadida bomba, ahora hay: " + str(Matriz[i][j].nady))





def main():
    seledificultad()

if __name__ == "__main__":
    main()
