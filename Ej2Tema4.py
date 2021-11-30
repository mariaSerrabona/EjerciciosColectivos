"""Escriba el mismo algoritmo, pero utilizando dos variables buleanas para comprobar el estado del agua,
sin comparaciones en los SI.
"""
si = True
no = False
def es_gaseoso(temperatura):
    if temperatura>100:
        print("es gaseoso?")
        return si
    else:
        print("es gaseoso?")
        return no
def es_liquido(temperatura):
    if temperatura>=0 and temperatura<=100:
        print("es liquido?")
        return si
    else:
        print("es liquido?")
        return no
def es_solido(temperatura):
    if temperatura<0:
        print("es solido?")
        return si
    else:
        print("es solido?")
        return no
print(es_solido(-2))
print(es_solido(2))