dato= int(input())
match dato:
    case 10:
        print("U ingreso 10")
    case 20:
        print("U ingreso 20")
    case 30:
        print("U ingreso 30")
    case _:
        print("No es 10, 20 o 30")

#Swith

def switch_case(dia):
    if dia == 1:
        print("Lunes")
    elif dia ==2:
        print("Martes")
    elif dia ==3:
        print("Miercoles")
    elif dia ==4:
        print("Jueves")
    elif dia ==5:
        print("Viernes")
    elif dia ==6:
        print("Sabado")
    elif dia ==7:
        print("Domingo")
    else :
        print("Número incorrecto")
switch_case(8)