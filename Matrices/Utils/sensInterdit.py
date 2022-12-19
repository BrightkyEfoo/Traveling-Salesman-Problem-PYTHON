
def sensInterdit(arcs):
    l = len(arcs)
    longsChemins = []
    for i in range(l):
        if not any((arcs[i] in longsChemins[j]) for j in range(len(longsChemins))):
            # je verifie que mon calcul n'a pas deja ete fait en fait.
            longsChemins.append(plusLongChemin(arcs[i], arcs))
    # print(longsChemins)
    res = []
    for i in range(len(longsChemins)):
        if len(longsChemins[i]) == 1:
            [a, b] = longsChemins[i][0]
            res += [[b, a]]
        else:
            temp = longsChemins[i].copy()
            # res += longsChemins[]
            tempV = temp[-1][1]
            temp.pop(-1)

            tempTab = []
            for el in temp:
                for k in range(2):
                    if not el[k] in tempTab:
                        tempTab.append(el[k])

            res += [[tempV, a] for a in tempTab]
    # print(f'res = {res}')
    return res


def prec(arc, arcs):
    temp = filter(lambda x: arc[0] == x[1], arcs)
    temp = list(temp)
    return temp


def suiv(arc, arcs):
    temp = filter(lambda x: arc[1] == x[0], arcs)
    temp = list(temp)
    return temp


def plusLongChemin(arc, arcs):
    m = arc
    chemin = [m]
    while len(prec(m, arcs)) > 0:
        chemin.insert(0, prec(m, arcs)[0])
        m = chemin[0]
    # print(chemin)
    m = arc
    while len(suiv(m, arcs)) > 0:
        chemin.append(suiv(m, arcs)[0])
        m = chemin[-1]
    # print(chemin)
    return chemin


if __name__ == '__main__':
    A = [
        [3, 1],
        [4, 3],
        [5, 6],
        [7, 8]
    ]
    # plusLongChemin([7, 8], A)

    sensInterdit(A)
