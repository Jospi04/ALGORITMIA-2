"""SET, coleccion desordenada de elementos unicos, son mutables,
no permiten elementos duplicdos"""

conjunto = {1,2,3,4,5}
conjunto.add(6) # agrega un elemento
conjunto.remove(3) # eliminar un elemento
print(conjunto) #salida : (1,2,3,4,5)

#No puedes tener un set que contenga otros sets:

set_de_sets = {{1,2}, {3,4}}
#Para lograr el efecto de un set de sets, normalmente se usa una estructura diferente, como una lista de sets:

lista_de_sets = [{1,2},{3,4}]
