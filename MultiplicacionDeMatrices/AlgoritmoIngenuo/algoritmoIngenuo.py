__author__ = 'MrRubik'

def algortimoIngenuo(A,B):
    C = crearTabla(n,0);
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = C[i][j] + (A[j][k]* B[k][j])
    return C

def crearTabla(n,num):
    M = []
    for i in range(n):
        M.append([num]*n)
    return M

n = input("Cuantas columnas y filas desea?")
A = crearTabla(n,1)
B = crearTabla(n,1)
C = algortimoIngenuo(A,B)
for i in range(n):
    print C[i]

