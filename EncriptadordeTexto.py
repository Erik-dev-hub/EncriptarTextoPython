import os

def encriptarFichero(rutaFichero):
    fichero = open(rutaFichero, 'r')
    texto = fichero.read()
    fichero.close()
    textoEncriptado = encriptarTexto(texto)

    fichero = open(rutaFichero, 'w')
    fichero.write(textoEncriptado)
    print("La encriptación se realizó con exito. \n")
    fichero.close()

def encriptarTexto(textoAencriptar):
    print(f"El texto a encriptar es el siguiente: \n{textoAencriptar}")
    print("\n")
    textoEncriptado = ""
    for caracter in textoAencriptar:
        ascii = ord(caracter)
        ascii += 1
        textoEncriptado += chr(ascii)
    return textoEncriptado

rutadelFichero = input("Ingrese la ruta del archivo que contiene el texto a encriptar: ")
if os.path.exists(rutadelFichero):
    print("\n")
    encriptarFichero(rutadelFichero)
else:
    print("La ruta y/ó el fichero ingresado no son correctos, intentalo de nuevo.\n")


