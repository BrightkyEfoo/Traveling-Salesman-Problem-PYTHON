# resolution du probleme avec une approche naive
from sys import maxsize
from itertools import permutations
v = 4

# implementation du TSP
def TSP(graph, s):

	# stocker tous les sommets à l'exception du sommet source
	V = []
	for i in range(v):
		if i != s:
			V.append(i)

	# stocker le poids minimum du cycle hamiltonien
	chemin_min = maxsize
	prochaine_permutation=permutations(V)
	for i in prochaine_permutation:

		# stocker le poids actuel du chemin (coût)
		poids_chemin_actuel = 0

		# calculer le poids du chemin actuel
		k = s
		for j in i:
			poids_chemin_actuel += graph[k][j]
			k = j
		poids_chemin_actuel += graph[k][s]

		# update minimum
		chemin_min = min(chemin_min, poids_chemin_actuel)
		
	return chemin_min


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 10, 15, 20], [15, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 70, 0]]
	s = 0
	print(TSP(graph, s))
