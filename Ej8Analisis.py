"""Invente un experimento para verificar que las operaciones de obtención y asignación
de ítems para diccionarios son O(1)O(1).
"""
futbolistas = {
    1 : "Casillas", 15 : "Ramos",
    3 : "Pique", 5 : "Puyol",
    11 : "Capdevila", 14 : "Xabi Alonso",
    16 : "Busquets", 8 : "Xavi Hernandez",
    18 : "Pedrito", 6 : "Iniesta",
    7 : "Villa"
}
print(futbolistas[15])
futbolistas[16]=="Guti"
#Para asignar un elemento de un dicccionario u obtenerlo, el tiempo que se tarda en ejecutar
# el programa es el mismo siempre, sea el elemento que sea, lo que hace que la complejidad sea O(1).