# -*-coding:utf-8 -*-

def MatProduct (A , B):
    # Prends en entree un une matrice A et une Matrice B d'entiers
    # renvoie le produit des deux matrice : A x B
    # renvoie -1 si A n'est pas integre
    # renvoie -2 si B n'est pas integre
    # renvoie -3 si le nombre de colonnes de A est different du nombre de lignes de B
    if not checkIntegrity(A):
        print(f'la matrice A : IntegrityError -1')
        affiche(A)
        print('n\'est pas integre')
        return -1
    elif not checkIntegrity(B):
        print(f'la matrice B : IntegrityError -2')
        affiche(B)
        print('n\'est pas integre')
        return -2
    elif len(A[0]) != len(B):
        print(f'err code : SizeError {-3}')
        print('cant calculate the product of ')
        affiche(A)
        print('and ')
        affiche(B)
        return -3
    else:
        n = len(A)
        m = len(B[0])
        k = len(A[0])
        res = [[None for i in range(m)] for j in range(n)]
        Temp = [None]*m
        for i in range(n):
            for j in range(m):
                if not Temp[j]:
                    Temp[j] = [B[e][j] for e in range(k)]
                res[i][j] = tabProd(A[i],Temp[j],k)
        return res


def checkIntegrity(A):
    # A est une matrice
    if not isinstance(A,list):
        return False
    else:
        for i in range(len(A)):
            if not isinstance(A[i],list):
                return False
            elif len(A[i-1]) != len(A[i]):
                return False
            elif not all(isinstance(item,int) for item in A[i]):
                return False
    return True
def affiche(A):
    # A est une liste
    if not isinstance(A,list) :
        print('err code -3')
        print(f'err {A} n\'est pas une liste')
        return -1
    for i in range(len(A)):
        print(A[i])

def tabProd (A,B,n):
    # A et B sont des tableaux d'entiers
    res = 0
    for i in range(n):
        res += A[i]*B[i]
    return res

if __name__ == '__main__':
    A = [
        [1,2],
        [3,'k'],
        [2,1]
    ]
    B = [
        [5,1,2],
        # [1,1,5]
    ]

    res = MatProduct(A,B)
    if not isinstance(res,list):
        print(f'err {res}')
    else:
        print('le produit de ')
        affiche(A)
        print('et ')
        affiche(B)
        print("est :")
        affiche(res)
