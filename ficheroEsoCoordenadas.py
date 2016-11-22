__author__ = 'manuel'

import linecache
import os
import shutil

dirFicherosDuplicados = "/media/manuel/DATOS/manuel/simulaciones/ficherosEsoDupli/"
dirFicherosFaltan = "/media/manuel/DATOS/manuel/simulaciones/ficherosEsoFaltan/"
dirFicherosEso = "/media/manuel/DATOS/manuel/simulaciones/ficherosEso/"
dirFicherosCSV = "/media/manuel/DATOS/manuel/simulaciones/salidaEsoTodosCSV/"

resultados = ["Latitude, Longitude, Elevation, HorasDisconfort"]
duplicados = []
dirs = os.listdir(dirFicherosEso)
for fichero in dirs:
    linecache.cache.clear()
    linea = linecache.getline(dirFicherosEso+fichero,299)
    coordenadas = linea.replace('\n',"").replace(" ","").split(",")
    if coordenadas in duplicados:
        print(fichero + " Fichero duplicado")
        shutil.move(dirFicherosEso + fichero, dirFicherosDuplicados + fichero)
        continue
    else:
        duplicados.append(coordenadas)

    dirFicheroCsv = dirFicherosCSV + "z" + fichero.replace("eso","csv")
    try:
        datosCSV = open(dirFicheroCsv,'r')
    except Exception:
        print(dirFicherosCSV + " Fichero no encontrado")
        # shutil.copy(dirFicherosEso + fichero, dirFicherosFaltan + fichero)
        continue
    lineasCSV = enumerate(datosCSV)
    cantHorasDisconfort = 0
    for i, lineaTmp in lineasCSV:
        if i > 3:
            try:
                tempRM = float(lineaTmp.replace("\r\n","").replace('"',"").split(',')[1])
                tempOperativa = float(lineaTmp.replace("\r\n","").replace('"',"").split(',')[2])
                tempOperativaSuperior = 0.33 * tempRM + 18.8 + 4
                tempOperativaInferior = 0.33 * tempRM + 18.8 - 4
                if (tempOperativa > tempOperativaSuperior or tempOperativa < tempOperativaInferior):
                    cantHorasDisconfort = cantHorasDisconfort + 1
            except Exception:
                print(fichero + "___No se pudo realizar el calculo")
                continue
    resultados.append([coordenadas[2], coordenadas[3], coordenadas[5], cantHorasDisconfort])
    datosCSV.close()
ficheroEscribir = open("/home/manuel/PycharmProjects/validarEPW/horasDisconfort.csv", "w")
for resultadosTmp in resultados:
    ficheroEscribir.write(format(str(resultadosTmp).replace("[","").replace("]","").replace("'","")))
    ficheroEscribir.write(format("\n"))
ficheroEscribir.close()

# for i, resultadosTmp in enumerate(resultados):
#     print(str(i) + str(resultadosTmp))

