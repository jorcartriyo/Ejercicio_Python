from Serie import *
s1=Serie(titulo="El nombre de la Rosa", numeroTemporadas=3, entregado=False, genero="Accion",creador="Pepe Luis")
s2=Serie(titulo="Manolito Gafotas", numeroTemporadas=5, entregado=True, genero="Comedia",creador="Manolo")
s3=Serie(titulo="El destructor", numeroTemporadas=98, entregado=False, genero="Accion",creador="Paco")
s4=Serie(titulo="Perdidos", numeroTemporadas=8, entregado=True, genero="Thriler",creador="Luis")
s5=Serie(titulo="El raton", numeroTemporadas=13, entregado=False, genero="Comedia",creador="Manolo")

v1=VideoJuegos(titulo="Candi cras", horasEstimadas=10, entregado=False, genero="Accion",compania="Pepe")
v2=VideoJuegos(titulo="El caso", horasEstimadas=39, entregado=True, genero="Comedia",compania="ACBT")
v3=VideoJuegos(titulo="Asterix y Obelix", horasEstimadas=78, entregado=False, genero="Accion",compania="SER")
v4=VideoJuegos(titulo="Mortadelo", horasEstimadas=85, entregado=True, genero="Thriler",compania="ERRE")
v5=VideoJuegos(titulo="Mario Bros", horasEstimadas=48, entregado=True, genero="Comedia",compania="DRERE")

listaSerie=[s1,s2,s3,s4,s5]
listaVideoJuegos=[v1,v2,v3,v4,v5]
entreSe=0
dev=0
entreVi=0
devVi=0
numtem=0

# Entrega algunos Videojuegos y Series con el método entregar().
s1.entregar()
v1.entregar()
# Cuenta cuantos Series y Videojuegos hay entregados, Al contarlos, devuélvelos.
for i in listaSerie:
    if i.entregado==True:
        entreSe=entreSe + 1
        print(i.__str__() + " Está entregado")
    else:
        dev=dev+1
        print(i.__str__()  + " No está entregado")
        i.entregar()
        print(i.__str__() + " Ya está entregado")

print("Hay " + str (entreSe) + " series entregadas")
print("Se han devuelto " + str (dev) + " series")

print()
for i in listaVideoJuegos:
    if i.entregado==True:
        print(i.__str__() + " Está entregado")
        entreVi = entreVi + 1
    else:
        devVi=devVi+1
        print(i.__str__()+ " No está entregado")
        i.entregar()
        print(i.__str__() + " Ya está entregado")

print("Hay " + str (entreVi) + " videojuegos entregados)")
print("Se han devuelto " + str (devVi) + " videojuegos")
print()
# indica el Videojuego tiene más horas estimadas y la serie con mas temporadas.
nombre=""
temporadas=0
for i in listaSerie:
    if i.numeroTemporadas>temporadas:
        temporadas=i.numeroTemporadas
        nombre=i.titulo
    else:
        pass
print ("La serie " + nombre + "Tiene " + str(temporadas) + " temporadas y es la que más temporadas tiene")
print()
video=""
horas=0
for i in listaVideoJuegos:
    if i.horasEstimadas>horas:
        horas=i.horasEstimadas
        video=i.titulo
    else:
        pass
print ("La serie " + nombre + "Tiene " + str(temporadas) + " temporadas y es la que más tiene")
print ("El videojuego " + video + " Tiene " + str(horas) + " horas estimadas y es el que más tiene")