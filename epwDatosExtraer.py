__author__ = 'manuel'

import os
import csv

dirFicheros = "/home/manuel/andreitaTest/epw/epw"

dirs = os.listdir(dirFicheros)
datos = []
with open("/home/manuel/andreitaTest/epw/Output.csv", "w") as text_file:
    text_file.write(format("Parroquia;Latitud;Longitud;Altura;Anno;Mes;Dia;Hora;Minuto;Temperatura;Precipitacion\n"))
    for file in dirs:
        if (file.endswith('.epw')):
            current_file = os.path.join(dirFicheros, file)
            data = open(current_file,'r')
            Fichero = enumerate(data)
            for i, Fiche in Fichero:
                if i == 0:
                    cabeceras = Fiche.split(",")
                    latitud = cabeceras[6]
                    longitud = cabeceras[7]
                    altura = cabeceras[9].rstrip()
                if i > 7:
                    linea = Fiche.split(",")
                    try:
                        datos = file.replace("-hour.epw","")  + ";" + latitud + ";" + longitud + ";" + altura + ";" + linea[0] + ";" + linea[1] + ";" + linea[2] + ";" + linea[3] + ";" + linea[4] + ";" + linea[6] + ";" + linea[28] + "\n"
                    except Exception:
                        print(file + " " + Fiche)
                        continue
                    text_file.write(format(datos))

#Location Title,Latitude {N+/S-},Longitude {E+/W-},TimeZone {+/- GMT},Elevation {m}