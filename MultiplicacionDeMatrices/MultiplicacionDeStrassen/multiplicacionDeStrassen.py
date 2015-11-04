# coding=utf-8
__author__ = 'MrRubik'


def multiplicacionDeStrassen(A, B):
    if len(A) > 1 and len(B) > 1:
        n = len(A)
        C = crearMatriz(n,0)
        a,b,c,d = partir(A)
        e,f,g,h = partir(B)

        p1 = multiplicacionDeStrassen(a, restaDeMatrices(f,h))
        p2 = multiplicacionDeStrassen(sumaDeMatrices(a,b), h)
        p3 = multiplicacionDeStrassen(sumaDeMatrices(c,d),e)
        p4 = multiplicacionDeStrassen(d, restaDeMatrices(g,e))
        p5 = multiplicacionDeStrassen(sumaDeMatrices(a,d) , sumaDeMatrices(e,h))
        p6 = multiplicacionDeStrassen(restaDeMatrices(b,d),sumaDeMatrices(g,h))
        p7 = multiplicacionDeStrassen(restaDeMatrices(a,c), sumaDeMatrices(e,f))

        r = sumaDeMatrices(restaDeMatrices(sumaDeMatrices(p5,p4), p2),p6)
        s = sumaDeMatrices(p1,p2)
        t = sumaDeMatrices(p3,p4)
        u = restaDeMatrices(restaDeMatrices(sumaDeMatrices(p5,p1),p3),p7)

        copiarMatricesPequenoAgrande(r,C,0,n/2,0,n/2)
        copiarMatricesPequenoAgrande(s,C,0,n/2,n/2,n)
        copiarMatricesPequenoAgrande(t,C,n/2,n,0,n/2)
        copiarMatricesPequenoAgrande(u,C,n/2,n,n/2,n)
        return C
    else:
        C = []
        C.append([A[0][0]*B[0][0]])
        return C

def restaDeMatrices(A, B):
    n = len(A)
    C = crearMatriz(n,0)
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
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
    C = multiplicacionDeStrassen(A,B)
    # for i in range(n):
    #    print C[i]


# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#A = crearMatriz(5,2)
#B = crearMatriz(5,2)
#print(sumaDeMatrices(A,B))
inicio()
