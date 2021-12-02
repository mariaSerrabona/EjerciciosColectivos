import random

def buscar(Lista,numero,primero,ultimo):
    Lista.sort()
    return busquedaBinariaRec(Lista,numero,primero,ultimo)

def busquedaBinariaRec(Lista,numero,primero,ultimo):
    puntoMedio = (primero + ultimo)//2
    if(primero>ultimo):
        return -1
    elif(Lista[puntoMedio]==numero):
        return puntoMedio
    else:
        if(Lista[puntoMedio]>numero):
            return busquedaBinariaRec(Lista,numero,primero,puntoMedio-1)
        else:
            return busquedaBinariaRec(Lista,numero,puntoMedio+1,ultimo)


if __name__ == "__main__":
    n=random.randint(6,20)
    m=random.randint(5,10)
    Lista3=[]
    for i in range(0,n*3):
        Lista3.append(i+m)
    random.shuffle(Lista3)
    Lista=Lista3[:n]
    numero=int(input("¿Qué número quieres?: "))
    print(buscar(Lista,numero,0,len(Lista)-1))