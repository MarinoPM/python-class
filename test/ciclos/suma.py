
numeros_str = input("Dame 3 números separados por espacio: ").split()
lista_numeros = (list(map(int, numeros_str)))
print(lista_numeros)

suma = sum(lista_numeros)
print(suma)


 