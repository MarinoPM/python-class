

secuencias = input("Dame secuencias separadas por comas: ").split(",")

conteo = [[[f"A= {secuencia.count('A')},T= {secuencia.count('T')}, C= {secuencia.count('C')}, G= {secuencia.count('G')}"]] for secuencia in secuencias]

print(conteo)