def main():
    primeraCalidad = int(150)
    segundaCalidad = int(125)
    desperdicioUno = float(.10)
    desperdicioDos = float(.15)
    

    metrosCuadrados = float(input('Ingresa los metros cuadrados: '))
    tipoMosaico = str(input('Inserta el tipo de mosaico (P - Primera Calidad, S - Segunda Calidad: '))

    if tipoMosaico == 'P':
        metrosCuadradosAComprar = metrosCuadrados + float(metrosCuadrados * desperdicioUno)


    elif tipoMosaico == 'S':
        metrosCuadradosAComprar = metrosCuadrados + float(metrosCuadrados * desperdicioDos)


    print('Metros cuadrados a comprar: '+str(metrosCuadradosAComprar))
    
main()

