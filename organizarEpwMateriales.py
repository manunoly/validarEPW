__author__ = 'manuel'

from xlrd import open_workbook
import os
from difflib import SequenceMatcher
import shutil

book = open_workbook('/home/manuel/andreitaTest/geovana/ficherosCarpetasOrganizar.xls')
dirFicheros = "/home/manuel/andreitaTest/EPW03-07simulaciones/epw0706"
destino = "/home/manuel/andreitaTest/EPW03-07simulaciones/organizados/"

sheet = book.sheet_by_index(0)


datosExcel = []
for row in xrange(sheet.nrows):
    datosExcel.append(sheet.row_values(row,0,5))
dirs = os.listdir(dirFicheros)
carpetas = []

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

for file in dirs:
    if (file.endswith('.epw')):
        current_file = os.path.join(dirFicheros, file)
        Fichero = file.split("-")[0]
        if (Fichero[file.split("-")[0].__len__()-1:file.split("-")[0].__len__()].isdigit()):
            Fichero = Fichero[:file.split("-")[0].__len__()-1]
        Fichero = Fichero.replace("_"," ")

        for linea in datosExcel:
            if similar(linea[0].encode('utf-8').strip(),Fichero) > 0.9:
                if (linea[4] not in carpetas):
                    carpetas.append(linea[4])
                    if not os.path.exists(destino + str(linea[4])):
                        os.mkdir(destino + str(linea[4]))
                shutil.copy(current_file,destino+str(linea[4]))
                # print str(linea[2])[:4]as

                # print str(datosFichero[7])[:4]
    else:
        print 'Extension No valida'