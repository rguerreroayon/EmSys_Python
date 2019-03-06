import math


def main():
    alumnos = int(input('Inserte numero de alumnos: '))
    totalPromedio = 0.0
    sumaDesviaciones = 0.0
    i = 1
    promedios = []

    while i <= alumnos:
        promedio = float(input('Inserte promedio alumno '+str(i)+': '))
        promedios.append(promedio)
        totalPromedio = totalPromedio + promedio
        i = i + 1
        print(str(promedios))

    media = totalPromedio / alumnos
    print('Media:'+str(media))


    for promedio in promedios:
        tercerPaso = promedio - media
        desviacion = math.pow(tercerPaso,2)
        sumaDesviaciones = sumaDesviaciones + desviacion
    

    desviacionEstandar = math.sqrt(sumaDesviaciones/alumnos)

    print('Promedio de grupo: '+str(media))
    print('Desviación estándar: '+str(desviacionEstandar))



main()