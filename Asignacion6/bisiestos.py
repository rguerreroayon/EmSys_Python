def main():
    ano1 = int(input('Introduce un año: '))
    ano2 = int(input('Introduce otro año: '))
    anos = [ano1]

    while(ano1 < ano2):
        ano1 = ano1 + 1
        anos.append(ano1)


    for ano in anos:
        if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
            print('El año '+str(ano)+' es bisiesto')


main()
