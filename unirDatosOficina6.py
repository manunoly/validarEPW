__author__ = 'manuel'

import os
import csv
mes = '02'
dirFicheros = "/media/manuel/DATOS/manuel/ficherosClimaticos/OficinasIner6/2018/"+mes
try:
    os.remove(dirFicheros + '/some.csv')
except OSError:
    pass

dirs = os.listdir(dirFicheros)
finalData = [['Temp1','Temp2',"Temp3","Temp4","fecha","hora","minuto"]]
# for file in dirs:
#     newDir = dirFicheros + "/" +file
#     newDirFicheros = os.listdir(newDir)
for newFile in dirs:
    # data = open(dirFicheros + "/"+ newFile,'r')
    with open(dirFicheros + "/"+ newFile, 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            dataList = row[0].split()
            tmpData = [dataList[1],dataList[9],dataList[10],dataList[14],dataList[25][:6],dataList[25][6:8],dataList[25][8:10]]
            finalData.append(tmpData)

with open("/media/manuel/DATOS/manuel/ficherosClimaticos/OficinasIner6/2017/juntos/" + '2018-'+mes+'.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(finalData)