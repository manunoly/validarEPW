__author__ = 'manuel'

import os

datosParoquias = open("/home/manuel/PycharmProjects/validarEPW/parroquias.csv",'r')
datosDisconfort = open("/home/manuel/PycharmProjects/validarEPW/horasDisconfort.csv",'r')
lineasCSV = datosParoquias.readlines()
lineasDisconfort = datosDisconfort.readlines()
lineasDisconfort.pop(0)
lineasCSV.pop(0)
banderaP = False
resultados = ["nombre,region,latitud,longitud,altura,codigo_parroquia,Latitude, Longitude, Elevation, HorasDisconfort"]
lineasCSV = enumerate(lineasCSV)
parroquiasSinUnion = ["nombre,region,latitud,longitud,altura,codigo_parroquia,Latitude, Longitude, Elevation, HorasDisconfort, Revisar estas Parroquias"]
for lineaD in lineasDisconfort:
    lineaD = lineaD.replace("\n","").replace(" ","")

for i, lineaTmp in lineasCSV:
    datosLineaP = lineaTmp.replace("\r","").replace("\n","").replace(" ","").split(",")
    encontrado = False
    for lineaD in lineasDisconfort:
        lineaD = lineaD.split(",")
        if round(float(datosLineaP[2]),1) == round(float(lineaD[0]),1):
            if round(float(datosLineaP[3]),1) == round(float(lineaD[1]),1):
                if int(float(datosLineaP[4])) == int(float(lineaD[2])):
                    datosLineaP.append(lineaD[0])
                    datosLineaP.append(lineaD[1])
                    datosLineaP.append(lineaD[2])
                    datosLineaP.append(lineaD[3])
                    resultados.append(datosLineaP)
                    encontrado = True
    if not encontrado:
        for lineaD in lineasDisconfort:
            lineaD = lineaD.split(",")
            if int(float(datosLineaP[4])) == int(float(lineaD[2])):
                if round(float(datosLineaP[2]),1) == round(float(lineaD[0]),1) or round(float(datosLineaP[3]),1) == round(float(lineaD[1]),1):
                        datosLineaP.append(lineaD[0])
                        datosLineaP.append(lineaD[1])
                        datosLineaP.append(lineaD[2])
                        datosLineaP.append(lineaD[3])
                        resultados.append(datosLineaP)
        parroquiasSinUnion.append(datosLineaP)


datosParoquias.close()
datosDisconfort.close()
resultados = resultados + parroquiasSinUnion
ficheroEscribir = open("/home/manuel/PycharmProjects/validarEPW/unionParoquiasDisconfort.csv", "w")
for resultadosTmp in resultados:
    ficheroEscribir.write(format(str(resultadosTmp).replace("[","").replace("]","").replace("'","")))
    ficheroEscribir.write(format("\n"))
ficheroEscribir.close()