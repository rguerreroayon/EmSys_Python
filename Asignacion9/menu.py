from scipy import random
import numpy as np
import matplotlib.pyplot as plt


def menu():
        valor = True
        while(valor):
                print('I - Integrar')
                print('T - Tabular')
                print('S - Salir')

                opcion = input('Elegir la opción deseada: ')

                if(opcion == 'i' or opcion == 'I'):
                        integrar(leerDatosIntegracion())
                elif(opcion == 't' or opcion == 'T'):
                        tabular(leerDatosTabulacion())
                elif(opcion == 's' or opcion == 'S'):
                        valor = False
                        salir()
                        exit()
        
      
        
def salir():
        print('Gracias')
        return False


def leerDatosIntegracion():
        print('Datos de Integración')
        inicial = int(input('Valor Inicial: '))
        final = int(input('Valor Final: '))
        numeroRec = int(input("Número de Rectangulos: "))

        return (inicial,final,numeroRec)

def leerDatosTabulacion():
        print('Datos de Tabulación')
        inicial = int(input('Valor Inicial: '))
        final = int(input('Valor Final: '))
        incr = int(input("Número Incremental: "))

        return (inicial,final,incr)

def funcion(valor):
        return float(((valor**3)-(2*valor)+3))


def integrar(datosIntegracion):
        a = datosIntegracion[0]
        b = datosIntegracion[1]
        N = datosIntegracion[2]
        xrand = random.uniform(a,b,N)

        integral = 0.0

        for i in range(N):
                integral+= funcion(xrand[i])

        respuesta = (b-a)/ float(N) * integral
        print('La integral de '+str(a)+' a '+str(b)+' de x^(3)-2x+3 es: '+str(respuesta))


def tabular(datosTabulacion):
        a = datosTabulacion[0]
        b = datosTabulacion[1]
        I = datosTabulacion[2]
        areas = []
        
        for i in range(I):
                xrand = np.zeros(I)

                for i in range(len(xrand)):
                        xrand[i] = random.uniform(a,b)
                        integral = 0.0
                for i in range(I):
                        integral += funcion(xrand[i])

                respuesta = (b-a)/float(I) * integral
                areas.append(respuesta)
        
        plt.title('Tabulacion de rectangulos')
        plt.hist(areas,bins=30,ec ='black')
        plt.xlabel('Areas')
                




menu()