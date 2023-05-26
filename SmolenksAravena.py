menu=True
carillas=250000
carillasQty=0
implantes=475000
implantesQty=0
ortodocia=800000
ortodociaQty=0
total=0
descuento=1
subtotal=0
subtotalDescuento=0
descuentoNum=0
valorCuota=0
'''
12 CUOTAS FIJAS

1. dar posibilidad de cotizar
2 reinciar cotizacion
3. salir
'''

while menu:
    while True:
        print('-'*50,"\n\tClinica Diente de Oro\n",'-'*50)
        print("\t1. Cotización\n\t2. Reiniciar cotizacion\n\t3. Salir")
        try:
            opcion=int(input("Ingresar opcion: "))
            if opcion==1:
                opcion_tratamiento=True
                while opcion_tratamiento:
                    while True:
                        print('-'*50,"\n\tTipos tratamientos:\n",'-'*50,"\n\t1. Carillas Porcelana ($250.000)\n\t2. Implantes Dentales ($475.000)\n\t3. Ortodoncia Brackets ($800.000)\n\t4. Descuento\n\t5. Salir")
                        try:
                            tratamiento=int(input("Ingresar opcion: "))
                            if tratamiento==1:
                                carillasQty+=1
                                print("Tratamiento Carillas Porcelana agregada")
                            elif tratamiento==2:
                                implantesQty+=1
                                print("Tratamiento Implantes Dentales agregada")
                            elif tratamiento==3:
                                ortodociaQty+=1
                                print("Tratamiento Ortodoncia Brackets agregada")
                            elif tratamiento==4:
                                opcion_cotizacion=True
                                while opcion_cotizacion:
                                    while True:
                                        print('-'*50,"\n\tTipos clientes:\n",'-'*50,"\n\t1. Normal\n\t2. Trabajador Auxiliar\n\t3. Trabajador Administrativo\n\t4. Trabajador docente")
                                        try:
                                            cotizacion_opcion=int(input("Ingresar opcion: "))
                                            if cotizacion_opcion==1:
                                                descuento=1
                                                descuentoNum=0
                                                opcion_cotizacion=False
                                                opcion_tratamiento=False
                                                break
                                            elif cotizacion_opcion==2:
                                                descuento=0.85
                                                descuentoNum=15
                                                opcion_cotizacion=False
                                                opcion_tratamiento=False
                                                break
                                            elif cotizacion_opcion==3:
                                                descuento=0.90
                                                descuentoNum=10
                                                opcion_cotizacion=False
                                                opcion_tratamiento=False
                                                break
                                            elif cotizacion_opcion==4:
                                                descuento=0.95
                                                descuentoNum=5
                                                opcion_cotizacion=False
                                                opcion_tratamiento=False
                                                break
                                            else:
                                                print("Opcion fuera de rango")
                                        except:
                                            print("Valor debe ser numerico")
                            elif tratamiento==5:
                                subtotal=(carillas*carillasQty)+(implantes*implantesQty)+(ortodocia*ortodociaQty)
                                subtotalDescuento=(subtotal)-(subtotal*descuento)
                                total=subtotal-subtotalDescuento
                                total=round(total)
                                subtotalDescuento=round(subtotalDescuento)
                                valorCuota=total/12
                                valorCuota=round(valorCuota)
                                print('-'*50, "\n\t\tCoización:\n", '-'*50)
                                print(f"{carillasQty} tratamiento(s) Carillas Porcelana\t ${carillas*carillasQty}")
                                print(f"{implantesQty} tratamiento(s) Implantes Dentales\t ${implantes*implantesQty}")
                                print(f"{ortodociaQty} tratamiento(s) Ortodoncia Brackets\t ${ortodocia*ortodociaQty}")
                                print('-'*50)
                                print(f"Subtotal\t\t${subtotal}\nDescuento {descuentoNum}%\t\t${subtotalDescuento}")
                                print('-'*50)
                                print(f"total\t\t\t${total}")
                                print('-'*50)
                                print(f"Son 12 cuotas de:\t${valorCuota}\n")
                                print("Sonria bonito\n")
                                opcion_tratamiento=False
                                break
                            else:
                                print("Opcion fuera de rango")
                        except:
                            print("Valor debe ser numerico")
            elif opcion==2:
                print('-'*50,"\n\tCotizacion reiniciada\n",'-'*50)
                carillasQty=0
                implantesQty=0
                ortodociaQty=0
                total=0
                descuento=1
            elif opcion==3:
                menu=False
                break
            else:
                print("Opcion fuera de rango")
        except:
            print("Valor debe ser numerico")