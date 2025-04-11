
with open("genes.gff") as file:
    for linea in file:
        columnas = linea.strip().split("\t")
        tamaño = int(columnas[4]) - int(columnas[3]) + 1
        print(tamaño)
        


