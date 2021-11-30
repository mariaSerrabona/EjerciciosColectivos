"""El triángulo de Pascal es un triángulo numérico con números dispuestos en filas escalonadas
de manera que  anr=n!r!(n−r)!anr=n!r!(n−r)!
Esta ecuación es la ecuación para un coeficiente binomial.
Usted puede construir el triángulo de Pascal agregando los dos números que están, en diagonal,
encima de un número en el triángulo. A continuación se muestra un ejemplo del triángulo de Pascal.

        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
Escriba un programa que imprima el triángulo de Pascal. Su programa debe aceptar un parámetro
que indique cuántas filas del triángulo se imprimirán.
"""
def trianguloPascal(columna,fila):
    if(columna == 0) or (columna == fila):
        return 1
    else:
        return trianguloPascal(columna-1,fila-1) + trianguloPascal(columna,fila-1)