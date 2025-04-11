inputfile = "dna_sequences.fa"

with open(inputfile, "r") as infile:
    lineas = infile.readlines()

#print(lineas[0])
#print(lineas[1])

lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
print(f"Total de secuencias: {len(lineas_filtradas)}")