#Se una la librería re para trabajar con expresiones regulares
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
lsInsulin = clean_data[0:24]

#Extraemos del carácter 25 al 54
bInsulin = clean_data[24:54]

#Extraemos del carácter 55 al 89
cInsulin = clean_data[54:89]

#Extraemos del carácter 90 al 110
aInsulin = clean_data[89:110]

#Creamos los diferentes archivos
with open("lsInsuline-seq-clean.txt", "w") as f:
    f.write(lsInsulin)

with open("bInsuline-seq-clean.txt", "w") as f:
    f.write(bInsulin)
    
with open("cInsuline-seq-clean.txt", "w") as f:
    f.write(cInsulin)
    
with open("aInsuline-seq-clean.txt", "w") as f:
    f.write(aInsulin)
    
#Verificamos el tamaño de caracteres
print("lsinsulin = ", len(lsInsulin))
print("binsulin = ", len(bInsulin))
print("cinsulin = ", len(cInsulin))
print("ainsulin = ", len(aInsulin))

insulin = bInsulin + aInsulin

#Total de insulina
print("Insulina procesada = ", len(insulin))

#Secuencia de la insulina
print("secuencia de la insulina = ", insulin)