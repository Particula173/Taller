import numpy as np

a=np.array([[0,0,0],[0,0,0]])
b=np.array([[0,0,0],[0,0,0]])
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
def normalizacion(v):
  suma=0
  for i in v:
     suma+= (i[0])**2
  norma=(suma**0.5)
  if norma==0:
      return v
  else:
    vector_normal=v/norma
    return vector_normal

def tres(A,v_o):
  A=A
  iteracion_maxima=10000
  iteracion=0
  while iteracion<iteracion_maxima:
      v=A.dot(v_o)
      v= normalizacion(v)
      v_o=v
      iteracion+=1
  return v

matriz=np.array([[-2,1,0],[1,-2,1],[0,1,-2]])
vector0=np.array([[1],[1],[900]])
respuesta_01=tres(matriz,vector0)
Valor=((matriz.dot(respuesta_01))[0])/(vector0[0])
print(Valor*2)
