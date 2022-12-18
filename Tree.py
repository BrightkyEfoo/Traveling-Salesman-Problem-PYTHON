from random import random


class Tree : 
    def __init__(self, value , filsG = None , filsD = None):
        self.value = value
        self.filsG = filsG
        self.filsD = filsD
    @staticmethod
    def taille(cls,tree):
        '''entrez l'arbre dont vous voulez retrouver la taille'''
        if tree.value:
            return 1 + cls.taille(tree.filsG) + cls.taille(tree.filsD)
        else:
            return 0
    @staticmethod
    def NewTree(value , filsG = None , filsD = None):
        return Tree(value , filsG , filsD)

def prefixe(arbre):
    if arbre == None : 
        return
    else : 
        print(arbre.value)
        prefixe(arbre.filsG)
        prefixe(arbre.filsD)

def infixe(arbre):
    if arbre == None :
        return
    else :
        infixe(arbre.filsG)
        print(arbre.value)
        infixe(arbre.filsD)

def postfixe(arbre):
    if arbre == None :
        return
    else :
        postfixe(arbre.filsG)
        postfixe(arbre.filsD)
        print(arbre.value)

# a5 = Tree(20,
#     Tree(3,Tree(3),Tree(12,Tree(8,Tree(6)),Tree(13))),
#     Tree(25,Tree(21),Tree(28))
#     )
# print('prefixe')
# prefixe(a5)
# print('=========================')

# print('infixe')
# infixe(a5)
# print('=========================')

# print('postfixe')
# postfixe(a5)


#binary trees for searching

def recherche(a , arbre):
    if a== None or a==arbre.value :
        return a
    elif a < arbre.value :
        return recherche(a , arbre.filsG)
    else :
        return recherche(a , arbre.filsD)

def estDans(a , arbre):
    return recherche(a , arbre) != None

def ajouter(a , arbre):
    if arbre == None : 
        a = Tree(a , None, None)
    elif a < arbre.value :
        ajouter(a , arbre.filsG)
    else :
        ajouter(a , arbre.filsD)
    return a

def ajouterSansModif(a , arbre):
    if arbre == None : 
        a = Tree(a , None, None)
    elif a < arbre.value :
        return Tree(a , ajouter(a , arbre.filsG) , arbre.filsD)
    else :
        return Tree(a , arbre.filsG, ajouter(a , arbre.filsD))

def dernierFils(arbre) :
    # retourne le dernier fils d'un arbre (le fils droit le 
    # plus profond)
    if arbre.filsD == None :
        # si l'arbre n'a pas de fils droit alors il est son 
        # dernier fils
        return arbre
    else :
        # sinon on cherche le dernier fils de son fils droit
        #  et ainsi de suite
        return dernierFils(arbre.filsD)

def eliminerRacine(arbre):
    # ici c'est pour eliminer la racine d'un arbre
    if arbre.filsG == None:
        # si il n'a pas de fils gauche 
        # alors l'arbre sans racine c'est juste l'arbre du 
        # fils droi
        return arbre.filsD
    if arbre.filsD == None:
        #egalement s'il n'a pas de filsD
        # alors l'arbre sans racine resultant c'est juste
        #  l'arbre du fils gauche
        return arbre.filsG
    # dans le cas contraire on remplace la valeur de l'arbre actuel 
    # par la valeur du dernier fils de l'arbre du fils gauche 
    # de l'arbre initial et on supprime le dernier fils en question
    # de l'arbre initial, l'arbre obtenu est donc l'arbre sans racine cherché

    b = dernierFils(arbre.filsG)
    arbre.value = b.value
    arbre.filsG = supprimer(arbre.value , arbre.filsG)
    return arbre

def supprimer(a , arbre):
    # ici on veut supprimer un element d'un arbre
    if arbre == None :
        # si l'arbre lui meme est vide alors on le renvoie
        return arbre
    if a == arbre.value :
        # si la valeur a supprimer de l'arbre est celle de la racine
        # alors on elimine la racine de cet arbre
        return eliminerRacine(arbre)
    # sinon on recherche la valeur et on la supprime (de facon recursive)
    if a < arbre.value :
        arbre.filsG = supprimer(a , arbre.filsG)
    else :
        arbre.filsD = supprimer(a , arbre.filsD)
    return arbre


# Matrice d'adjacence
class GrapheMat :
    def __init__(self , n1) :
        self.nb = n1
        self.m =[[None for i in range(n1)] for j in range(n1)]
    
    def __init__(self , n1 , p) :
        self.nb = n1
        self.m =[[None for i in range(n1)] for j in range(n1)]
        for i in range(self.nb) :
            # print(self.m)
            for j in range(self.nb) :
                a = int(p*random())
                if i == j:
                    self.m[i][j] = 0
                elif a == (p-1):
                    self.m[i][j]=1
                else :
                    self.m[i][j]=0
        # print(self.m)

    
    
    # @staticmethod
    def imprimer(self) :
        print(f"nombre de sommets {self.nb}")
        print("  j  0 1 2 3")
        print("i")
        for i in range(self.nb):
            # print(self.m[i])
            tempString = str(i) + "    "
            for j in range(self.nb):
                tempString += str(self.m[i][j])
                tempString += " "
                # print(f"{self.m[i][j]} ")
            print(tempString)
        print("")

graph1 = GrapheMat(4,3)
graph1.imprimer()
# graph1.imprimer(graph1)

class GrapheSucc:

    def __init__(self , n):
        self.nb = n
        self.succ = [[None for i in range(n)] for j in range(n)]
        self.omega = -1
    
    @staticmethod
    def imprimer(self , g):
        print(f"nombre de sommets {g.nb} ")
        for i in range(g.nb):
            j=0
            tempString = ""
            while g.succ[i][j] != self.omega:
                tempString += f"{g.succ[i][j]} "
                j += 1
            print(tempString)
        print("")

class GrapheListe:
    def __init__(self , n1):
        self.nb = n1
        self.listeSucc = [None for i in range(n1)]
    
    @staticmethod
    def imprimer(g):
        # g est un grapheListe
        print(f"nombre de sommets {g.nb}")
        for i in range(g.nb):
            print(f"somment {i} , : successeur : ")
            u = g.listeSucc[i]
            tempString = ""
            while u != None:
                tempString += f" {u.value}"
                u = u.suivant
            print(tempString)
        print("")
