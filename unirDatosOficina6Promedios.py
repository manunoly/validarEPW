__author__ = 'manuel'

import os
import csv

dirFicheros = "/media/manuel/DATOS/manuel/ficherosClimaticos/OficinasIner6/semestreProcesar"
fichero = "/media/manuel/DATOS/manuel/ficherosClimaticos/OficinasIner6/semestreProcesar/datos2016nuevasOficinas.csv"

try:
    os.remove(dirFicheros + '/monthAverage.csv')
    os.remove(dirFicheros + '/dayAverage.csv')
    os.remove(dirFicheros + '/hourAverage.csv')

except OSError:
    pass

dirs = os.listdir(dirFicheros)
monthAverage = [['Temp1','Temp2',"Temp3","Temp4","fecha"]]
dayAverage = [['Temp1','Temp2',"Temp3","Temp4","fecha"]]
hourAverage = [['Temp1','Temp2',"Temp3","Temp4","fecha","hora"]]

with open(fichero, 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
#   this file input has header, it must jump
    print(spamreader.next())
    amountMonth = 0
    amountDay = 0
    amountHour = 0
    tmpMonth = ""
    tmpDay = ""
    tmpHour = ""
    normalRound = False
    for row in spamreader:
        if normalRound:
            if tmpMonth != row[5]:

            if tmpMonth == "":
                tmpMonth = row[4][2:4]
                tmpDay = row[4][4:]
                tmpHour = row[5]
                print(tmpHour)
        else:
            normalRound = True
            tmpMonth = row[4][2:4]
            tmpDay = row[4][4:]
            tmpHour = row[5]

            exit()
        if tmpMonth == row[4][2:4]:



            dataList = row[0].split()
        print()
        # break
exit()
with open(dirFicheros + '/monthAverage.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(finalData)