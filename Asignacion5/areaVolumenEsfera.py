import math

def main():
    radio = float(input("Introduce los metros del radio de la esfera"))

    volumen = float((4*math.pi*pow(radio,3)/3))

    print('Pies: {0:.4f}.'.format(volumen))





main()



