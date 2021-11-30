"""Escriba una función recursiva para calcular la secuencia de Fibonacci.
¿Cómo se compara el desempeño de la función recursiva con el de una versión iterativa?
"""
def fibonacci(numero):
    if (numero==0 or numero==1):
        return 1
    else:
        return (fibonacci(numero-1)+fibonacci(numero-2))