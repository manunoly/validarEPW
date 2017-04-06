__author__ = 'manuel'
import os
import argparse

# fields = ["Estacion","voltajeMinimoBateria","temperaturaAirePromedio","humedadAirePromedio","vientoVelocidadPromedio","vientoDireccionPromedio","radiacioSolarPromedioW","radiacioSolarPromedioMJ","presionBarometricaPromedio","nivelSonidoInternoPromedio","nivelSonidoInternoExterno","iluminacion3Promedio","iluminacion7Promedio","dioxidoCarbono3Promedio","dioxidoCarbono6Promedio","dioxidoCarbono7Promedio","termocuplaPromedio1","termocuplaPromedio2","termocuplaPromedio3","termocuplaPromedio4","termocuplaPromedio5","termocuplaPromedio6","termocuplaPromedio7","termocuplaPromedio8","termocuplaPromedio9","termocuplaPromedio10","termocuplaPromedio11","termocuplaPromedio12","termocuplaPromedio13","termocuplaPromedio14","termocuplaPromedio15","termocuplaPromedio16","termocuplaPromedio17","termocuplaPromedio18","termocuplaPromedio19","termocuplaPromedio20","termocuplaPromedio21","termocuplaPromedio22","termocuplaPromedio23","termocuplaPromedio24","termocuplaPromedio25","termocuplaPromedio26","termocuplaPromedio27","termocuplaPromedio28","termocuplaPromedio29","termocuplaPromedio30","termocuplaPromedio31 ","termocuplaPromedio32"]
fields = ["radiacioSolarPromedioW, radiacioSolarPromedioMJ"]
output_dir = "/home/manuel/andreitaTest/yachayVariableSeparadas/"

for field in fields:
    # os.system(query_start + field + " -o " + field + ".csv")
    os.system('''mongoexport --type=csv -d clima -c clima -q '{Estacion : "Yachay"}' -f "fecha",'''+ field + ''' -o ''' + output_dir + field + '''.csv''')