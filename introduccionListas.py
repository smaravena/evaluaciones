'''
Cree un sistema de ventas de supermercado en el cual se pueda agregar productos al carro de compras, las opciones del menú serán:
1.- Agregar productos deberá mostrar un menú con 5 productos y sus precios (creado por usted), cada vez que se seleccione un producto quedará agregado en la lista.
2.- Ver canasta, es mostrar todos los productos seleccionados.
3.- Ver total, es mostrar el total a pagar por el cliente.
'''
menu=True
productos=["Cereal = $1.000", "Leche = $1.200", "Manzana = $250", "Pera =  $200", "Uva = $5"]
productos.sort()
canasta=[]
total=0
opcion=0
producto="blank"
line='-'*50

while menu:
    while True:
        print(f"{line}\n\tMENU PRINCIPAL\n1. Agregar productos\n2. Ver canasta\n3. Ver total a pagar\n4. Salir")
        try:
            opcion=int(input("Ingresar opcion: "))
            if opcion==1:
                print(f"{line}\n\tProductos disponibles:\n{productos}")
                while True:
                    try:
                        producto=str(input("Escribir producto a añadir [EXIT PARA SALIR]: "))
                        producto=producto.lower()
                        if producto=='manzana':
                            print("+1 manzana(s) a canasta")
                            canasta.append("manzana")
                            total+=250
                        elif producto=="leche":
                            print("+1 leche(s) a canasta")
                            canasta.append("leche")
                            total+=1200
                        elif producto=="cereal":
                            print("+1 cereal(es) a canasta")
                            canasta.append("cereal")
                            total+=1000
                        elif producto=="pera":
                            print("+1 pera(s) a canasta")
                            canasta.append("pera")
                            total+=200
                        elif producto=="uva":
                            print("+1 uva(s) a canasta")
                            canasta.append("uva")
                            total+=5
                        elif producto=="exit":
                            break
                        else:
                            print("Producto inexistente")
                    except:
                        print("Valor nombre producto invalido")
            elif opcion==2:
                canasta.sort()
                print(f"{line}\nCANASTA: {canasta}")
            elif opcion==3:
                print(f"{line}\nTotal: ${total}")
            elif opcion==4:
                menu=False
                break
            else:
                print("Valor invalido")
        except:
            print("Solo valor numerico")