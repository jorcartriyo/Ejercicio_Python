class Serie():
    titulo=""
    numeroTemporadas=3
    entregado=False
    genero=""
    creador=""

    def __init__(self, titulo="", numeroTemporadas=3, entregado=False, genero="",creador=""):
        self.titulo=titulo
        self.numeroTemporadas=numeroTemporadas
        self.entregado=entregado
        self.genero=genero
        self.creador=creador

    def get__titulo(self):
         return self.titulo
    def get__numeroTemporadas(self):
         return self.numeroTemporadas
    def get__genero(self):
         return self.genero
    def get__creador(self):
         return self.creador

    def set__titulo(self,titulo):
        self.titulo = titulo
    def set__numeroTemporadas(self,numeroTemporadas):
        self.numeroTemporadas= numeroTemporadas
    def set__genero(self,genero):
         self.genero=genero
    def set__creador(self,creador):
        self.creador=creador

    def entregar(self):
        if self.entregado==False:
            self.entregado=True

    # def toString(self):
    #     return "Serie: {0}, {1}".format(self.titulo, self.genero)
    def __str__(self):
        return "Serie: {0}".format(self.titulo)

class VideoJuegos():
    titulo=""
    horasEstimadas=10
    entregado=False
    genero=""
    compania=""
    def __init__(self,titulo="",horasEstimadas=10,entregado=False,genero="",compania=""):
        self.titulo=titulo
        self.horasEstimadas=horasEstimadas
        self.entregado=entregado
        self.genero=genero
        self.compania=compania

    def get__titulo(self):
         return self.titulo
    def get__horasEstimadas(self):
         return self.horasEstimadas
    def get__genero(self):
         return self.genero
    def get__compania(self):
         return self.compania

    def set__titulo(self,titulo):
        self.titulo = titulo

    def set__horasEstimadas(self,horasEstimadas):
        self.horasEstimadas= horasEstimadas

    def set__genero(self,genero):
        self.genero=genero

    def get__compania(self,compania):
        self.compania=compania

    def __str__(self):
        return "Videojuego: {0}".format(self.titulo)

    def entregar(self):
        if self.entregado==False:
            self.entregado=True

