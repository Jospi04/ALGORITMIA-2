#Ejercicio 01

def soles(s):
    return (3.73)*s
print(soles(2))

#Ejercicio 02

def funcionCal (Cal):
    if Cal>0 and Cal<10:
        print("Malo")
    elif Cal>11 and Cal<=13 :
        print("Regular")
    elif Cal>=14 and Cal<=17:
        print("BMaso")
    elif Cal>=18 and Cal<=20:
        print("Bueno")
    else :
        print("Reprobado")
        
funcionCal(20)

#Ejercicio 03
def funPrem (edad, puntaje):
    if edad>=18 and puntaje <=90:
        print("Premio de primer lugar en la categoria joven/adulta")
    elif edad>=18 and puntaje>=70:
        print("Mecion honorifica juvenil/adulta")
    elif edad>=17 :
        print("Eres menor de edad")
    else :
        print("No recibe premio")
funPrem(25,90)
    
#Ejercicio 04
def funUsuario(contra, usu):
    if contra == "lopez" and usu == "joseph":
        print("ingreso correcto")
        int(input("Desea cambiar la contraseña?"))

    else:
        print("Usuario o contraseña incorrecta")
        
funUsuario("lopez", "joseph")


#Ejercicio 05
def funNombre(*nombre):
    for Varnombre in nombre:
        if Varnombre =="juan":
            continue
        print(Varnombre)
funNombre("pepe", "lulu", "jose","juan", "pipo")


#Ejercicio 06
def funAcumulador (*numeros):
    acumulador = 0
    for valor in numeros :
        acumulador += valor
    return acumulador
print(funAcumulador(1,1,1,1))

#Ejercicio 07