from Matrices.Utils.reductionMatrice import reduire
from Matrices.Utils.regrets import regrets
from Matrices.Utils.removeRawAndCol import removeRawAndCol as rem
from Matrices.Utils.sensInterdit import sensInterdit

inf = float('inf')
class TSPMat:
    chemins = []
    Interdits = []
    def __init__(self, Mat, Rows, Cols):
        # Mat is a simple matrice
        # Cols reprensente un tableau avec les numero des sommets et Rows aussi
        # il indique les noms de sommets sur les colonnes et sur les lignes

        self.Mat = Mat
        self.Cols = Cols
        # [i+1 for i in range(len(Mat[0]))]
        self.Rows = Rows
        # [i+1 for i in range(len(Mat))]
        # self.coutNiveau = 0
        [a, b] = reduire(self.Mat)
        # a total des reductions
        # b Matrice Reduites

        self.MatReduite = b
        self.totalReducs = a
        [[i,j], M, Struct] = regrets(b)
        self.posRegMax = [i, j]
        self.RegretMax = M[i][j]
        self.Regrets = filter(lambda x: x.get('value') == self.RegretMax, Struct)

    def calculRegrets(self):
        # revoie [ La positon du regretMax, Le regretMax, [toutes les occurences du regretMax] ]
        return [self.posRegMax, self.RegretMax, self.Regrets]
    def reduire(self):
        return [self.MatReduite, self.totalReducs]
    def suppLigneColonne(self, row, col):
        a = rem(self.MatReduite, row, col)
        cols = self.Cols.copy()
        cols.pop(col)
        rows = self.Rows.copy()
        rows.pop(row)
        self.chemins.append([self.Rows[row], self.Cols[col]])
        # print(self.chemins)
        interdits = sensInterdit(self.chemins)
        print(interdits)
        print(f'les interdits ici sont {interdits}')
        self.Interdits.clear()
        self.Interdits += interdits
        print(self.Interdits,'///')
        for el in interdits:
            if el[0] in rows and el[1] in cols:
                a[rows.index(el[0])][cols.index(el[1])] = inf
        return TSPMat(a, rows, cols)
    