# coding: utf-8
def interList(A, B):
    """
    params : 2 listes
    return : élements communs à A et à B
    """

    r = []
    b = list(B)
    for a in A[:]:
        if(a in b):
            r.append(a)
            b.remove(a)
    return r

def sameValueList(A, B):
    """
    params : 2 listes
    return : ensemble des élements communs au même rang
    exemple :  [1,3,3,4]
               [2,3,8,4]
             ->[  3,  4]
    """

    lim = min(len(A),len(B))
    r = []
    for i in range(lim):
        if(A[i] == B[i]):
            r.append(A[i])
    return r

def diffList(A, B):
    """
    params : 2 listes
    return : complémentaire de B dans A (<=> "A-B")
    """

    r = list(A)
    a = list(A)
    for b in B:
        if(b in a):
            r.remove(b)
            a.remove(b)
    return r

def getCombinaisons(listValues, combi, n, all):
    """
    params : params : combinaisons possibles à n chiffres définis par listValues
    output : all : toutes les combinaisons
    """

    if(n <= 0):                                                 #cas final : on ajoute à all
        all.append(combi)
        return

    for i, val in enumerate(listValues):                        # pour chaque valeur, récurrence sur n décroissant
        getCombinaisons(listValues, combi+[val], n-1, all)