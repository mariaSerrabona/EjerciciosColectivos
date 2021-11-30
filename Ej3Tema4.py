"""Escriba un algoritmo que determine la categoría deportiva de un usuario en función de su edad:
6 a 7 años: benjamín
8 a 9 años: alevín
10 a 11 años: infantil
12 años y más: cadete
Escriba el programa Python asociado.
"""
edad = int(input("Introduzca su edad en años: "))
if edad<6:
    print("No puede jugar en ninguna categoria")
elif edad == 6 or edad == 7:
    print("Su categoria es benjamin")
elif edad == 8 or edad== 9:
    print("Su categoria es alevin")
elif edad == 10 or edad== 11:
    print("Su categoria es infantil")
elif edad >=12:
    print("Su categoria es cadete")