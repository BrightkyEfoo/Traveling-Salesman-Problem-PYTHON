from Utils.regrets import regrets
from Utils.Produit import affiche as afficheMat , checkIntegrity , MatProduct , tabProd
from Utils.reductionMatrice import estReduite , reduire
from Utils.regrets import regrets
from Utils.removeRawAndCol import removeRawAndCol
from MatForTSP.TSPClass import TSPMat
from Tree.Tree import Tree , postfixe
inf = float('inf')

Mat = [
    [inf, 1, 7, 3, 14, 2],
    [3, inf, 6, 9, 1, 24],
    [6, 14, inf, 3, 7, 3],
    [2, 3, 5, inf, 9, 11],
    [15, 7, 11, 2, inf, 4],
    [20, 5, 13, 4, 18, inf]
]


# Cols = [1, 2, 3, 4, 5, 6]
# Rows = [1, 2, 3, 4, 5, 6]

Cols = ['A', 'B', 'C', 'D', 'E', 'F']
Rows = ['A', 'B', 'C', 'D', 'E', 'F']

# mat1 = TSPMat(Mat, Rows, Cols)
# poids = []
# # pos1 position de la premiere occurence du regret max dans mat1, rm1 valeur du regret max
# [pos1, rm1, Regrets1] = mat1.calculRegrets()
# print(Rows[pos1[0]], ' ', Cols[pos1[1]], '\n')
# poids += [mat1.totalReducs]
#
# mat2 = mat1.suppLigneColonne(pos1[0], pos1[1])
# [pos2, rm2, Regrets2] = mat2.calculRegrets()
# poids += [poids[-1]+mat2.totalReducs]
# print(mat2.Rows[pos2[0]], ' ', mat2.Cols[pos2[1]], '\n')
#
# mat3 = mat2.suppLigneColonne(pos2[0], pos2[1])
# [pos3 , rm3, Regrets3] = mat3.calculRegrets()
# poids += [poids[-1]+mat3.totalReducs]
# print(mat3.Rows[pos3[0]], ' ', mat3.Cols[pos3[1]], '\n')

mats = [TSPMat(Mat, Rows, Cols)]
poids = []
Pos = []
Trees = []
# FGValues = [] # tableaux des filsGauches

for i in range(len(Mat)-1):
    if len(poids) == 0:
        temp = mats[i].totalReducs
        poids = [temp]
        # FGValues = [temp + mats[i].RegretMax]
        T = Tree(temp, Tree(temp + mats[i].RegretMax , None, None), None)
        Trees = [T]
    else:
        poids.append(poids[-1]+mats[i].totalReducs)
        print(poids[-1])
        # FGValues.append(poids[-1] + mats[i].RegretMax)
        T = Tree(poids[-1] , Tree(poids[-1] + mats[i].RegretMax, None , None) , None)
        Trees[-1].filsD = T
        Trees.append(T)
    [pos , a, b] = mats[i].calculRegrets()
    Pos.append(pos)
    mats.append(mats[i].suppLigneColonne(Pos[i][0],Pos[i][1]))



print(TSPMat.Interdits)
lastRoute = TSPMat.Interdits[0]
TSPMat.chemins.append(lastRoute)

print('\n\n\n')
print(TSPMat.chemins)


# postfixe(Trees[0])


print(f'\n{poids}')

refWeight = poids[-1]

Trees.pop(-1)
FGValues = [Trees[i].filsG.value for i in range(len(Trees))]

print(FGValues)
minWeight = min(FGValues)

print(f'cout min = {refWeight}')