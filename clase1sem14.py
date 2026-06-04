"""
programa que gestiona archivos en python 
los modos de apertura de un archivo son

"w" -> Escritura (write) siempre se crea el archivo. si no existe se crea, y si existe se remplaza
"a"-> Añadir (append) Siempre añade contenido en un archivo sin destruirlo, se crea la primera vez
"r"-> Lectura (Read) abre un archivo y prepararlo para su lectura
"""
import os
os.system("cls")
print("="*40)
print("PROGRAMA DE CÓDIGO HTML")
print("="*40)

vfichero = input("Ingrese el nombre del archivo a generar [sin espacios]: ").lower()

if vfichero == "" or len(vfichero) == 0:
    print("Error..! debe ingresar un valor en el nombre")
else:
    vfichero = vfichero + ".html"
    
    varchivo = open(vfichero, "w")
    
    vautor = input("Ingrese Su Nombre: ").upper()
    
    vhtml = "<!DOCTYPE html>\n"
    vhtml += "<html>\n"
    vhtml += "<head>\n"
    vhtml += "<title>Python</title>\n"
    vhtml += "</head>\n"
    vhtml += "<body>\n"
    vhtml += "<h1> Bienvenido a python</h1><br><hr>\n"
    vhtml += "<h2>Hola mundo...!</h2><br>\n"
    vhtml += "<h3>Soy, " + vautor + "</h3><br>\n"
    vhtml += "</body>\n"
    vhtml += "</html>\n"

    varchivo.write(vhtml)
    varchivo.close()
    
    print("="*60)
    print(f"Archivo [{vfichero}] generado correctamente")
    print("Programa finalizado con éxito, proceda a abrirlo en su navegador de confianza")
    print("="*60)
    
input("Pulse [ENTER] para continuar")
