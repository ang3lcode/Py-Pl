#Leer un archivo línea por línea
"""with open('01py-curso\\R_W_archivos\\txt\\Cuento.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#Leer todas las líneas en una lista
"""with open('01py-curso\\R_W_archivos\\txt\\Cuento.txt', 'r') as file:
    lines = file.readline()
    print(lines)
    print(len(lines))"""

#Añadir texto
"""with open('01py-curso\\R_W_archivos\\txt\\Cuento.txt', 'a') as file:
    file.write('\n\nBy:ChatGPT')"""

#Sobreescribir el texto
"""with open('01py-curso\\R_W_archivos\\txt\\Cuento.txt', 'w') as file:
    file.write('\n\nBy:ChatGPT')"""