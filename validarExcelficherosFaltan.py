__author__ = 'manuel'

from xlrd import open_workbook

book = open_workbook('/home/manuel/Desktop/datos_parroquiasDuplicadas.xlsx')

sheet = book.sheet_by_index(0)
i = 0
j = 0
col = 0

def buscarOtraColumna(textBuscar):

    print textBuscar
    return True
mayor = ""
for row in xrange(sheet.nrows):
    datoBuscar = sheet.cell_value(row, col).split("-")[0].split("_")
#while sheet.row(i).__len__() > 0:
#    if sheet.row_values(i)[0]:
#        datoBuscar = sheet.row_values(i)[0].split("-")[0].split("_",-1)

#    print sheet.cell_value(row, col).__len__()
    if datoBuscar.__len__() > 1:
        mayor = ""
        for dato in datoBuscar:
            if dato.__len__() > mayor.__len__():
                mayor = dato
    if mayor.__len__() > 1:
        buscarOtraColumna(mayor)
    elif sheet.cell_value(row, col).__len__() > 1:
        buscarOtraColumna(sheet.cell_value(row, col).split("-")[0])
    else:
        continue
    i += 1
print i
print "AAS"
# read header values into the list

