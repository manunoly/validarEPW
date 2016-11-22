__author__ = 'manuel'

import os

datosParoquias = open("/home/manuel/PycharmProjects/validarEPW/parroquias.csv",'r')
datosDisconfort = open("/home/manuel/PycharmProjects/validarEPW/horasDisconfort.csv",'r')
lineasCSV = datosParoquias.readlines()
lineasDisconfort = datosDisconfort.readlines()
banderaP = False
resultados = []
lineasCSV = enumerate(lineasCSV)
for i, lineaTmp in lineasCSV:
    banderaD = False
    if banderaP:
        datosLineaP = lineaTmp.replace("\r","").replace("\n","").replace(" ","").split(",")
        for lineaD in lineasDisconfort:
            if banderaD:
                lineaD = lineaD.replace("\n","").replace(" ","").split(",")
                if round(float(datosLineaP[2]),1) == round(float(lineaD[0]),1) and round(float(datosLineaP[3]),1) == round(float(lineaD[1]),1) and int(float(datosLineaP[4])) == int(float(lineaD[2])):
                    datosLineaP.append(lineaD[0])
                    datosLineaP.append(lineaD[1])
                    datosLineaP.append(lineaD[2])
                    datosLineaP.append(lineaD[3])
                    print(i)
                    print(datosLineaP)
            else:
                banderaD = True
    else:
        banderaP = True
datosParoquias.close()
datosDisconfort.close()
