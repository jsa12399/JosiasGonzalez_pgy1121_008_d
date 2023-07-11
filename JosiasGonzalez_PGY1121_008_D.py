import numpy
import os
import time
import datetime
import funciones as fn


fecha = datetime.datetime.now()
arreglo_con = numpy.zeros((10,10),int)
fn.lista_run

platinum = 120000
gold =80000
silver = 50000

acumulador_platinum = 0
contador_platinum = 0

acumulador_gold = 0
contador_gold = 0

acumulador_silver = 0
contador_silver = 0

contador_total = 0
acumulador_total = 0



while True:
    os.system('cls')
    print("""Menú
          1. Comprar entradas
          2. Mostrar ubicaciones disponibles
          3. Ver listado de asistentes
          4. Mostrar ganacias totales
          5. Salir
          """)
    opcion = fn.validar_opcion()
    if opcion ==1:
        cant_entrada = fn.validar_entrada()
        run = fn.validar_run()
        fila = fn.validar_fila()
        if fila == 1 or fila == 2:
            acumulador_platinum = acumulador_platinum + platinum
            contador_platinum = contador_platinum + 1




        elif fila == 3 or fila == 4 or fila == 5:
            acumulador_gold = acumulador_gold + gold    
            contador_gold = contador_gold + 1




        elif fila == 6 or fila == 7 or fila == 8 or fila == 9 or fila == 10:
            acumulador_silver = acumulador_silver + silver
            contador_silver = contador_silver + 1   
            contador_total = contador_platinum+ contador_gold+ contador_silver     
            acumulador_total = acumulador_platinum+acumulador_gold+acumulador_silver


        columna=fn.validar_columna()
    
        print("Compra exitosa")
        
    elif opcion == 2:
        
        fn.arreglo()
        time.sleep(4)
        print("Asientos disponibles")


      
    elif opcion == 3:
        print(fn.lista_run)
        time.sleep(4)



    elif opcion == 4:
        print("[Tipo Entrada:]"         "[Cantidad]"                       " [Total]"                                             )
        print("[Platinum $120000]    ",     contador_platinum          ,acumulador_platinum                                   )
        print("[Gold: $80000]        "    ,     contador_gold              ,acumulador_gold                                       )
        print("[Silver: $50000]      "  ,     contador_silver            ,acumulador_silver                                     )                  
        print("[     TOTAL       ]   ",    contador_total            ,acumulador_total                                      )
        time.sleep(4)  
    else:
        print("Josias Gonzalez",fecha)
        break