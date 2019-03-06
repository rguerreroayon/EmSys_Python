def main():
    sueldo = float(input('Ingresa tu sueldo: '))

    if(sueldo<1000):
        
        print('Comision: no hay comision')
        
    if(sueldo>= 1000 and  sueldo<=4999):
        comision = float(sueldo * .025)
        print('Comision: {0:.4f}.'.format(comision))
        
    if(sueldo>= 5000 and sueldo<=9999):
        comision = float(sueldo * .050)
        print('Comision: {0:.4f}.'.format(comision))
    if(sueldo>= 10000 and sueldo<=49999):
        comision = float(sueldo * .075)
        print('Comision: {0:.4f}.'.format(comision))
    else:
        comision = float(sueldo * .10)
        print('Comision: {0:.4f}.'.format(comision))
    
main()
