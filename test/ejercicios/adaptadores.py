inputfile = "4_input_adapters.txt"
outputfile = "4_input_no_adapters.txt"

with open(inputfile,"r") as infile, open(outputfile,"w") as outfile:
    for line in infile:
     secuencia_limpia = line.strip()[14:]
     outfile.write(f"{secuencia_limpia}\n")
