__author__ = 'manuel'

li = ['a', 'b', 'e']

for el in li:
    print(el)

def recursiva(var):
    if var.__len__() > 2:
        firt = var.pop()

