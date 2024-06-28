#####
import csv
agregar_cliente=True
agregar_compra=True
lista_productos=[]
data=[]
lista_productos_cliente=[]
valor=0
valor_de_venta=0
valor_de_compra=0

def no_valido():
    print("***NO VALIDO***\nintente nuevamente\n")

def no_disponible():
    print("***No disponible***\nintente nuevamente\n")

def menu_productos():
    print("""  
      PRODUCTOS
Producto:       Valor:
1. Producto 1   1.200
2. Producto 2   1.000
3. Producto 3   1.100
4. Producto 4   1.700
5. Producto 5   1.100
0. Salir
""")


print(
"""
        Empresa X
    Gestion de pedidos.
""")


#Se solicitan los datos del cliente:

while agregar_cliente:
    lista_productos_cliente.clear()
    print("\nIngrese datos del cliente:")

    nombre=input("Nombre: ")
    while not nombre.isalpha():
        no_valido()
        nombre=input("Nombre: ")

    telefono=input("Telefono: ")
    while not telefono.isdigit() or len(telefono)<9 or len(telefono)>9:
        if len(telefono)<9 or len(telefono)>9:
            print("***Debe contener 9 digitos***\nintente nuevamente\n")
        else:
            no_valido()
        telefono=input("Numero de telefono: ")

    direccion=input("Direccion: ")

#Se solicitan los datos compra:
    agregar_compra=True
    lista_productos.clear()
    valor_de_venta=0
    while agregar_compra:
        menu_productos()
        
        producto=input("Ingrese numero de producto: ")
        if int(producto)==0:
            agregar_cliente=False
            break
    
        while not producto.isdigit() or int(producto)<0 or int(producto)>5:
            if producto.isdigit():
                if int(producto)<0 or int(producto)>5:
                    no_disponible()
            
            elif producto.lower()=="m":
                    menu_productos()
            
            else:
                no_valido()
            
            producto=input("Ingrese numero de producto:\nletra'm' para visualizar el menu\n")
        
        unidades_producto=input("Unidades: ")
        while not unidades_producto.isdigit() or int(producto)<0:

            if unidades_producto.isdigit():
                if int(producto)<0:
                    no_disponible()
            else:
                no_valido()
            unidades_producto=input("Unidades: ")
        
        
        if int(producto)==1:
            valor=1200
        elif int(producto)==2:
            valor=1000
        elif int(producto)==3:
            valor=1100
        elif int(producto)==4:
            valor=1700
        elif int(producto)==5:
            valor=1100
        

        valor_de_venta+=valor*int(unidades_producto)
        valor_de_compra=valor*int(unidades_producto)
        lista_productos_cliente.append([f"Code: {producto}",f"Units: {unidades_producto}"])
        lista_productos.append([f"Producto {producto}",f"Cantidad: {unidades_producto}",f"Valor: {valor_de_compra}$"])

        

#Agregar compra

        compra=input("Agregar compra:\n1. Si \n2. No\n")
        while not compra.isdigit() or int(compra)!=1 and int(compra)!=2 :

            if not compra.isdigit():
                no_valido()
            elif int(compra)!=1 or int(compra)!=2:
                no_disponible()
            
            compra=input("Agregar compra:\n1. Si \n2. No\n")
        
        if int(compra)==2:
            agregar_compra=False
    


#Lista de datos
    data.append([nombre,telefono,direccion,lista_productos_cliente])


#BOLETA

    print(
f"""
**********************************************
******************* BOLETA *******************
**********************************************
Productos:""")
    for i in lista_productos:
        print(i)
    print(f"PRECIO FINAL: {valor_de_venta}$\n**********************************************")


#agregar cliente
    nuevo_cliente=input("Ingresar nuevo cliente:\n1. Si \n2. No\n")
    while not nuevo_cliente.isdigit() or int(nuevo_cliente)!=1 and int(nuevo_cliente)!=2 :

        if not nuevo_cliente.isdigit():
            no_valido()
        elif int(nuevo_cliente)!=1 or int(nuevo_cliente)!=2:
            no_disponible()
            
        nuevo_cliente=input("Ingresar nuevo cliente:\n1. Si \n2. No\n")
        
    if int(nuevo_cliente)==2:
        agregar_cliente=False
print("\nSaliendo...")



#Traspasando la informacion al archivo CSV


with open('DATA.csv', 'w') as archivo_csv:

    escritor_csv = csv.writer(archivo_csv)
        
    escritor_csv.writerow(['Nombre', 'Telefono', 'Direccion', 'Productos'])
        
    escritor_csv.writerows(data)

    