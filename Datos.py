from Main import Persona

# Pide por teclado el nombre, la edad, sexo, peso y altura.
try:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo: ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    print()
except ValueError:
    print("Tienes que introducir un numero")
    edad =int(input("Edad: "))
# el primer objeto obtendrá las anteriores variables pedidas por teclado


obj1=Persona(nombre,edad,sexo,peso,altura)

# el segundo objeto obtendrá todos los anteriores menos el peso y la altura)
obj2=Persona(nombre,edad,sexo)
# el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
obj3=Persona()
obj3.set__nombre("Manolo")
obj3.set__edad(15)
obj3.set__sexo("z")
obj3.set__peso(95)
obj3.set__altura(1.70)

# método para decir si está en su peso ideal
def pesoIdeal(nom, pesoPersona):
    if pesoPersona== 0:
        return nom + " Está en su peso Ideal"
    elif pesoPersona == -1:
        return nom + " Está por debajo de su peso Ideal"
    elif pesoPersona== 1:
        return nom + " Tiene Sobrepeso"

# método para decir si es mayor de edad
def mayoriaEdad(es):
    if es == True:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

# Para cada objeto, deberá comprobar si esta en su peso ideal,
# el primer objeto
try:
    imc,peso=obj1.calcularIMC()
    print(pesoIdeal(nombre,peso))
    es = obj1.esMayorDeEdad()
    print(mayoriaEdad(es))
    nomb,ed, dn, sex, pes, alt = obj1.toString()
    print (nomb,ed + " años",dn,sex,pes,alt)
except ValueError:
    print("Tienes que introducir un numero")
    edad =int(input("Edad: "))

# el segundo bjeto
imc,peso=obj2.calcularIMC()
print(pesoIdeal(obj2.get__nombre(),peso))
es = obj2.esMayorDeEdad()
print(mayoriaEdad(es))
nomb,ed, dn, sex, pes, alt = obj2.toString()
print(nomb, ed + " años", dn, sex, pes, alt)

# el tercero bjeto
imc,peso=obj3.calcularIMC()
print(pesoIdeal(obj3.get__nombre(),peso))
es = obj3.esMayorDeEdad()
print(mayoriaEdad(es))
nomb,ed, dn, sex, pes, alt = obj3.toString()
print( nomb, ed + " años", dn, sex, pes, alt)
