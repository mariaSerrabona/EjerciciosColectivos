"""Implemente una solución al problema de las torres de Hanoi utilizando tres pilas
para mantener un seguimiento de los discos.
"""
def torres_Hanoi(discos,TorreOrigen=1,TorreAuxiliar=2,TorreDestino=3):
    if discos==1:
        print (TorreOrigen,"a",TorreDestino)
    else:
        torres_Hanoi(discos-1,TorreOrigen,TorreDestino,TorreAuxiliar)
        print(TorreOrigen,"a",TorreDestino)
        torres_Hanoi(discos-1,TorreAuxiliar,TorreOrigen,TorreDestino)
    return