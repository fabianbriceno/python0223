##EJERCICIO 1 MAIN.PY

if __name__=="__main__":
     print(__name__)
     
print("\n** Ejercicio 1 **")
print("Se está ejecuntando el main.py")
print("\n** Ejercicio 2 **")
import Ejercicio2_1903
print("\n** Ejercicio 3 **")
import Ejercicio3_1903
print("\n** Ejercicio 4 **")
import Ejercicio4_1903
print("\n** Ejercicio 5 **")
import Ejercicio5_1903
print("\n** Ejercicio 6 **")
print("Se creó un ejecutable del ejercicio 2")

## EJERCICIO 2

import random
class Sorteo:
    
    def __init__(self):
        self.cantidadValores=0
        self.listaValores=[] 
    def ingresarValores(self,cantidadValores):
        for i in range(1,cantidadValores+1):
            elementos=input(f"Dato {i} a sortear: ")
            self.listaValores.append(elementos)   
    def mostrarLista(self):
        if len(self.listaValores)>0:
            for i in self.listaValores:
                print(i)
        else:
            print("---Lista vacía---")
    def sortear(self):
        if len(self.listaValores)>0:
            print("Elegido: ",random.choice(self.listaValores))
        else:
            print("---No hay datos para sortear---")

message="""
    1) Ingresar valores para sortear
    2) Mostrar valores
    3) Sortear aleatoriamente
    4) Salir
    """
sorteoo=Sorteo()
while True:
    print(message)
    op=int(input("Ingrese la opción que desea realizar: "))
    if op==1:
        try:
            n=int(input("Ingrese la cantidad valores a sortear: "))
            sorteoo.ingresarValores(n)
        except Exception as E:
                print("!!!Sucedió un error: ",E)
        else:
            print("--Agregando valores--")
    if op==2:
        sorteoo.mostrarLista()
    if op==3:
        sorteoo.sortear()
    if op==4:
        break

## EJERCICIO 3


block_cipher = None


a = Analysis(
    ['Ejercicio2_1903.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Ejercicio2_1903',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

## EJERCICIO 4

import sqlite3
from datetime import datetime
try:
    conexion = sqlite3.connect("Clase04/ListaEjercicios_clase04/TextoEj4.txt")
    cursor = conexion.cursor()
    fichero=open("Clase04/ListaEjercicios_clase04/TextoEj4.txt","a")
    msg=input("Ingrese un mensaje: ")
    fecha0=datetime.now()
    fecha1=datetime.strftime(fecha0, ' %B %d %Y ')
    fichero.write(f"{fecha1} - TextoEj4.txt - {msg}")

except Exception as E:
    print(E)

## EJERCICIO 5

import re
numCelular=input("Ingrese su número de celular:")
validar=re.search(r"^9\d{8}$", numCelular) #Al agregar {8} implica que debe haber 8 caracteres númericos después del 9
if validar:
    print("Número válido")
else:
    print("¡Número inválido!")