__author__ = 'Ricardo Ruiz Maldonado'

def insertionSort(A,n):
    for i in range(1,n):
        llave = A[i]
        j = i - 1
        while j >= 0 and llave <= A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = llave
    return A

def creacionArreglo(A,n):
    for i in range(0,n):
        x = input()
        A.append(x)
    return A

A = []
n = input()
creacionArreglo(A,n)
insertionSort(A,n)

