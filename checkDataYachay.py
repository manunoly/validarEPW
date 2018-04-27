__author__ = 'manuel'
import csv
import codecs
from datetime import datetime

with codecs.open('/media/manuel/DATOS/manuel/ficherosClimaticos/yachay/2016-2017yachayData.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = reader.__next__()
    tmp = reader.__next__()
    horaActual = "00"
    for row in reader:
        print()
        if (row[0].split(" ")[1].split(":")[0]):
            break
        tmpDate = datetime.strptime(tmp[0], '%Y-%m-%d %H:%M:%S')
        resta_fecha = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S') - tmpDate
        if str(resta_fecha) != "0:05:00":
            print(row)
        tmp = row
#        tmp = int(tmp) + 1
#        if tmp[1] != int(row[1]):
#            print (row)"""
