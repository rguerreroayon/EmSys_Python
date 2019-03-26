import math

class Alumno:
    def __init__(self,calificacion):
        self.calificacion = calificacion


def leeCalifs():
    alumnos = int(input("Ingrese el numero de alumnos: "))
    contador = int(1)
    listaAlumnos = []

    while(contador <= alumnos):
        calificacion = int(input("Ingrese la calificacion del alumno "+str(contador)+":"))
        listaAlumnos.append(Alumno(calificacion))
        contador = contador + 1
    

    return listaAlumnos



def mediaDesvest(listaAlumnos):
    sumaC = 0
    
    for alumno in listaAlumnos:
        sumaC = sumaC + alumno.calificacion

    media = sumaC / len(listaAlumnos)

    sumaDesviacion = 0

    for alumno in listaAlumnos:
        sumaDesviacion = sumaDesviacion + pow(alumno.calificacion)

    desviacion = math.sqrt(sumaDesviacion / len(listaAlumnos) - pow(media))

    return (media,desviacion)
    
def generaCalifLetra(listaAlumnos):
    