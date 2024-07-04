import funcion

seis_litro=0
diez_litro=0
doce_litro=0
almacen=[]
while True:
    print("Menu Principal")
    print("1.Registrar")
    print("2-Listar los todos los pedidos")
    print("3.Imprimir hoja de ruta")
    print("4.Buscar un pedido por ID")
    print("5.Salir del programa")
    opc=input("Selecciona una opcion: ")

    if  opc == "1":
        funcion.registrar(almacen)
    elif opc == "2":
        funcion.listar(almacen)
    elif opc == "3":
        funcion.ruta(almacen)
    elif opc == "4":
        code=int(input("buscar por id del usuario"))
        funcion.buscar(almacen, code)
       
        
    elif opc == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion incorrecta")

        



