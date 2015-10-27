# coding=utf-8
__author__ = 'MrRubik'


def multiplicacionRecursiva(A, B):
    n = len(A)
    C = crearMatriz(n,0)
    a,b,c,d = partir(A)
    e,f,g,h = partir(B)
    c1  = sumaDeMatrices(algortimoIngenuo(a,e),algortimoIngenuo(b,g))
    c2  = sumaDeMatrices(algortimoIngenuo(a,f),algortimoIngenuo(b,h))
    c3  = sumaDeMatrices(algortimoIngenuo(c,e),algortimoIngenuo(d,g))
    c4  = sumaDeMatrices(algortimoIngenuo(c,f),algortimoIngenuo(d,h))
    copiarMatricesPequenoAgrande(c1,C,0,n/2,0,n/2)
    copiarMatricesPequenoAgrande(c2,C,0,n/2,n/2,n)
    copiarMatricesPequenoAgrande(c3,C,n/2,n,0,n/2)
    copiarMatricesPequenoAgrande(c4,C,n/2,n,n/2,n)
    return C


def sumaDeMatrices(A, B):
    n = len(A)
    C = crearMatriz(n,0)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def algortimoIngenuo(A,B):
    n = len(A)
    C = crearMatriz(n, 0)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + (A[j][k]* B[k][j])
    return C

def copiarMatrices(A,C,tamIniReng, tamFinReng, tamIniCol, tamFinCol):
    n = len(A)

    iaux = 0
    for i in range(tamIniReng,tamFinReng):
        jaux = 0
        for j in range(tamIniCol, tamFinCol):
            C[iaux][jaux] = A[i][j]
            jaux+=1
        iaux+=1

def copiarMatricesPequenoAgrande(A,C,tamIniReng, tamFinReng, tamIniCol, tamFinCol):
    n = len(A)

    iaux = 0
    for i in range(tamIniReng,tamFinReng):
        jaux = 0
        for j in range(tamIniCol, tamFinCol):
            C[i][j] = A[iaux][jaux]
            jaux+=1
        iaux+=1

def partir(A):
    n = len(A)
    a = crearMatriz(n/2,0)
    b = crearMatriz(n/2,0)
    c = crearMatriz(n/2,0)
    d = crearMatriz(n/2,0)

    copiarMatrices(A,a,0,n/2,0,n/2)
    copiarMatrices(A,b,0,n/2,n/2,n)
    copiarMatrices(A,c,n/2,n,0,n/2)
    copiarMatrices(A,d,n/2,n,n/2,n)

    return a,b,c,d

def crearMatriz(n,num):
    M = []
    for i in range(n):
        M.append([num]*n)
    return M

def inicio():
    n = input()
    A = crearMatriz(n,1)
    B = crearMatriz(n,1)
    C = multiplicacionRecursiva(A,B)
    # for i in range(n):
    #    print C[i]


# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#A = crearMatriz(5,2)
#B = crearMatriz(5,2)
#print(sumaDeMatrices(A,B))
inicio()
