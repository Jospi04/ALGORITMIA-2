def saludar(nombre):
    """Esta función imprime un saludo personalizado."""
    print("¡Hola,", nombre, "!")
                                                                # Llamada saludar
saludar("Juan")

#Funcion sin parametro
def saludoBienvenida():
    print("BIENVENIDO")

#Funcion con parametro
def saludoNombre(name):
    print("Hola!", name)
    
# Usando las funciones con los argumentos
saludoBienvenida()
saludoNombre("Pedro")

print("----------------------------Boleta electronica----------------------------------------")

def saludoPerzonalizado(nombre,sexo):
    if(sexo=="masculino"):
        print(f"Hola, {nombre} Bienvenido estimado")
    else :
        print(f"Hola, {nombre} Bienvenida señorita")
        
saludoPerzonalizado("Maria", "Femenino")
saludoPerzonalizado("Juan", "Masculino")

print("----------------------------Factura--------------------------------")
def suma(a,b):
    result =a*b
    return result

print (suma(8888888,95959))