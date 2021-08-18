def main():
    #escribe tu código abajo de esta línea
    nacimiento=int(input("Dame el año de nacimiento: "))
    actual=int(input("Dame el año actual: "))
    lustro=float((actual-nacimiento)/5)
    print("Los lustros que has vivido son:", lustro)



if __name__ == '__main__':
    main()
