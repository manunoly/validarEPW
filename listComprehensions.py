__author__ = 'manuel'

def testList():
    def imprimir(lista):
        for elemento in lista:
            if isinstance(elemento, list):
                imprimir(elemento)
            else:
                print(elemento)

    lista_anidada = [1, [2, [3, 4, [5, 6], 7]], 8, [9, 10]]
    # imprimir(lista_anidada)
    lista1 = ["2","3","4","5"]
    lista2 = "Asdfasd,asdfs"
    lista3 = [8,2,3,4,5]
    strings = [ "Hola", "mundo", "Juan Perez", "CHAU"]

    def imprimo(i):
        print(i)
    def imprimo2(i):
        print(i)

    [(imprimo(r), imprimo2(r)) for r in lista3]
    for i, var in enumerate(lista1):
        print(str(i) + " " + var)

    tabla = [(x, x*3) for x in range(11) if x% 2 == 0]
    print(tabla)
    exit()
    for x, y in tabla:
        print(x, y)


    def operador(n,m):
           return n+m
    lista1 = [2,3,4,5]
    print(" ".join(lista1))
    tupla1 = (9,8,7,6)
    lista_Resp = map(operador,lista1,tupla1)
    print lista_Resp

    def mi_generador(n, m, s):
        while(n <= m):
            yield n
            n += s

    for n in mi_generador(0, 5, 1):
        print n
    lista = [i for i in range(1, 10) if i%2 == 0]

    # print(lista)




if __name__ == "__main__":
    testList()