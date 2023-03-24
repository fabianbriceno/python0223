# ARCHIVO MAIN.PY

import Ejercicio2_1203 as E2
import Ejercicio3_1203 as E3
import Ejercicio4_1203 as E4
import Ejercicio5_1203 as E5
import Ejercicio6_1203 as E6

if __name__=="__main__":
     print(__name__)


print("Ejercicio 2:")
E2.Ej2()
print("Ejercicio 3:")
E3.Ej3()
print("Ejercicio 4:")
E4.Ej4()
print("Ejercicio 5:")
E5.Ej5()
print("Ejercicio 6:")
E6.Ej6()

# EJERCICIO 2 

def Ej2():    
    class Producto_AP:
        name=""
        code=""
        marca=""
        precio=0.0
        def __init__(self,name,code,marca,precio):
            self.name=name
            self.code=code
            self.marca=marca
            self.precio=precio

        def __str__(self) -> str:
            return f'El producto {self.name} con código {self.code} de marca {self.marca}, cuesta {self.precio} soles'
    class Catálogo:
        ListaProdAutoPartes=[]
        def __init__(self):
            self.ListaProdAutoPartes=[]
        def agregarprod(self,producto):
            self.ListaProdAutoPartes.append(producto)
        def motrarlista(self):
            for i in self.ListaProdAutoPartes:
                print(i)

    ap1=Producto_AP("Filtro","4336","FILPOWER",200.0)
    ap2=Producto_AP("Bujía","4562","CHAMPION",150.0)

    list=Catálogo()
    list.agregarprod(ap1)
    list.agregarprod(ap2)
    print("---Lista de productos de autopartes ---")
    list.motrarlista()

# EJERCICIO 3

def Ej3(): 
    try:
        def dividir(a,b):
            try:
                c=a/b
                print("El resultado es :",c)
            except Exception as E:
                print(E)
        a=float(input("Ingrese un número: "))    
        b=float(input("Ingrese otro número: "))
        dividir(a,b)         
    except Exception as E:
                print(E)

# EJERCICIO 4
 
def Ej4(): 
    class Producto:
        nombre=""
        codigo=""
        def __init__(self,nombre,codigo):
            self.listaProducto=[]
            self.nombre=nombre
            self.codigo=codigo
        
        def __str__(self)->str:
            return f"El nombre del producto es {self.nombre} y el código es {self.codigo}"
        
        def identificarPaisLote(self):
            cod=self.codigo.split(sep="-")
            print("País de origen:",cod[0],"y Lote:",cod[1])
    p1=Producto('Televisor','ARGENTINA-0043-2020') #Otro ejemplo: p2=Producto('Celular','ARGENTINA-0574-2021')

    print(p1)
    p1.identificarPaisLote()

# EJERCICIO 5

def Ej5(): 
    try:
        from Ejercicio4_1203 import Ej4
    except Exception as E:
        print(E)
    else:
        import os
        print("La ruta del directorio",os.getcwd())
    finally:
        print("--Proceso terminado--")

# EJERCICIO 6

def Ej6(): 
    class Product:
        id=""
        nombre=""
        precio=""
        tipo=""
        stock=""
        release=""
        def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
            self.id=id
            self.nombre=nombre
            self.precio=precio
            self.tipo=tipo
            self.stock=stock
            self.release=release
            pass
        def __str__(self) -> str:
            return f"El producto {self.nombre} con id {self.id}  de {self.precio} soles, cuenta con {self.stock} und en stock"
        def updateStock(self,stock):
            self.stock=stock
        def updateID(self,id):
            self.id = id
        
    class CarritoCompra: 
        def __init__(self):
            self.listaProductos=[]
            self.precioTotal=0
        def agregarProducto(self,product:Product,cantidad=1):
            if self.validarStock(product):
                print("agregando producto")
                self.listaProductos.append(product)
                product.updateStock(product.stock-1)
            else:
                print("el producto no tienen stock")
            
        def quitarProduct(self,id):
            for index in self.listaProductos:
                if index.id==id:
                    self.listaProductos.remove(index)
                    print("--Producto eliminado--")
                    for a in self.listaProductos:
                        if a.id>id:
                            a.updateID(a.id-1) 
                else:
                    print("--No existe producto con ese id--")

        def calcularPrecio(self):
            for i in self.listaProductos:
                self.precioTotal+=i.precio
            print(f"Precio total: {self.precioTotal}")
        def validarStock(self,product:Product):
            existe=False
            if product.stock>0:
                existe=True
            return existe
        def mostrarProductos(self):
            print("Hay ",len(self.listaProductos)," productos en el carrito")
            if len(self.listaProductos)>0:
                for i in self.listaProductos:
                    print(i)
            else:
                print("carrito vacio")

    message="""
        1)Agregar Producto
        2)Mostrar Productos
        3)Quitar producto
        4)Mostrar el precio total
        5)Salir
    """
    id=0
    carrito=CarritoCompra()
    while True:
        
        print(message)
        opcion=int(input("ingrese la opcion a realizar:"))
        if opcion==1:
            try:
                id=id+1
                name=input("ingrese el nombre del producto:")
                precio=float(input("ingrese el precio del producto:"))
                tipo=input("ingrese el tipo del producto:")
                stock=int(input("ingrese el stock del producto:"))
                release=int(input("ingrese el release del producto:"))
                px=Product(id,name,precio,tipo,stock,release)
                carrito.agregarProducto(px)
            except Exception as Error:
                    print(Error)
                    print("sucedio un error")
            else:
                print("agregando en el menu")
        if opcion==2:
            carrito.mostrarProductos()
        if opcion==3:
            if len(carrito.listaProductos)>0:
                id_=int(input("Ingrese el id del producto que quiere quitar: "))
                carrito.quitarProduct(id_)
            else:
                print("No hay productos en el carrito para quitar")
        if opcion==4:
            carrito.calcularPrecio()
            
        if opcion==5:
            break      
                