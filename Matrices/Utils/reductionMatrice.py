
def reduire(Ma):
    # Reduit une matrice Ma
    # Renvoie [s , Mat] s etant la somme des reductions et Mat la matrice reduite
    s = 0
    Mat = Ma.copy()
    l = len(Mat) # l nombre ligne
    l1 = len(Mat[0]) # l1 nombre colones
    for i in range(l):
        temp = min(Mat[i])
        s+=temp
        for j in range(l1):
            Mat[i][j] = Mat[i][j] - temp
    
    for i in range(l1):
        m = min([Mat[j][i] for j in range(l)])
        s += m
        for j in range(l):
            Mat[j][i] = Mat[j][i] - m
    
    return [s , Mat]

def estReduite(Mat):
    # prends une Matrice Mat en entree
    # renvoie False si la matrice n'est pas reduite
    #  True sinon
    if not all(min(el)==0 for el in Mat):
        return False
    elif not all(
        min([ Mat[i][j] for i in range( len(Mat) ) ]) == 0 for j in range(len(Mat[0]))):
        return False
    else:
        return True


if __name__=='__main__':
    inf = float('inf')
    A = [
        [inf, 0],
        [8, inf],
    ]



    for el in A:
        print(el)

    print('A est reduite' if estReduite(A) else 'A n est pas reduite')

    [s , B] = reduire(A)


    print(f'\ntotal reductions {s}\n')

    print('matrice reduite :')
    for el in B:
        print(el)

    print('B est reduite' if estReduite(B) else 'B n est pas reduite')
