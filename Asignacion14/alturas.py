import statistics as stats

def leerDatos():
    index = 0
    resultado = list()
    while(index != -1):
        matricula = int(input("Ingrese la matricula del alumno: "))
        if matricula == 0:
            index = -1
            break
        else:
            altura = float(input("Ingrese la altura del alumno: "))
            preresultado = (matricula, altura)
            resultado.insert(index, preresultado)
            index = index + 1
    return resultado

def desplegaDatos(lista):
    print("Matricula / Altura")
    for matricula, altura in lista:
        print("Matricula: "+str(matricula)+", Altura: "+str(altura))

def ordSeleccion(lista):
    for i in range(len(lista) - 1, 0, -1):
        posMayor = 0
        for j in range(1, i + 1):
            if menorMatricula(lista, j, posMayor):
                posMayor = j
        if posMayor != i:
            temp = lista[i]
            lista[i] = lista[posMayor]
            lista[posMayor] = temp
    return lista

menorMatricula = lambda lista, index, posMayor : True if lista[index] < lista[posMayor] else False

menorAltura = lambda alumno1, alumno2 : True if alumno1 < alumno2 else False

def rango(lista):
  maximo = max(lista)
  minimo = min(lista)
  
  print("El maximo es: ", maximo)
  print("el minimo es: ", minimo)




def mediaDesvEst(lista):
     print (stats.mean(lista))
     print(stats.pstdev(lista))

def altos(lista, mediaDesvEst):
    return None

def secuencial(lista, matricula):
    for i in lista:
        if i[0]== matricula:
            return i[1]
    return 0

def main():
    datos = leerDatos()
    
    print(desplegaDatos(datos))
    print(ordSeleccion(datos))
    print(rango(datos))
    print(mediaDesvEst(datos))

main()    
    
