#!/usr/bin/python
# coding=utf-8

# A es el arreglo de numeros a ordenar
# n es el numero de elementos del arreglo

def mergeSort(A, n):
    if n == 0 or n == 1:
        return A
    else:
        p = n / 2
        mI, mD = partir(A, p, n)
        mIo = mergeSort(mI, p)
        mDo = mergeSort(mD, n - p)
        aO = mezclar(mIo, mDo, p, n - p)
    return aO


def partir(A, p, n):
    mI = copiar(A, 0, p)
    mD = copiar(A, p, n)
    return mI, mD


def copiar(origen, inicio, fin):
    destino = list(origen[inicio: fin])
    return destino


def mezclar(i, d, ti, td):
    if ti == 0 and td == 0:
        A = []
        return A
    if ti != 0 and td == 0:
        A = copiar(i, 0, ti)
        return A
    if ti == 0 and td != 0:
        A = copiar(d, 0, td)
        return A
    else:
        #ai posicion para el nuevo arreglo ordenado
        #ti tamaño izquierdo
        ai = 0
        ad = 0
        j = 0
        generator = (x for x in range(ti + td - 1))
        A = list(generator)

        while ai < ti and ad < td:
            if i[ai] <= d[ad]:
                A[j] = i[ai]
                ai = ai + 1
            else:
                A[j] = d[ad]
                ad = ad + 1
            j = j + 1

        if ai <= ti:
            A.append(list(i[ai-1:ti]))
        else:
            A.append(copiar(d, ad, td))
        return A


A = [5, 8, 6, 3]
mergeSort(A, 4)
