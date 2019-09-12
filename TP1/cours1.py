import numpy as np

A = np.empty # tableau vide
A = np.empty([10]) # tableau vide

A = np.empty([10], dtype=int)
A[0]=2
print(A)

B = np.empty([1, 2, 3, 4 ,5])

C = np.ones([1,3])
D = np.ones(2)
print (C,D)

#help np.zeros
C = np.zeros([2,3,4])
#D = np.zeros(2)
print (C)

print(np.eye(3, dtype=int))

# A partir d'une liste
l=[1,2,4]
print(" ")
print(l)
print(np.array(l))

l=([1,2], [3,4] , [5,6])
print(l)
print (np.array(l))

#Autres
D=np.diag([1,2,4]) #diagonal
print(D)

#Tableaux aleatories
import numpy.random as rd
R = rd.random((3,3))
print(R)

print(np.diag(R))
T1 = np.arange(1,7,1)
print("T1 ", T1)

T1b = np.arange(7)
T1c = np .arange(9, 3 -3)
print(T1b,T1c)

T1 = np.reshape(T1, (2,3))
print(T1)

Tl = np.linspace(0,1,1)
print("Tl", Tl)

X= np.linspace(0,1,6)
Y= np.linspace(-1,1,6)
print(Y)

M = np.meshgrid(X,Y) # WHATR
print(M)

print(T1)
print(T1[0,1])
print([T1[0]])
print(T1[0,:])
print(T1[:,1])

T2 = np.arange(10)
print("T2", T2)
#cases impaires
print("impaire",T2[1:10:2])
print(T2[-1], T2[-3])
#cases impaires
print("impaire",T2[1:-1:2])
print("impaire",T2[1::2])

#cases paires
print("paires",T2[0::2])
print("paires",T2[::2])

#Extraire un bout du tableau
print(T2[3:8:1])
print(T2[3:8:])
print(T2[3:8])

T1b = np.reshape(np.arange(12),(3,4))
print(T1b)

#lignes paires et col impaires
print(T1b[::2, 1::2])

#Quelques outils pour les tableaux
print(T1b)
print("dimension =", T1.ndim, "profil/shape =" , T1.shape)
print(np.arange(2), np.arange(2).shape) #le tuple, soit deux dimension

print("nb ligne =", T1b.shape[0])
print(T1b.size)
print(T1b.dtype)
print(T1b.max())
print(T1b.ndim)

print(T1b.sum())
print(T1b.prod())
print(T1b.transpose())