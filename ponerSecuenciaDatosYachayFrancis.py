__author__ = 'manuel'
import csv
import codecs
from datetime import datetime

with codecs.open('/media/manuel/DATOS/manuel/ficherosClimaticos/yachay/data-yachay-2015Francis.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = reader.__next__()
    tmp = reader.__next__()
    fecha = tmp[2]
    datosNuevos = []
    contador = 1
    tmp.append(1)
    datosNuevos.append(tmp)
    contador = contador + 1

    for row in reader:
        if (row[2] == fecha):
            row.append(contador)
            datosNuevos.append(row)
            contador = contador + 1
        else:
            contador = 1
            row.append(contador)
            datosNuevos.append(row)
            fecha = row[2]
            contador = contador + 1

#    for dato in datosPromedio:
#        print(dato)

with open("/media/manuel/DATOS/manuel/ficherosClimaticos/yachay/datosNumeradosFrancis.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(datosNuevos)