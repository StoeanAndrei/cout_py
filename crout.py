import numpy as np

def Crout(A):
    n = len(A)
    U = np.zeros((n,n))
    L = np.zeros((n,n))
    for i in range(n):
        U[i, i] = 1
        for j in range(i+1):
            sum1 = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = A[i][j] - sum1
        for j in range(i,n):
            sum2 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = (A[i][j] - sum2) / L[i][i]
    return L, U

def LTRIS(L,b):
    n = len(L)
    y = np.zeros((n,1))
    y = b
    for r in range(0,n):
        suml = sum(L[r][c] * y[c] for c in range(0,r))
        y[r] = (b[r] - suml) / L[r][r]
    return y

def UTRIS(U,y):
    n = len(U)
    x = np.zeros((n,1))
    x = y
    x[n-1] = y[n-1] / U[n-1][n-1]
    for r in range(n-2,-1,-1):
        sumu = sum(x[c] * U[r][c] for c in range(n-1,r,-1))
        x[r] = (y[r] - sumu) / U[r][r]
    return x

#n = 4
#A = np.array([[1, 1, -1, -1], [3, -5, 0, 0], [0, 5, 12, 0], [0, 0, -12, 5]])
#n = 3
A = np.array([[1, -1, -1], [1, 15, 0], [0, -15, 9]])
#n = 1
#A = np.array([[20]])
A = np.triu(A, -1)
A = A.astype('float')
#b =  np.array([[0, 3, 12, -5]]).T
b =  np.array([[0, 5, 0]]).T
#b = np.array([[5]]).T
b = b.astype('float')

#sol = np.linalg.inv(np.copy(A))@np.copy(b)

[L, U] = Crout(A)

y = LTRIS(L,b)
x = UTRIS(U,y)

print('---------- x ------------')
print(x)

#print('--------- Sol -----------')
#print(sol)