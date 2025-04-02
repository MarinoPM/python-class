
secuencia = "ATGCGT"

for i, base in enumerate(secuencia):
    print(f"Posicion {i}: {base}")



#funcion zip

bases = "ATGCC"
complementos = "TACG"

for base, complemento in zip(bases, complementos):
    print(f"{base} --> {complemento}")