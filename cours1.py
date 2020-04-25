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

#Les tests
"""
if test:
elif test2 : 
else:
"""

#l'indentation est syntaxique -> pas de end
#il est interdit d'ecrire test == true
#elif et else doivent etre omis s'il n'y a rien a faire dans ce cas

#Cas des tableaux
# test sur des taleaux
T = np.reshape(np.arange(6), [2,3])
print(T)

#T==0 est ambigue ! Deux possibilités :
#tester si toutes les casesz sont nulles avec np.all(T==0)
#tester si au moins une case est nulle avec np.any(T==0)

print(np.all(T==0), np.any(T==0))
#False True

#Structure conditionelle case par case
#Syntaxe: np.where(test sur T, operation si vrai, op si faux)
print(T)
#pour tester si div par 2 il faut faire a%2
print(2%2, 1%2)

# pour remplacer toutes les cases par 0
print(T%2==0,T,0)

T1 = rd.random((2,3)) # valeurs entre 0 et 1
T1 = 0.4*rd.random((2,3))+0.6 #entre 0.6 et 1
print(T1,"\n", T2)

#T3 = np.where(T1 < 0.1, T1, T2) # les tavbleaux doivent etre de la meme taille
#print(T3)

Tp = np.where(T1<0.1, "-", "+")
print(Tp)

#Structuration
#script
# Il est possible d ecrire un code dans un script (fichier ) puis de l'executer plusieurs fois
#%run script

""" 
EXEMPLE DE LONG COMMENTAIRE
"""

#Fonctions informatiques

# c'est un bloc reutilisable de code
# elle prends des arguments d'entree et renvoie un argument de sortie
# mais les arguments d'entree peuvent etre un avis un ens vide comme la sortie

# print , np;arange

def nom_fonction(param1,param2):
	# bloc d'instruction
	return resultat

def carre(x):
	return x**2

carre(2)

def print_hello():
	print("Hello")

print_hello()

a = 2
T=np.ones(3)

def mon_un(x):
	x = 1
mon_un(a)
print(a) #affiche 2

def test(x):
	x[0] = 1
	return x.sum()

print(T)
r = test(T)
print("test",r,T)

## Documentation

#Python vient avec une aide intefree. Par ex help(print). Pour chaque fonction vous devez
#(c'est fortement cosneille et valorise) fournir la doc au help

def cube(x):
	"""
	carre'renvoie le cube de x
	"""
	return x**3
help(cube)

"""
arguement optionels
Il est possible de definir une valeur par defaut oiry certaubs arguement
ils doivent etre a la fournirsi on precise leur valeur il faut preciser leur nom"""

def mon_deux(n=5, m=1):
	"""Renvoie un talbeau de 2 (type enteier) a n lignes et m colonne"""
	return np.one([n,m],dtype=int)

mon_deux()
mon_deux(n=2 , m=2)
mon_deux(m=3)
mon_deux(n=3)

#Modules 
Module = bibliotheque en Python

quelques modules standards
time pour manipuler les dates, l'heure 






