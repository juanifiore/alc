import numpy as np

#Ejercicio 3. Escribir funciones de Python que calculen la solución de un sistema:
#(a) Ly = b, siendo L triangular inferior.
#(b) U x = y, siendo U triangular superior.

def resta(L,b,x,i):
    result = b[i]
    for j in range(1,i+1):
        result = result - x[i-j] * L[i][i-j]  
    return result


def sistema_L(L,b):
    x = b.copy()
    x[0] = b[0] / L[0][0]
    for i in range(len(b)):
        for j in range(i):
            x[i] = x[i] - (x[j] * L[i][j]) 
        x[i] = x[i] / L[i][i] 
    return x


L = [[1,0,0],[2,4,0],[3,5,6]]
b = [1,2,3]

rL = sistema_L(L,b)

def sistema_U(L,b):
    x = b.copy()
    x[-1] = b[-1] / L[-1][-1]
    l = len(b)
    for i in range(len(b)):
        for j in range(i):
            x[l-i-1] = x[l-i-1] - (x[-j] * L[i-j-2][j]) 
        x[l-i-1] = x[l-i-1] / L[l-i-1][l-i-1] 
    return x


L = [[1,2,3],[0,4,5],[0,0,6]]
b = [1,2,3]

rU = sistema_U(L,b)
