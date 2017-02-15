__author__ = 'manuel'

class aProbar():
    gravatarUrl = ""
    def __init__(self):
        print("Start my code")
    def primerMetodoPrueba(self, correo):
        mailHash = hash(correo).__str__()
        return "https://www.gravatar.com/avatar/" + mailHash


import unittest

class primeraClasePrueba(unittest.TestCase):
    def setUp(self):
        self.aProbar = aProbar()

    def test_primerMetodoPrueba(self):
        gravatarUrl = self.aProbar.primerMetodoPrueba("example1@gmail.com")
        self.assertEquals(gravatarUrl, "https://www.gravatar.com/avatar/1596583901201284426")

if __name__ == "__main__":
    unittest.main()