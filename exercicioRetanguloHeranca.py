class Forma():
    def __init__(self,area,perimetro):
        self.area=area
        self.perimetro=perimetro

class Retangulo(Forma):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def calculaArea(self):
        print("Area retangulo:",self.base*self.altura)
        self.calcularArea=self.base*self.altura
        self.area=self.calcularArea

    def calculaPerimetro(self):
        print("Perimetro retangulo",self.base*self.altura*2)
        self.calcularPerimetro=self.base*self.altura*2
        self.perimetro=self.calcularPerimetro

class Triangulo(Forma):
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def calculaArea(self):
        print("Area triangulo:",self.base*self.altura/2)



retangulo=Retangulo(10,20)
retangulo.calculaArea()
retangulo.calculaPerimetro()
triangulo=Triangulo(10,30)
triangulo.calculaArea()