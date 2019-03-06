import math 

def main():
    v = float(input('Indica la velocidad inicial: '))
    dm = 0.0
    am = 0.0
    gravedad = float(9.81)
    dm= 0.0

    print('VelocidadInicial {:.2f}'. format(v)) 
    print('Angulo       Distancia Alcanzada')
    print('--------------------------------')


    for angulo in range(0, 95, 5):
        angulo2 = math.radians(angulo)
        da = (2*(v**2)*math.sin(angulo2)*math.cos(angulo2)) / gravedad
        print('{:6d} {:20f}'.format(angulo,da))
        if da > dm:
	        dm = da
	        am = angulo

    print('Distancia máxima: {:f} metros - {:d} GRADOS'.format(dm,am))

main()
    