secuencias = input("dame secuencias separadas por comas ").split(",")

secuencias_arn = [secuencia.replace("T","U").strip() for secuencia in secuencias]

print(secuencias_arn)