def esBisiesto(ano):
    return ano%4 == 0 and ano%100 != 0 or ano%400 == 0

def leeAnhos(listaBisiestos):
    anoInicial = listaBisiestos[0]
    anoFinal = listaBisiestos[len(listaBisiestos) - 1]

    anos = [anoInicial,anoFinal]
    return tuple(anos)


def listaBisiestos(ano1,ano2):
    anos = [ano1]
    while(ano1 < ano2):
        ano1 = ano1 + 1
        anos.append(ano1)

    anosBisiestos = list()

    for ano in anos:
        if(esBisiesto(ano)):
            anosBisiestos.append(ano)
    
    for ano in anosBisiestos:
        print(str(ano))


    print(anosBisiestos)
    return anosBisiestos 

def main():
    print(leeAnhos(listaBisiestos(1970,2020)))


main()