## EJERCICIO 1

Menu= """
1)Hacer un cuadrado
2)Saber los Multiplos
3)Identificar los Mayores de edad
"""
print(Menu)
opcion=int(input("Elija su opcion:"))

#1.1 un cuadrado
if opcion==1:
    cuadrado = int(input('Ingrese la medida del lado del cuadrado: '))
    for f in range(0, cuadrado):
        for c in range(0, cuadrado):
            print('*', end='')
        print()
        pass

#1.2 multiplo de 2
elif opcion ==2:
    lista=[1,2,35,28,97]
    for numero in lista:
        if (numero % 2 == 0):
            print(f"es multiplo: {numero}")


#1.3 mayores de edad
elif opcion == 3:
    personas = [('Luis','24'),('Miguel','26'),('Kiara','11')]
    for edad in personas:
        if int(edad[1])>=18:
            print(f"Mayores de edad:{edad}")

## EJERCICIO 2

Biblioteca = {
    "Categoria":["Literatura","Historia","Filosofia","Religion"],
    "Libros":[
        
            ### Titulo, Autor, Disponibilidad 
            ["Cien años de Soledad","Gabriel garcia Marquez", "disponible"],
            ["historia del Peru","Inca Garcilazo de la Vega", "disponible"],
            ["El discurso del metodo", "Rene Descartes", "prestado"],
            ["Cuenta con Jesus","Alicia PAz", "disponible"],
    ],
    "Usuarios":[]
}

def mostrar_categoria():
    print(Biblioteca["Categoria"])

def mostrar_libros ():
    print(Biblioteca["Libros"])

def agregar_usuario():
    print("Escriba salir para dejar de colocar usuarios")
    nom_usuario = input("Agregue el nombre del usuario: ")
    while nom_usuario != "salir":
        Biblioteca["Usuarios"].append(nom_usuario)
        nom_usuario = input("Agregue el nombre del usuario: ")
    print("Estos son los usuarios agregados", '\n',Biblioteca['Usuarios']) 

def cambiar_estado_libro():
    print(Biblioteca["Libros"])
    cambio = input("Ingresar el nombre del libro a cambiar ")
    print("Estados: disponible o prestado")
    estado = input("Ingresar el nuevo estado: ")
    for i in range(0,3):
        if Biblioteca["Libros"][i][0] == cambio:
            Biblioteca["Libros"][i][2] = estado
            print(Biblioteca["Libros"])
        else:
            print("No se encontro el libro")


##mostrar_categoria()
##mostrar_libros()
#agregar_usuario()
cambiar_estado_libro()

## EJERCICIO 3
##mayor

primero = int(input("ingrese el primero numero: "))
segundo = int(input("ingrese el segundo numero: "))

def mayor():
    if (primero > segundo):
        print(f"el mayor es:{primero}")
    elif (primero < segundo):
        print(f"el mayor es:{segundo}")
    else:
        print("son iguales")
mayor()

## EJERCICIO 4
import sys

args = sys.argv
print("argumentos:", args)
print("cantidad de argumentos:", len(args))

## EJERCICIO 5
import sys
abc = sys.path

print(list(abc))

## EJERCICIO 6
#EVENTO
concierto={
    'artista':"jeff beck",
    'precio':700,
    'aforo':1000,
    'lugar':"Parque de la Exposicion"
}

def buscarEvento(artista):
    if concierto['artista'] == artista:
        return concierto
    else:
        return False

def verificarAforo(conciert:dict)->int:
    if conciert['aforo']:
        return conciert['aforo']
    
def verificarLugar(lug:dict):
    if lug['lugar'] :
        return lug['lugar']
    else:
        return False
    

def main():
    nameConcierto=input('Nombre del concierto que desea:')
    myConcert=dict()
    if buscarEvento(nameConcierto):
        myConcert=buscarEvento(nameConcierto)
    else:
        print("No existe el concierto")

    #verificar aforo
    if verificarAforo(myConcert):
        print(f"El aforo para el concierto es {verificarAforo(myConcert)}")
    else:
        print("No hay aforo disponible")
    
    #verificar Lugar
    if verificarLugar(myConcert):
        print(f"El concierto se llevara acabo en {verificarLugar(myConcert)}")
    else:
        print("Concierto Cancelado")

main()

########## EJERCICIO 7

texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas Letraset, las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum"


Menu= """
1)Cambiar el texto a MAYUSCULA
2)Saber la longitud del texto
3)buscar cuantas veces sale una palabra
"""
print(Menu)
opcion=int(input("Elija su opcion:"))

if opcion==1:
    print(texto.upper())

elif opcion ==2:
    print(len(texto))

elif opcion == 3:
        palabra = input("que palabra quiere buscar?:")
        print(texto.count(palabra))

else:
    print("adios")

## EJERCICIO 8
lista=range(0,1000,1)

prime=[]

for i in lista:
   c=0
   for j in range(1,i):
      if i%j==0:
         c+=1
   if c==1:
      prime.append(i)

print(prime)

## EJERCICIO 9

### Minisistema
roles=['admin','vendedor','inventario']

sistema={
    "nombre":"tienda",
    "usuarios":[
        {
            'name':"",
            'password':"",
            'rol':"" ##vendedor ,administrador ,inventario
        }
    ],
    "sedes":[{
        "nombreSede":"",
        "ubicacion":""
    }],
    "productos":[
    {
        "nombre":"",
        "precio":"",
        "stock":""
    }]
}
## funciones
## joaquin samanamud
def agregarUsuario():
    nameUsuario=input("ingrese el nombre de usuario")
    password=input("ingrese su password")
    while True:
        rol=input("ingrese su rol")
        if rol in roles:
            break
        else:
            print("ingrese un rol correcto",roles)
    
    dictUser={
        'name':nameUsuario,
        'password':password,
        'rol':rol
    }
    sistema['usuarios'].append(dictUser)
###
def eliminarUsuario():
    usuarioPorEliminar=input("ingrese usuario por eliminar")
    for i,valor in enumerate(sistema['usuarios']):
        if valor['name']==usuarioPorEliminar:
                ## ingresar password para verificar que es correcto
                sistema['usuarios'].remove(i)
    ## remove
    pass
###
def obtenerRol(usuario):
    rol=""
    for i,valor in enumerate(sistema["usuarios"]):
        if valor['name']==usuario:
            rol=valor['rol']
    return rol
####
def agregarSedes():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        sede=input("ingrese sede")
        ubicacion=input("ingrese ubicacion")
        dictSede={
            'sede':sede,
            'ubicacion':ubicacion
        }
        sistema["sedes"].append(dictSede)
    else:
        print("no es un rol permitido")


## BRICENO VILLEGAS LEONARDO
def agregarProductos():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        nombre=input("ingrese nombre del producto:")
        precio=int(input("ingrese precio del producto:"))
        stock=int(input("ingrese stock del producto:"))
        dictProducto={
            'nombre':nombre,
            'precio':precio,
            'stock':stock
        }
        sistema["productos"].append(dictProducto)
    else:
        print("no es un rol permitido")

#####
def cambiarStock():
    usuario=input("ingresa usuario")
    rol=obtenerRol(usuario)
    if rol=='admin':
        print(sistema["productos"])
        valores = input("cambiar el stock:")
        for valor in sistema["productos"]:
            valor['stock'] = valores
            print(sistema["productos"])

pass


agregarUsuario()
print(sistema)


agregarProductos()
print(sistema)

cambiarStock()
print(sistema)

