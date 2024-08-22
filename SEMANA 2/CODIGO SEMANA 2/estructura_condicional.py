"""
Estructura condicional simple
"""
#Se utiliza para ejecutar un bloque de código si una condición es verdadera. Si la condición es falsa, el bloque de código asociado no se ejecuta. 
edad = 18
if edad >= 18 :
    print("Eres mayor de edad")

"""Estructura condicinal compuesta o doble (if-else)"""

#Permite ejecutar un bloque de código si una condición es verdadera y otro bloque de código si la condición es falsa. 
edad = 18
if edad >= 18 :
    print("Eres mayor de edad")
else :
    print("Eres menor de edad")

"""Estructura condicional múltiple (if.elif-else)"""
#La estructura condicional múltiple se utiliza cuando tienes varias condiciones independientes que quieres evaluar, y quieres ejecutar diferentes bloques de código según cada condición.

opcion = 2
if opcion == 1:
    print("Seleccionaste la opción 1")
elif opcion == 2:
    print("Seleccionaste la opción 2")
elif opcion == 3:
    print("Seleccionaste la opción 3")
else :
    print("Opción no valida")

"""Estructura condicional anidada"""
#La estructura condicional anidada se utiliza cuando necesitas evaluar múltiples condiciones de forma jerárquica, es decir, una dentro de otra. Esto puede ser útil cuando hay diferentes niveles de condiciones que quieres verificar.

edad = 20
sexo = "F"
if edad >= 18:
    if sexo == "F" :
        print("Eres una mujer mayor de edad")
    else :
        print("Eres un hombre mayor de edad")
else :
    print("Eres menor de edad")

"""Estructura condicional combinadas (if and if or if not if else)"""
#Las condicionales combinadas implican el uso de operadores lógicos para combinar múltiples condiciones en una sola expresión condicional y los operadores lógicos más comunes son and, or y not.
rol = "usario"
verificar = True
if (rol == "Admin") and verificar :
    print("Todos los privilegios")
