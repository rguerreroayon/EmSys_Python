import math


def leeEncuesta():
    alumnos = list()
    while(True):
        mat = int(
            input("Introduce la matricula del estudiante ('0' para terminar): "))
        if(mat == 0):
            break
        sexo = input("Introduce su sexo ('M'/'F'): ")
        carrera = input("Introduce las siglas de su carrera: ")
        tupla = (mat, sexo, carrera)
        alumnos.append(tupla)
    return alumnos


def clasificaAlumnosCategoria(alumnos):
    sublist = list()
    for i in range(len(alumnos)):
        subTupla = (alumnos[i][1], alumnos[i][2])
        sublist.append(subTupla)
    alumnosCategoria = dict.fromkeys(sublist, 0)
    for i in range(len(alumnos)):
        key = tuple(alumnos[i][1:3])
        if(key in alumnosCategoria):
            val = int(alumnosCategoria.get(key))+1
            alumnosCategoria.update({key: val})
    return alumnosCategoria


def clasificaAlumnosCarrera(alumnosCategoria):
    carreras = list()
    keys2 = list(alumnosCategoria.keys())
    for i in range(len(alumnosCategoria)):
        carreras.append(keys2[i][1])
    alumnosCarrera = dict.fromkeys(carreras, 0)
    keys = list(alumnosCategoria.keys())
    values = list(alumnosCategoria.values())
    for i in range(len(alumnosCategoria)):
        if(keys[i][1] in alumnosCarrera):
            val = int(alumnosCarrera.get(keys[i][1]))+values[i]
            alumnosCarrera.update({keys[i][1]: val})
    return alumnosCarrera



def clasificaAlumnosSexo(alumnosCategoria):
    alumnosSexo = dict.fromkeys(['F', 'M'], 0)
    keys = list(alumnosCategoria.keys())
    values = list(alumnosCategoria.values())
    for i in range(len(alumnosCategoria)):
        if(keys[i][0] in alumnosSexo):
            val = int(alumnosSexo.get(keys[i][0]))+values[i]
            alumnosSexo.update({keys[i][0]: val})
    return alumnosSexo


def despAlumnosSexo(alumnosSexo):
    print("#Alumnos    Sexo")
    keys = list(alumnosSexo.keys())
    values = list(alumnosSexo.values())
    for i in range(len(alumnosSexo)):
        print(values[i], "  \t   ", keys[i])

def despAlumnosCategoria(alumnosCategoria):
    print("#Alumnos    Sexo    Carrera")
    keys = list(alumnosCategoria.keys())
    values = list(alumnosCategoria.values())
    for i in range(len(alumnosCategoria)):
        print(values[i], "  \t   ", keys[i][0], "\t", keys[i][1])

def despEncuesta(alumnos):
    print("Matricula    Sexo    Carrera")
    for i in range(len(alumnos)):
        print(alumnos[i][0], "  \t   ", alumnos[i][1], "\t", alumnos[i][2])




def despAlumnosCarrera(alumnosCarrera):
    print("#Alumnos    Carrera")
    keys = list(alumnosCarrera.keys())
    values = list(alumnosCarrera.values())
    for i in range(len(alumnosCarrera)):
        print(values[i], "  \t   ", keys[i])


def main():
    alumnos = leeEncuesta()
    despEncuesta(alumnos)
    alumnosCategoria = clasificaAlumnosCategoria(alumnos)
    despAlumnosCategoria(alumnosCategoria)
    alumnosSexo = clasificaAlumnosSexo(alumnosCategoria)
    despAlumnosSexo(alumnosSexo)
    alumnosCarrera = clasificaAlumnosCarrera(alumnosCategoria)
    despAlumnosCarrera(alumnosCarrera)


main()
