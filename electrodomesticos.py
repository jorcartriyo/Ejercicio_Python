class Electrodomesticos():
    # Las he puesto en mayúsculas, porque en el ejercicio dice que tienen que ser constantes
    PRECIOBASE = 100
    COLOR = "Blanco"
    CONSUMOE = "F"
    PESO=5

    def __init__(self,PRECIOBASE=100,COLOR="Blanco",CONSUMOE = "F",PESO=5):
        self.PRESCIOBASE = PRECIOBASE
        self.COLOR = self.comprobarColor(COLOR)
        self.CONSUMOE= self.comprobarconsumoenergetico(CONSUMOE)
        self.PESO = PESO

    def set__precioBase(self,pecioBase):
         self.__precioBase = precioBase

    def get__precioBase(self):
         return self.PRESCIOBASE
    def get__color(self):
         return self.COLOR.upper()
    def get__consumo(self):
         return self.CONSUMOE.upper()
    def get__peso(self):
         return self.PESO
    def A():
        return "A"
    def comprobarconsumoenergetico(self,letra):
        switcher = {
            "A": "A",
            "B": "B",
            "C": "C",
            "D": "D",
            "E": "E",
            "F": "F",
        }
        return switcher.get(letra.upper(), "F")

    def comprobarColor(self,color):
        switcher = {
            "BLANCO":"BLANCO",
            "NEGRO":"NEGRO",
            "ROJO": "ROJO",
            "AZUL": "AZUL",
            "GRIS": "GRIS",
        }
        return switcher.get(color.upper(), "BLANCO")

    def precioFinal(self):
        preciobase=self.PRECIOBASE
        consumo=self.comprobarconsumoenergetico(self.CONSUMOE)
        peso=self.PESO
        if consumo.upper() == "A":
            preciobase=preciobase+100
        if consumo.upper() == "B":
            preciobase=preciobase+80
        if consumo.upper()  == "C":
            preciobase=preciobase+60
        if consumo.upper()  == "D":
            preciobase=preciobase+50
        if consumo.upper()  == "E":
            preciobase=preciobase+30
        if consumo.upper()  == "F":
            preciobase=preciobase+10
        if peso>80:
            preciobase= preciobase + 100
        if peso>50 and peso<79:
            preciobase= preciobase + 80
        if peso>20 and peso<49:
            preciobase= preciobase + 50
        if peso>0and peso<19:
            preciobase= preciobase + 10
        return preciobase
    # print(comprobarColor("rojo"))

# F = electrodomesticos(100,"negro","d",55)
#
# print (F.precioFinal())
# print(F.get__consumo())

class Lavadora(Electrodomesticos):
    CARGA:int
    def __init__(self,CARGA=5,PRECIOBASE=100,COLOR="Blanco",CONSUMOE = "F",PESO=5):
        super().__init__(PRECIOBASE, COLOR, CONSUMOE, PESO)
        self.CARGA = CARGA

    def get__carga(self):
         return self.CARGA

    def precioFinal(self):
        carga = self.CARGA
        preciofinal=Electrodomesticos.precioFinal(self)
        if carga>30:
            preciofinal=preciofinal+50
        else:
            preciofinal = preciofinal
        return preciofinal

# d = Lavadora(60,100,"negro","d",55)
# print (d.precioFinal())


class Television(Electrodomesticos):
    resolucion= 20
    fourK=False

    def __init__(self,resolucion=20,fourK=False,PRECIOBASE=100,COLOR="Blanco",CONSUMOE = "F",PESO=5):
        super().__init__(PRECIOBASE, COLOR, CONSUMOE, PESO)
        self.resolucion=resolucion
        self.fourK=fourK

    def get__resolucion(self):
         return self.resolucion
    def get__fourK(self):
         return self.fourK

    def precioFinal(self):
        resolucion=self.resolucion
        fourK=self.fourK
        preciofinal=Electrodomesticos.precioFinal(self)
        if resolucion>40:
            preciofinal=preciofinal+((preciofinal*30)/100)
        else:
            preciofinal = preciofinal
        if fourK==True:
            preciofinal = preciofinal + 50
        else:
            preciofinal = preciofinal
        return preciofinal
# t = Television(60,True,100,"negro","d",55)
# print (t.precioFinal())



