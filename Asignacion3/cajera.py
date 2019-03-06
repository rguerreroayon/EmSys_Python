def main():
    dinero = int(input("Cuanta feria vas a sacar :D?"))
    contador1000 = 0
    contador500 = 0
    contador100 = 0
    contador50 = 0
    mil = int(1000)
    quin = int(500)
    cien = int(100)
    cincu = int(50)

    if dinero / mil >= 1:
        contador1000 = int(dinero/mil)
        dinero = dinero - mil*contador1000
    
    if dinero / quin >= 1:
        contador500 = int(dinero/quin)
        dinero = dinero - quin*contador500
    if dinero / cien >= 1:
        contador100 = int(dinero/cien)
        dinero = dinero - cien*contador100
    if dinero/ cincu >= 1:
        contador50 = int(dinero/cincu)
        dinero = dinero - cincu*contador50



    print('Dinero faltante: '+str(dinero))
    print('Billetes de 1000: '+str(contador1000))
    print('Billetes de 500: '+str(contador500))
    print('Billetes de 100: '+str(contador100))
    print('Billetes de 50: '+str(contador50))






main()

