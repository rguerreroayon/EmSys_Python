import maclaurin as mc

def main():
    
    while True:

        tipoFuncion = input('Función a realizar -S para Seno , -E Exponencial')
        valor = float(input('Valor a calcular en la función'))
        vMin = int(input('Valor donde comienza la tabulación'))
        vMax = int(input('Valor donde termina la tabulación'))
        incr = int(input('Valor de incremento para la tabulación'))
        mc.tabularFuncion(tipoFuncion,valor,vMin,vMax,incr)

        opcion = input('Desea volver a ejecutar el programa - S/N')
        
        if opcion == 'N':
            break

main()