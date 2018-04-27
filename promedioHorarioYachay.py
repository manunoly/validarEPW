__author__ = 'manuel'
import csv
import codecs
from datetime import datetime

with codecs.open('/media/manuel/DATOS/manuel/ficherosClimaticos/yachay/2016-2017yachayData.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = reader.__next__()
    tmp = reader.__next__()
    horaActual = tmp[0].split(" ")[1].split(":")[0]
    sumaHora = float(tmp[3])
    datosPromedio = []
    cantidadHoras = 1
    ultimaFila = tmp
    for row in reader:
        if (float(row[3]) > 30):
            print(row)
        if (row[0].split(" ")[1].split(":")[0] == horaActual):
            cantidadHoras = cantidadHoras + 1
            sumaHora = sumaHora + float(row[3])
            ultimaFila = row
        else:
            datosPromedio.append([str(cantidadHoras), str(ultimaFila[0]),str(sumaHora/cantidadHoras)])
            horaActual = row[0].split(" ")[1].split(":")[0]
            cantidadHoras = 1
            sumaHora = float(row[3])
            ultimaFila = row

#    for dato in datosPromedio:
#        print(dato)

with open("/media/manuel/DATOS/manuel/ficherosClimaticos/yachay/2016-2017-promedioHorario.csv", 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(datosPromedio)