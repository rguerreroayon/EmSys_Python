def main():
    metros = input("Introduce los metros")
    metros = float(metros)
    pies = float(metros * 3.28084)
    pulgadas = float(metros * 39.3701)




    print('Pies: {0:.4f}.'.format(pies))
    print('Pulgadas: {0:.4f}.'.format(pulgadas))


main()