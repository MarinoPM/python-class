
texto = "ATG CGT TAA GGC"
lista = texto.split()
print(lista)

secuencia = "ATG,CGT,TAA,GGC"
lista = secuencia.split(",")
print(lista)

secuencias = "ATG-CGT-TAA-GGC"
lista = secuencias.split("-", 2)
print(lista)