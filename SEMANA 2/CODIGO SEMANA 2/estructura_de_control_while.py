#Imprimir los números pares menores que 10
num = 0
while num <10:
    print(num)
    num+=2
########## ------------ ###########
#Inicializamos una variable de control
contador =1
#Usamos el bucle while para imprimir los numeros del 1 al 5
while contador<=5:
    print(contador)
    contador +=1
print("fin del bucle")

########### ------- ################
#Definimos la contraseña
contraseña_predeterminada = "secreto123"

#Solicitamos al usuario que ingrese la contraseña
contraseña_ingresada = input("Ingrese la contraseña : ")

"""Utilizamos un bucle while para verficar si la contraseña ingresada coindide con la predeterminada"""
intentos = 2
while contraseña_ingresada != contraseña_predeterminada:
    print("Contraseña incorrecta. intento", intentos)
    contraseña_ingresada = input("Ingrese la contraseña nuevamente : ")
    intentos +2
print("¡Contraseña correcta bienvenido!")