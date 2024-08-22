"""Los métodos en python son como
habilidades o acciones que los objetos
pueden realizar, y nos permiten interactuar
con esos objetos de una manera
espeifica según la clase a la
que pertenece"""
#Ejemplo 01
variable_texto ="Hi, I' Joseph"
variable_bienvenia = "Welcome MAQUINA, CRACK, ÍDOLO"
# Sirve para mirar que metodos hay
print(dir(variable_texto))
# Metodos -----------------------------------------
textoMayuscula = variable_texto.upper()
print(variable_texto.upper())                   # UPPER convierte todo en mayuscula
print(textoMayuscula)

textoMayuscula = variable_texto.lower()
print(variable_texto.lower())                   #LOWER convierte todo en minuscula
print(textoMayuscula)

textoMayuscula = variable_texto.capitalize()
print(variable_texto.capitalize())              #CAPITALIZE primera en minuscula
print(textoMayuscula)

varEncontrarTexto = variable_texto.find("Joseph")
print(varEncontrarTexto)                        #FIND metodo para encontrar palabra decir la posición

varEncontrarTexto2 = variable_texto.index("Jo")
print(varEncontrarTexto2)                       #INDEX Parecido al metodo FIND

# num = variable_texto.isnumeric("Joseph")