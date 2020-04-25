import numpy as np
import numpy.random as rd

def Matlap(n):
    
    """Envoie la mtrice du laplacien 2D à n lignes et n colonnes"""
    A = 2*np.eye(n)
    v = np.ones(n-1)
    A -= np.diag(v,1) + np.diag(v, -1)
    return A

def MatSymRand(n):
    "renvoei la matrice symetrice n*n aléatoire"
    A = rd.random_sample((n,n))
    return A+ A.transpose()

if(__name__=="__main__"):
    print("Matrice symétrique aléatoire avec MatSymRand")
    print(" ", MatSymRand(4))
