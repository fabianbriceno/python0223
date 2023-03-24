## BRICENO VILLEGAS LEONARDO
## EJERCICIO 1 - IMPRIMIR MIS DATOS PERSONALES
name=input("Dime tus nombres y apellidos: ")
edad=input("Dime tu edad:")
sexo=input("Dime tu sexo:")
estudios=input("Dime tus estudios:")
mensaje="BIENVENIDO/A"
print(name)
print(edad)
print(sexo)
print(estudios)
print(mensaje,name)

## EJERCICIO 2 --- AREA CIRCULO, CUADRADO Y TRIANGULO

Opciones="""
    1)AREA DEL CIRCULO
    2)AREA DEL CUADRADO
    3)AREA DEL TRIANGULO    
"""
print(Opciones)
opt=int(input("Ingrese una opcion que deseas desarrollar:"))

if type(opt) == int:
    if opt==1:
        radio=int(input("Ingresa el radio:"))
        print(f"El area del Circulo es: {radio*radio*3.14}")
    elif opt==2:
        lado=int(input("Ingresa el lado: "))
        print(f"El area del Cuadrado es: {lado*lado}")
    elif opt==3:
        base=int(input("Ingresa la base: "))
        altura=int(input("Ingresa la altura:"))
        print(f"El area del Triangulo es: {(base*altura)/2}")  
    else:
        print("Ingrese una opcion correcta")
else:
    print("ingrese un valor entero ,valor no permitido")

 ## EJERCICIO 3 -- SUMA, RESTA, MULTIPLICACION, DIVISION Y DIVISION ENTERA

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero:"))
numero3=int(input("Ingrese el tercer numero:"))

if (numero2==0):
    print("No puede ser cero")
elif(numero3==0):
    print("No puede ser cero")
else:
    print(f"La suma de los tres numeros es: {numero1+numero2+numero3}")
    print(f"La resta de los tres numeros es: {numero1-numero2-numero3}")
    print(f"La multiplicacion de los tres numeros es: {numero1*numero2*numero3}")
    print(f"La division de los tres numeros es: {numero1/numero2/numero3}")
    print(f"La division de los tres numeros es: {numero1//numero2//numero3}")

## EJERCICIO 4 -- TIPO DE DATOS

var = input("Ingrese un valor: ")
print(type(var))
    
## EJERCICIO 5 -- IMPORTAR LA RUTA
import sys
print("La ruta es "+sys.argv[0])

## EJERCICIO6 == SUMA DE N NUMEROS

numero=int(input("Ingrese el numero: "))

print(f"La suma de los numeros es: {(numero*(numero+1)//2)}")

##EJERCICIO 7 -- COMPARACION DE NUMEROS

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))

if (numero1 == numero2):
    print("Los numeros son iguales")
elif (numero1 != numero2):
    print("los numeros son diferentes")
    if(numero1 > numero2):
        print("El primer numero es mayor que el segundo")
    else:
        print("El primer numero es menor que el segundo")
else:
    print("Vuelva a intentarlo")

#EJERCICIO 8 -- CONTRASEÑA

contra = "contraseña"
password = input("Introduzca la contraseña: ")
if contra == password.lower():
    print("Contaseña Correcta")
    print("Usuario Detectado")
    print("Bienvenido")
else:
    print("Contraseña Incoincide")
    print("Alerta De Intruso")

#EJERCICIO 9 -- CADENAS Y TUPLAS

lista = [('Pedro','24','12345678'),('Jose','10','12309845'),('Martin','26','23456789'),('Julio','58','2356789')]
lista_dni = ['12345678','12309845','23456789','98765432']
 
for valor in lista :
    if int(valor[1]) >= 18 :
        if valor[2] in lista_dni :
            print(valor[0])

#EJERCICIO 10 -- DICCIONARIOS

info_curso = {"nombre de curso":"", "cantidad de alumnos":0, "activo":True, "nombre de profesor":"", "max nota":0, "alumnos":[]}

input1 = input("Ingrese nombre de alumno:")
info_curso["alumnos"].append(input1)
input2 = input("Escriba el nombre del curso:")
info_curso["nombre de curso"] = input2
input3 = int(input("Ingrese la nota maxima:"))
info_curso["max nota"] = input3
print(info_curso)