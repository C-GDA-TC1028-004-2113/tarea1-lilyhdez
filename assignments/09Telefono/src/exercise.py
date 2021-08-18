def main():
    #escribe tu código abajo de esta línea
    msj=int(input("Dame el número de mensajes: "))
    megas=float(input("Dame el número de megas: "))
    mins=int(input("Dame el número de minutos: "))

    costo=float((msj*0.80)+(megas*0.80)+(mins*0.80))
    print("El costo mensual es:",costo)




if __name__ == '__main__':
    main()
