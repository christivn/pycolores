## ESTILOS DE TEXTO
class estilo:
    def __init__(self, string):
        self.string=string
    
    def negrita(self):
        self.string="\033[01m"+self.string+"\033[0m"
        return self.string

    def deshabilitado(self):
        self.string="\033[02m"+self.string+"\033[0m"
        return self.string
    
    def subrayado(self):
        self.string="\033[04m"+self.string+"\033[0m"
        return self.string

    def reverso(self):
        self.string="\033[07m"+self.string+"\033[0m"
        return self.string

    def tachado(self):
        self.string="\033[09m"+self.string+"\033[0m"
        return self.string
    
    def invisible(self):
        self.string="\033[08m"+self.string+"\033[0m"
        return self.string


## COLORES DE TEXTO
class color:
    def __init__(self, string):
        self.string=string

    def negro(self):
        self.string="\033[30m"+self.string+"\033[0m"
        return self.string
    
    def rojo(self):
        self.string="\033[31m"+self.string+"\033[0m"
        return self.string

    def verde(self):
        self.string="\033[32m"+self.string+"\033[0m"
        return self.string

    def naranja(self):
        self.string="\033[33m"+self.string+"\033[0m"
        return self.string

    def azul(self):
        self.string="\033[34m"+self.string+"\033[0m"
        return self.string

    def morado(self):
        self.string="\033[35m"+self.string+"\033[0m"
        return self.string

    def cyan(self):
        self.string="\033[36m"+self.string+"\033[0m"
        return self.string

    def gris(self):
        self.string="\033[37m"+self.string+"\033[0m"
        return self.string

    def grisOscuro(self):
        self.string="\033[90m"+self.string+"\033[0m"
        return self.string

    def rojoClaro(self):
        self.string="\033[91m"+self.string+"\033[0m"
        return self.string

    def verdeClaro(self):
        self.string="\033[92m"+self.string+"\033[0m"
        return self.string

    def amarillo(self):
        self.string="\033[93m"+self.string+"\033[0m"
        return self.string

    def azulClaro(self):
        self.string="\033[94m"+self.string+"\033[0m"
        return self.string

    def rosa(self):
        self.string="\033[95m"+self.string+"\033[0m"
        return self.string

    def cyanClaro(self):
        self.string="\033[96m"+self.string+"\033[0m"
        return self.string


## COLORES DE FONDO
class colorFondo:
    def __init__(self, string):
        self.string=string

    def negro(self):
        self.string="\033[40m"+self.string+"\033[0m"
        return self.string

    def rojo(self):
        self.string="\033[41m"+self.string+"\033[0m"
        return self.string

    def verde(self):
        self.string="\033[42m"+self.string+"\033[0m"
        return self.string

    def naranja(self):
        self.string="\033[43m"+self.string+"\033[0m"
        return self.string

    def azul(self):
        self.string="\033[44m"+self.string+"\033[0m"
        return self.string

    def morado(self):
        self.string="\033[45m"+self.string+"\033[0m"
        return self.string

    def cyan(self):
        self.string="\033[46m"+self.string+"\033[0m"
        return self.string

    def gris(self):
        self.string="\033[47m"+self.string+"\033[0m"
        return self.string
