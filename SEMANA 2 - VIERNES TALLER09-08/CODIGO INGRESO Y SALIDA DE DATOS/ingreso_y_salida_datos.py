#Ingreso de datos (entrada estandar)

nombre = input("Por favor, ingresa tu nombre : ")
print("Hola,", nombre, " Bienvenido.")


nombre = input("Por favor, ingresa tu nombre : ")
print("Hola bienvenido", nombre )

#int-float

edad = int(input("Por favor ingresa tu edad : "))
print("El año que viene tendrás", edad+1 , "años.")

##### ---------------------------------------- ####

#Salida de datos con formateo de cadenas

nombre = "Maria"
edad =30
print("Nombre: {} | Edad: {}" .format(nombre, edad))

# O utilizando f-strings
print(f"Nombre: {nombre} | Edad: {edad}")