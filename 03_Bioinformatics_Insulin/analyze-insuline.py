"""
Script: analyze-insuline.py
Descripción: Limpieza de la secuencia genómica de preproinsulina humana utilizando Expresiones Regulares.
"""
#Se usa la librería re para trabajar con expresiones regulares
import re

#Abrimos el archivo de texto
with open("preproinsulin-seq.txt", "r") as f:
    #Leemos todo el contenido del archivo
    raw_data = f.read()

#Eliminar el ORIGIN //
clean_data = re.sub(r"\bORIGIN\b", "", raw_data, flags=re.IGNORECASE)

#Eliminar el terminador de registro
clean_data = clean_data.replace("//", "")

#Eliminar cualquier cosa que no sea letra
clean_data = re.sub(r"[^A-Za-z]", "", clean_data)

#Convertimos todo a minúsculas
clean_data = clean_data.lower()

#Abrir nuevamente el archivo prepoinsulina
with open("preproinsulin-seq.txt", "w") as f:
    #Limpiamos el archivo
    f.write(clean_data)

#Calculamos la longitud de prepoinsulina
print("Longitud prepoinsulina = ", len(clean_data))

#Si la secuencia no tiene 110 caracteres salimos del programa
if len(clean_data) != 110:
    print("Error, la secuencia no tiene 110 caracteres")
    exit()

#Extraemos los primeros 24 caracteres
ls_insulin = clean_data[0:24]

#Extraemos del carácter 25 al 54
b_insulin = clean_data[24:54]

#Extraemos del carácter 55 al 89
c_insulin = clean_data[54:89]

#Extraemos del carácter 90 al 110
a_insulin = clean_data[89:110]

#Creamos los diferentes archivos
with open("lsInsuline-seq-clean.txt", "w") as f:
    f.write(ls_insulin)

with open("bInsuline-seq-clean.txt", "w") as f:
    f.write(b_insulin)
    
with open("cInsuline-seq-clean.txt", "w") as f:
    f.write(c_insulin)
    
with open("aInsuline-seq-clean.txt", "w") as f:
    f.write(a_insulin)
    
#Verificamos el tamaño de caracteres
print("lsinsulin = ", len(ls_insulin))
print("binsulin = ", len(b_insulin))
print("cinsulin = ", len(c_insulin))
print("ainsulin = ", len(a_insulin))

insulin = b_insulin + a_insulin

#Total de insulina
print("Insulina procesada = ", len(insulin))

#Secuencia de la insulina
print("secuencia de la insulina = ", insulin)