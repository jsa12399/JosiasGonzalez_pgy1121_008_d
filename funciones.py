import numpy
arreglo_con = numpy.zeros((10,10),int)

lista_run = []



def validar_run():
    while True:
        try:
            run = int(input("Ingrese run: "))
            if len(str(run)) == 8:
                lista_run.append(run)
                return run 
                
            else:
                print("Error debe ingresar rut valido")
        except:
            print("Error debe ingresar numeros enteros")    

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("Error debe ingresar opcion valida")
        except:
            print("Error debe ingresar numeros enteros")       


def validar_entrada():
    while True:
        try:
            cant_entrada = int(input("Ingrese cantidad de entradas que desea (1 a 3): "))         
            if cant_entrada >=1 and cant_entrada <=3:
                return cant_entrada
            else:
                print("Error ingrese una cantidad valida")   
        except:
            print("Error debe ingresar numeros enteros")        



def arreglo():
    for x in range(10):
        print(f"fila: {x+1}:",end=" ")
        for y in range(10):
            print(arreglo_con[x][y],end=" ")
        print()
        print()    

def validar_fila():
    while True:
        try:
            fila = int( input("Ingrese fila que desea: "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("Error debe ingresar una fila valida: ")
        except:
            print("Error debe ingresar numeros enteros") 


def validar_columna():
    while True:
        try:
            columna = int( input("Ingrese columna que desea: "))
            if columna in (1,2,3,4,5,6,7,8,9,10):
                return columna
            else:
                print("Error debe ingresar una columna valida: ")
        except:
            print("Error debe ingresar numeros enteros")              


               