__author__ = 'manuel'

class aProbar():
    gravatarUrl = ""
    def __init__(self):
        print("Running test")

    def primerMetodoPrueba(self, correo):
        mailHash = hash(correo).__str__()
        return "https://www.gravatar.com/avatar/" + mailHash

    def calculaMultiplicacion(self, firt, second):
        return firt * second


import unittest

class primeraClasePrueba(unittest.TestCase):
    def setUp(self):
        self.aProbar = aProbar()

    def test_primerMetodoPrueba(self):
        gravatarUrl = self.aProbar.primerMetodoPrueba("example1@gmail.com")
        self.assertEquals(gravatarUrl, "https://www.gravatar.com/avatar/1596583901201284426")

    def test_matematicalCalculate(self):
        resultado = self.aProbar.calculaMultiplicacion(3,5)
        self.assertEquals(resultado, 15, "Calculo herrado")

if __name__ == "__main__":
    unittest.main()