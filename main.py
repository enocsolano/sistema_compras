#La galería de productos con sus respectivos precios es el siguiente:
#- Camisa tiene el código 1 con un precio de $50
#- Cinturón tiene el código 2 con un precio de $20
#- Pantalón tiene el código 3 con un precio de $30


print("             GALERÍA DE PRODUCTOS\n")
print("PRODUCTO            CODIGO          PRECIO")
print("Camisa                1              $50")
print("Cinturón              2              $20")
print("Pantalón              3              $30")
print("---------------------------------------------------")

inicio = int(input(" Ingrese 1 para iniciar: "))



contador = 0;
cuenta = 0;
while inicio == 1:
    cuenta+=1 
    print("---------------------------------------------------------\n ")
    print(f"                 ID: {cuenta}")
    codigo = int(input("Ingrese el código del producto a comprar: "))
    #OBJETO DE CAMISA
    producto = {
        1 : "Camisa",
        2 : "Cinturón",
        3 : "Pantalón"
    }
    #OBJETO DE PRECIO
    precio = {
        1 : 50,
        2 : 20,
        3 : 30
    }
    #PARA IMPRIMIR

    if codigo == 1: 
        print(f"El precio de {producto[codigo]} es de: ${precio[codigo]}")
    elif codigo == 2:
        print(f"El precio de {producto[codigo]} es de: ${precio[codigo]}")
    elif codigo == 3:
        print(f"El precio de {producto[codigo]} es de: ${precio[codigo]}")
        

    unidadesCompradas = int(input("Ingrese el número de unidades a comprar: "))
    compra = unidadesCompradas * precio[codigo]
    print(f"Subtotal: ${compra}")

    contador+=compra    
    
    print("\n--------------------------------------------------------- ")
    inicio = int(input("Ingrese 1 para seguir comprando 2 para ver factura final: "))
    
    if inicio!=1:
        print(f"\nTotal de factura general: ${contador}")
        if contador >= 0 and contador <= 100:
            print(f"No hay descuento porque tiene un total de ${contador}\n")
        elif contador >= 101 and contador <= 300:
            print("Tiene un descuento del 20%")
            descuento = contador - (contador*.20)
            print(f"Total: ${descuento}\n")
        elif contador >=301:
            print("Tiene un descuento del 30%")
            descuento = contador - (contador*.30)
            print(f"Total: ${descuento}\n") 
    else:
        pass



