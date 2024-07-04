import random
import csv

def inicial(): 
    
    return
    

def crear_codigo():
    return random.randint(100000, 999999)



def registrar(almacen):

   
    id_pedido=crear_codigo()
    nombre=input("nombre del cliente: ")
    direccion=input("direccion del cliente: ")
    sector=input("sector del cliente: ")
    seis_litro=0
    diez_litro=0
    doce_litro=0
    litros=0
    suma=0

  
    while litros <= 0 and litros != 6 and litros != 10 and litros !=12:
        print("ingrese la cantidad de litros")
        print("6")
        print("10")
        print("12")
        litros=int(input())
        inicial()
        if litros == 6:
            
            while True:
                suma=int(input("cuantos dispensadores necesita: "))
                if suma > 0:
                    break
                else:
                    print("tiene que ser mayor a 0")

            seis_litro = suma + seis_litro  
        elif litros == 10:
            while True:
                suma=int(input("cuantos dispensadores necesita: "))
                if suma > 0:
                    break
                else:
                    print("tiene que ser mayor a 0")
            diez_litro = suma +diez_litro 
            
        elif litros == 12:
            while True:
                suma=int(input("cuantos dispensadores necesita: "))
                if suma > 0:
                    break
                else:
                    print("tiene que ser mayor a 0")
            doce_litro = suma+ doce_litro
        else:
            print("cantidad de litros no disponible")
            
    datos = [ id_pedido,
              nombre,
              direccion,
              sector,
              seis_litro,
              diez_litro,
              doce_litro]
    almacen.append(datos)

def listar(almacen):
    print(["id", "nombre", "direccion", "sector", "6 litros", "10 litros", "12 litros"]) 
    for dispensadores in almacen:
        print(f"{dispensadores[0]}, {dispensadores[1]}, {dispensadores[2]}, {dispensadores[3]}, {dispensadores[4]}, {dispensadores[5]}, {dispensadores[6]}")

    
def ruta(almacen):
    with open("hoja_ruta.csv", "w", newline="") as archivo:
        escritor=csv.writer(archivo)
        #encabezado
        escritor.writerow(["id", "nombre", "direccion", "sector", "6 litros", "10 litros", "12 litros"])
        
        sectores = (["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"])
        sector_buscar=input("que sector buscas: ")
        if sector_buscar in sectores:
            for dispensador in almacen:
                if dispensador[3] == sector_buscar:
                    escritor.writerow(dispensador)

def buscar(almacen, code):
    print(["id", "nombre", "direccion", "sector", "6 litros", "10 litros", "12 litros"])
    for dispensador in almacen:
        if dispensador[0] == code:
            print(dispensador)
        

            

        

        
    


            

        
    
    
