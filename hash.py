import hashlib
import os


def buscar_contraseña(contraseña, carpeta):
    hash_contraseña = hashlib.sha1(contraseña.encode()).hexdigest().upper()
    archivo_busqueda = hash_contraseña[:5] + ".txt"
    ruta_archivo = os.path.join(carpeta, archivo_busqueda)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as file:
            lineas = file.readlines()
            for linea in lineas:
                if linea.startswith(hash_contraseña):
                    return linea.split(':')[1].strip()
        print("Contraseña no encontrada en el archivo.")
    else:
        print("Archivo no encontrado.")


contraseña = input("Ingrese la contraseña: ")
carpeta_archivos = "/home/kate/Desktop/UNSA-2023A/BigData/Lab3/devdata"
numero = buscar_contraseña(contraseña, carpeta_archivos)

if numero:
    print("¡Oh no! Esta contraseña ha sido vista", numero, "veces antes.")
else:
    print("¡Good! No encontramos coincidencias para esta contraseña")

