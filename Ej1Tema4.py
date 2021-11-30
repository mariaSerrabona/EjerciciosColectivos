"""Escriba, usando comparaciones, un algoritmo que muestre el estado del agua
(hielo, líquido, vapor) en función de su temperatura.
"""
temperatura = 0
if temperatura<0:
    print("El agua esta en estado solido")
elif temperatura>=0 and temperatura<=100:
    print("El agua esta en estado líquido")
else:
    print("El agua esta en estado gaseoso")