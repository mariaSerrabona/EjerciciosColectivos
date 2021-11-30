"""Escriba un algoritmo que permita saber cuál es el día de la semana,
utilizando el siguiente método y después conviértalo a Python:
Conserve las dos últimas cifras del año.
Añada 1/4 de esta cifra, ignorando el resto: división entera.
Añada el día del mes.
Según el mes, añada el valor indicado:
Enero = 1
Febrero = 4
Marzo = 4
Abril = 0
Mayo = 2
Junio = 5
Julio = 0
Agosto = 3
Septiembre = 6
Octubre = 1
Noviembre = 4
Diciembre = 6
Si el año es bisiesto y el mes es enero o febrero, restamos 1.
Según el siglo, añada el valor indicado:
Años 1600 = 6
Años 1700 = 4
Años 1800 = 2
Años 1900 = 0
Años 2000 = 6
Años 2100 = 4
Divida la suma por 7 y guarde el resto: un módulo.
Este resto es el día de la semana buscado.
1 para Domingo
2 para Lunes
3 para Martes
4 para Miércoles
5 para Jueves
6 para Viernes
0 para Sábado
"""
suma = 0
año = int(input("Introduzca las dos ultimas cifras del año "))
suma = año//4
mes = input("Introduzca el mes actual ")
bisiesto = bool(input("Introduzca True si el año es bisiesto o False si no lo es "))
años = int(input("Introduzca un siglo en años "))

if mes == "Enero":
    suma +=1
elif mes == "Febrero":
    suma +=4
elif mes == "Marzo":
    suma +=4
elif mes == "Abril":
    suma +=0
elif mes == "Mayo":
    suma +=2
elif mes == "Junio":
    suma +=5
elif mes == "Julio":
    suma +=0
elif mes == "Agosto":
    suma +=3
elif mes == "Septiembre":
    suma +=6
elif mes == "Octubre":
    suma +=1
elif mes == "Noviembre":
    suma +=4
elif mes == "Diciembre":
    suma +=6

if bisiesto == True and (mes == "Enero" or mes == "Febrero"):
    suma -=1
if años == 1600:
    suma += 6
elif años == 1700:
    suma+=4
elif años == 1800:
    suma+=2
elif años == 1900:
    suma+=0
elif años == 2000:
    suma+=6
elif años == 2100:
    suma+=4

modulo = suma%7
if modulo == 1:
    print("Domingo")
elif modulo == 2:
    print("Lunes")
elif modulo == 3:
    print("Martes")
elif modulo == 4:
    print("Miercoles")
elif modulo == 5:
    print("Jueves")
elif modulo == 6:
    print("Viernes")
elif modulo == 0:
    print("Sabado")
