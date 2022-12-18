from Utils.regrets import regrets
from Utils.Produit import affiche as afficheMat , checkIntegrity , MatProduct , tabProd
from Utils.reductionMatrice import estReduite , reduire
from Utils.regrets import regrets
from Utils.removeRawAndCol import removeRawAndCol
from MatForTSP.TSPClass import TSPMat

inf = float('inf')

Mat = [
    [inf, 780, 320, 580, 480, 660],
    [780, inf, 700, 460, 300, 200],
    [320, 700, inf, 380, 820, 630],
    [580, 460, 380, inf, 750, 310],
    [480, 300, 820, 750, inf, 500],
    [660, 200, 630, 310, 500, inf]
]


# Cols = [1, 2, 3, 4, 5, 6]
# Rows = [1, 2, 3, 4, 5, 6]

Cols = ['B', 'L', 'N', 'P', 'M', 'D']
Rows = ['B', 'L', 'N', 'P', 'M', 'D']

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
for i in range(5):
    if len(poids) == 0:
        poids = [mats[i].totalReducs]
    else:
        poids.append(poids[-1]+mats[i].totalReducs)
    [pos , a, b] = mats[i].calculRegrets()
    Pos.append(pos)
    mats.append(mats[i].suppLigneColonne(Pos[i][0],Pos[i][1]))


print(TSPMat.Interdits)
lastRoute = TSPMat.Interdits[0]
TSPMat.chemins.append(lastRoute)

print('\n\n\n')
print(TSPMat.chemins)

print(f'\n{poids}')

# [a,b] = reduire(Mat)



# print(a , ' reductions')
# afficheMat(b)


# [pos , matRegrets1 , struct1] = regrets(b)

# afficheMat(matRegrets1)
# print()
# afficheMat(struct1)
# print()
# print(pos)
# print()

# afficheMat([checkIntegrity([1])])