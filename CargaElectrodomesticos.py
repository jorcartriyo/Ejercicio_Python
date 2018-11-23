from electrodomesticos import *


a32 =Electrodomesticos(100,"Blanco","F",60)
b15 = Television(60,True,100,"negro","d",25)
b25 = Television(80,False,100,"azul","a",15)
a38 =Lavadora(8,100,"Negro","c",58)
a22 =Electrodomesticos(100,"Azul","a",40)
b13 = Television(60,True,100,"negro","d",25)
b45 = Television(80,False,100,"azul","a",15)
a10 =Lavadora(8,100,"Negro","c",58)
a58 =Lavadora(5,100,"Blanco","F",60)
b63 = Television(60,True,100,"negro","d",25)

listaelect=[a32,b15,b25,a38,a22,b13,b45,a10,a58,b63]
total=0
electr=0
lavad=0
telev=0
nlav=0
nelectr=0
ntelev=0
for i in listaelect:
    if str(i.__class__) == "<class 'electrodomesticos.Electrodomesticos'>":
        electr= i.precioFinal() + electr
        nelectr = nelectr + 1
    if str(i.__class__) == "<class 'electrodomesticos.Lavadora'>":
        lavad= i.precioFinal() + lavad
        nlav=nlav+1
    if str(i.__class__) == "<class 'electrodomesticos.Television'>":
        telev= i.precioFinal() + telev
        ntelev = ntelev + 1
    total = i.precioFinal() + total

print(str(nelectr) + " Electrodomesticos: " + str(electr)+ "€")
print(str(nlav) +  " Lavadoras: " + str(lavad)+ "€")
print(str(ntelev) + " Televisiones: " + str(telev)+ "€")
print("Total en conjunto: " + str(total) + "€")
