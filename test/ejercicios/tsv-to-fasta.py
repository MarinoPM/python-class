inputfile = "dna_sequences.txt"
outputfile = "dna_sequences.fa"


with open(inputfile, "r") as infile, open(outputfile, "w") as outfile:
    for linea in infile:
        partes = linea.strip().split("\t")
        id = partes[0]
        seq = "\t".join(partes[1:])  # Junta todas las columnas a partir de la segunda
        outfile.write(f">{id}\n{seq.upper()}\n")
