__author__ = 'manuel'

import csv


with open('datosAndresCsv.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
     parroquia = ""
     primerosDias = []
     salida = []
     dia = 1
     dia0 = 0
     dia1 = 0
     dia2 = 0
     dia3 = 0
     dia4 = 0
     dia5 = 0
     dia6 = 0
     dia7 = 0
     diaTemp = 0
     diaTempAnt = 0
     nuevo = True

     for row in spamreader:
        # print spamreader.line_num
        if (parroquia != row[0]):
            if (nuevo==False):
                for primeros in primerosDias:
                    diaTempAnt = diaTemp
                    dia1 = dia0
                    dia0 = primeros[2]
                    diaTemp = (0.2 * float(dia1)) + 0.8 * diaTempAnt
                    salida.append(primeros[0] + ' , ' + primeros[1] + ' , ' + str(diaTemp) + ' , ' + str(dia0))

            dia = 1
            dia0 = 0
            dia1 = 0
            dia2 = 0
            dia3 = 0
            dia4 = 0
            dia5 = 0
            dia6 = 0
            dia7 = 0
            diaTemp = 0
            diaTempAnt = 0
            parroquia = row[0]
            nuevo = True
            primerosDias = []

        dia7 = dia6
        dia6 = dia5
        dia5 = dia4
        dia4 = dia3
        dia3 = dia2
        dia2 = dia1
        dia1 = dia0
        dia0 = row[2]
        if(dia > 7):
            if diaTemp > 0:
                diaTempAnt = diaTemp
                diaTemp = (0.2 * float(dia1)) + 0.8 * diaTempAnt
                salida.append(row[0] + ' , ' + row[1] + ' , ' + str(diaTemp) + ' , ' + str(dia0))
            if nuevo:
                # print str(dia1) + '__' + str(dia2) + '__' + str(dia3) + '__' + str(dia4) + '__' + str(dia5) + '__' + str(dia6) + '__' + str(dia7)
                diaTemp = (float(dia1) + 0.8 * float(dia2) + 0.6 * float(dia3) + 0.5 * float(dia4) + 0.4 * float(dia5) + 0.3 * float(dia6)+ 0.2 * float(dia7))/3.8
                nuevo = False
                salida.append(row[0] + ' , ' + row[1] + ' , ' + str(diaTemp) + ' , ' + str(dia0))
        else:
            primerosDias.append(row)
            # print primerosDias
        dia = dia + 1
with open("/home/manuel/PycharmProjects/validarEPW/AndresOutput.csv", "w") as text_file:
    for content in salida:
        text_file.write(format(content))
        text_file.write(format("\n"))