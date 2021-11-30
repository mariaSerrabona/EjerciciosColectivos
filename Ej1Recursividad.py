"""Escriba una función recursiva para calcular el factorial de un número.
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)