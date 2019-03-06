class Alumno:
    def __init__(self,edad,sexo,procedencia,vivienda):
        self.edad = edad
        self.sexo = sexo
        self.procedencia = procedencia
        self.vivienda = vivienda


def main():
    ciclo = True
    alumnos = []

    while ciclo:
        print('Contesta esta encuestra!')
        edad = int(input('Ingresa tu edad: '))
        sexo = input('Ingresa tu sexo M/F: ')
        procedencia = input('Ingresa tu procedencia L - Local , F - Foraneo: ')

        if(procedencia == 'F' or procedencia == 'f'):
            vivienda = input('Vivienda Deseada (‘A’ por casa de asistencia, ‘C’ por compartir casa, ‘S’ por vivir solo: ')
            alumno = Alumno(edad,sexo,procedencia,vivienda)
            alumnos.append(alumno)

        else:
            alumno = Alumno(edad,sexo,procedencia,'LOCAL')
            alumnos.append(alumno)

        respuesta = input('Quieres encuestar a otro alumno? S/N: ')

        if(respuesta == 'N' or respuesta == 'n'):
            ciclo = False



    sumaPromedioEdad = 0
    sumaAlumnos = 0
    sumaForaneosHombres = 0
    sumaForaneosMujeres = 0
    sumaMujeresCompartirCasa = 0
    sumaAlumnosVivirCasaAsistencia = 0
    sumaHombresVivirSolo = 0

    promedioAlumnosEdad = 0
    porcentajeForaneos = 0
    porcentajeCasaAsistencia = 0
    porcentajeMujeresCompartirCasa = 0
    porcentajeHombresSolos = 0

    for alumno in alumnos:
        sumaPromedioEdad = sumaPromedioEdad + alumno.edad
        sumaAlumnos =sumaAlumnos + 1

        if alumno.procedencia == 'F' or alumno.procedencia == 'f':
            if alumno.sexo == 'M' or alumno.sexo == 'm':
                sumaForaneosMujeres = sumaForaneosMujeres + 1
            elif alumno.sexo == 'H' or alumno.sexo == 'h':
                sumaForaneosHombres = sumaForaneosHombres + 1

        
        if alumno.vivienda == 'C' or alumno.vivienda == 'c':
            sumaAlumnosVivirCasaAsistencia = sumaAlumnosVivirCasaAsistencia + 1
        elif alumno.sexo == 'H' or alumno.sexo == 'h':
            sumaHombresVivirSolo = sumaHombresVivirSolo + 1
        elif alumno.sexo == 'M' or alumno.sexo == 'm':
            sumaMujeresCompartirCasa = sumaMujeresCompartirCasa + 1


    promedioAlumnosEdad = sumaPromedioEdad / sumaAlumnos
    porcentajeForaneos = ((sumaForaneosHombres+sumaForaneosMujeres) * sumaAlumnos) / 100
    porcentajeCasaAsistencia = (sumaAlumnosVivirCasaAsistencia*sumaAlumnos) / 100
    porcentajeMujeresCompartirCasa = (sumaMujeresCompartirCasa*sumaAlumnos) / 100
    porcentajeHombresSolos = (sumaHombresVivirSolo * sumaAlumnos ) / 100

    print('Numero de alumnos encuestados: '+str(sumaAlumnos))
    print('Edad promedio de alumnos:'+str(promedioAlumnosEdad))
    print('Porcentajes de los alumnos hombres y mujeres foráneos: '+str(porcentajeForaneos))
    print('Porcentaje de alumnos que desean vivir en casa de asistencia: '+str(porcentajeCasaAsistencia))
    print('Porcentaje de alumnos mujeres que desean compartir casa: '+str(porcentajeMujeresCompartirCasa))
    print('Porcentaje de alumnos hombres que desean vivir solos: '+str(porcentajeHombresSolos))



main()