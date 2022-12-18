# -*-coding:utf-8 -*-

def removeRawAndCol(Mat , i ,j):
    Res = Mat.copy()
    Res.pop(i)
    for i in range(len(Res)):
        Res[i].pop(j)
    return Res

# print(__name__)
if __name__ == "__main__":
    inf = float('inf')

    A = [
        [inf, 0, 8],
        [0, inf, 0],
        [8, 0, inf],
    ]

    for el in A:
        print(el)
    
    B = removeRawAndCol(A , 0 , 1)
    print('matrice reduite :')
    for el in B:
        print(el)