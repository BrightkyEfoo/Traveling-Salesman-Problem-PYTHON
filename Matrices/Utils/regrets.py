# -*-coding:utf-8 -*-
def regrets(Ma):
    # Ma est une matrice
    Mat = Ma.copy()
    l = len(Mat)
    l1 = len(Mat[0])
    Max = 0
    pos = [0,0]
    Res = [[None for j in range(l1)] for i in range(l)]
    Struct = []
    for i in range(l):
        for j in range(l1):
            if Mat[i][j] == 0:
                Res[i][j] = 0
                temp = Mat[i].copy()
                temp.pop(j)
                Res[i][j] += min(temp)
                temp = [Mat[a][j] for a in range(l)]
                temp.pop(i)
                Res[i][j] += min(temp)
                Struct.append({"i":i , "j":j , "value" : Res[i][j]})
                if Res[i][j] > Max:
                    pos[0] = i
                    pos[1] = j
                    Max = Res[i][j]

    return [pos,Res,Struct]

if __name__ == '__main__':
    inf = float('inf')

    A = [
        [inf, 0],
        [8, inf],
    ]



    for el in A:
        print(el)

    [[i,j],RegMat , Struct] = regrets(A)

    print(f'\nRegret max: {RegMat[i][j]} \n position : i-> {i} j-> {j}\n')

    for el in Struct:
        print(el)