__author__ = 'manuel'

from xlrd import open_workbook
import os

book = open_workbook('/home/manuel/andreitaTest/epw03-07/Amn_altsrtm30.xls')
dirFicheros = "/home/manuel/andreitaTest/epw03-07/epw0706"

sheet = book.sheet_by_index(0)

def buscarOtraColumna(textBuscar):

    print textBuscar
    return True

datosExcel = []
for row in xrange(sheet.nrows):
    datosExcel.append(sheet.row_values(row,0,4))

dirs = os.listdir(dirFicheros)
cant = 0
# print datosExcel
# exit()
ficherosNoCoinciden = []
numero = 0
datosExcelTodos = []
datosExcelRestar = []
for file in dirs:
    numero = numero + 1
    if (file.endswith('.epw')):
        current_file = os.path.join(dirFicheros, file)
        data = open(current_file,'r')
        Fichero = data.readline()
        datosFichero = Fichero.split(",")
        Igual = False
        for linea in datosExcel:
            datosExcelTodos.append(linea[0][:15])
            if datosFichero[1][:15] == linea[0][:15] and str(datosFichero[6])[:4] == str(linea[1])[:4] and str(datosFichero[7])[:4] == str(linea[2])[:4]:
                Igual = True
                datosExcelRestar.append(linea[0][:15])
                # print str(linea[2])[:4]as

                # print str(datosFichero[7])[:4]
                cant += 1
        if not Igual:
            ficherosNoCoinciden.append(datosFichero)
    else:
        print 'Extension No valida '
for datosFichero in ficherosNoCoinciden:
    Igual = False
    for linea in datosExcel:
            if datosFichero[1][:15] == linea[0][:15] and str(datosFichero[6])[:2] == str(linea[1])[:2] and str(datosFichero[7])[:2] == str(linea[2])[:2]:
                Igual = True
                cant += 1
                datosExcelRestar.append(linea[0][:15])
    if not Igual:
        ficheroTMP = datosFichero[1][:15] + '___'+ str(datosFichero[6])[:4] + '___'+ str(datosFichero[7])[:4]
        print ficheroTMP

print

print "El excel contiene " + str(sheet.nrows) + " filas \nLa carpeta contiene " + str(numero) + " de ficheros \nEntre la carpeta y el excel existen " + str(cant) + " epw correctos \nFantando por procesar " + str(list(set(datosExcelTodos) - set(datosExcelRestar)))
# read header values into the list RECINTO BUENA F

