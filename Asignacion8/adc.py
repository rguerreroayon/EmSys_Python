import math
import time

def adc():
    vmax = int(10)
    bits = 12
    steps = int(math.pow(2,bits))
    stepWidth = (( vmax / (math.pow(2,bits))))


    print('Valor Maximo: '+str(vmax))
    print('Bits de resolucion: '+str(bits))
    print('Pasos: '+str(steps))

    vin = int(input('Ingresa el input: '))
    

    if( vin > vin < 11):
        print(str(stepWidth))

        
        for i in range(1,steps+1):
            vout = (math.pow(2,12)*vin) / vmax
            vin = vin + stepWidth
            print('Valor digital numero '+str(i)+': '+str(vout))
            time.sleep(1)

adc()
