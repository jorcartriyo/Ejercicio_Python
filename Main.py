from random import randint


class Persona():
    __nombre=""
    __edad =0
    __DNI = 0
    __sexo = "M"
    __peso = 0.0
    __altura = 0.0

    def __init__(self,nombre="",edad =0,sexo = "M",peso = 0.0,altura = 0.0):
        try:
            self.__nombre=nombre
            self.__edad=edad
            self.__sexo=sexo
            self.__peso=peso
            self.__altura=altura
            self.__DNI=self.generaDNI()
            self.__sexo=self.introducirSexo(sexo)
        except ValueError:
            print("Tienes que introducir un numero")
    def calcularIMC(self):
        imc=0.0
        if self.__peso==0:
             print("No se puede dividir por 0")
        else:
            imc = round(self.__peso / pow(self.__altura, 2), 2)
        if imc<18.49:
            calculo = -1
        elif imc>18.19 and imc<30:
            calculo = 0
        elif imc>30:
           calculo = 1
        return imc,calculo

    def esMayorDeEdad(self):
        mayorEdad = False
        try:
            if self.__edad>=18:
                mayorEdad= True
            else:
                mayorEdad=False
            return mayorEdad
        except ValueError:
            print("Tienes que introducir un numero")
    def introducirSexo(self,__sexo):
        if __sexo.upper()=="H":
            return "H"
        else:
            return "M"
    def toString(self):
        return "Nombre: "+ self.__nombre, "\nEdad : " + str (self.__edad), "\nDNI: " + str (self.__DNI), "\nSexo: " + self.__sexo, "\nPeso: " + str (self.__peso), "\nAltura: " + str(self.__altura)+'\n'


    def generaDNI(self):
        dni = randint(10000000, 99999999)
        seq = "TRWAGMYFPDXBNJZSQVHLCKE";
        return str(dni) + str(seq[dni % len(seq)])

    def set__nombre(self,nombre):
        self.__nombre = nombre

    def set__edad(self,edad):
         self.__edad = edad

    def set__sexo(self,sexo):
        self.__sexo= self.introducirSexo(sexo)
# arreglar set sexo
    def set__peso(self,peso):
        self.__peso=peso

    def set__altura(self,altura):
         self.__altura = altura

    def get__nombre(self):
         return self.__nombre