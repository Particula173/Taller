import numpy as np

a=np.array([[5,-4,-2],[5,-5,4],[2,5,-4],[-5,4,3],[3,-4,-3]])
b=np.array([5,-2,-3])
c=np.array([[0,-1,-1,3],[5,-5,-2,2],[1,0,4,5]])
d=np.array([[0,-2,3],[-3,-1,-3]])
e=np.array([[2,-5,5,1],[5,2,-7,-6],[-6,-1,7,-4],[5,4,1,-5]])
f=np.array([[0,4,-7,1,-6],[-1,-6,-5,1,1],[2,-1,-6,5,-5],[-3,-6,6,3,5]])
def ausiliary_product (a,b):
    D=np.zeros((a.shape[0],b.shape[1]))
    for i in range(a.shape[0]):
        for z in range(b.shape[1]):
            w=np.dot(a[i],b[:,z])
            D[i][z]=w
    return D
def matriz_ptoduct (a,b):
    if a.shape[1] != b.shape[0]:
        return "Las dimensiones no cuadran"
    if len(b.shape)==1:
        B = b.reshape(-1,1)
        d = (b.shape[0],1)
        return ausiliary_product(a,B)
    else:
        return ausiliary_product(a,b)
    
print(matriz_ptoduct(a,b))
print(matriz_ptoduct(c,d))
print(matriz_ptoduct(e,f))
print("del a). aXb")
print(matriz_ptoduct(a,b))
print("del a). bXa")
print(matriz_ptoduct(b,a))

#Punto 2
MF = np.array([[3,1,-1],[1,-2,1],[4,-1,1]])
MFS = np.array([2,0,3])
MI = np.array([[1,1,1],[0,-8,10],[4,-8,0]])
MIS = np.array([0,0,6])
def sustitucion_atras(M):
    
    n= M.shape[0]
    b= np.zeros(n)
    a= M[:,:n]
    b=M[:,n]
    x= np.zeros(n)

    for i in range(n-1,-1,-1):
        sum = b[i]
        for j in range(n-1,i,-1):
            sum -= a[i,j]*x[j]
        x[i]= sum/a[i,i]

    return x

def eliminacion_y_solucion(a,b):

    n=np.shape(a)[0]
    M= np.zeros(shape=(n,n+1))

    M[:,:n]=a
    M[:,n]=b

    for i in range(n-1):
        Ri=M[i,:]/M[i,i]
        M[i,:]=Ri
        for j in range(i+1,n):
            M[j,:]= M[j,:]-Ri*M[j,i]

    M[-1]=M[-1]/M[-1,n-1]

    return (M, sustitucion_atras(M) )


print("Las fuerzas que se ven presentes en el objeto son:{0}" .format(eliminacion_y_solucion(MF,MFS)[1]))
print("Las corrientes que se ven presentes en el objeto son:{0}" .format(eliminacion_y_solucion(MI,MIS)[1]))

#Punto 3
k = 23
m1 = 13
m2 = 13
m3 = 5

A=np.array([[(-2*k)/m1,k/m1,0.],[k/m2,(-2*k)/m2,k/m2,],[0.,k/m3,(-2*k)/m3]])

b = np.array([1.,1.,3.])


def norma(v):

    s = 0

    for i in range(v.shape[0]):
        s += v[i]**2
    return np.sqrt(s) 

def eigenvalue(A,v,k):

    z = v
    q = z/norma(z)
    Ai= np.linalg.inv(A)

    for i in range(k):
        z = np.dot(Ai,q)
        q = z/norma(z)
        q2 = np.transpose(q)
        sup = np.dot(q2,Ai)
        r = np.dot(q2,sup)
        w=np.sqrt(np.abs(1/r))

    return (-q,w)

v1,e1 = eigenvalue(A,b,90)

w1 = np.sqrt(np.abs(e1))

print(v1,e1)

def ptm(w,A):
    wt = w.T
    p = np.dot(wt,A)
    f = np.dot(p,w)
    return f

def eigenvectors(A,b,k):
    
    z = b
       
    for i in range(k):
        w = z/norma(z)  
        mu =  ptm(w,A)
        z = np.matmul(A,w)
    
    return w,mu

v,e = eigenvectors(A,b,10)

w = np.sqrt(np.abs(e))

print(v,w)
