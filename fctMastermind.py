# coding: utf-8
from fctList import *
import random

def setSolution(solution):
    """
    params : list dans laquelle sera stockée la solution
    output : list 
    """
    
    for n in range(4):
        solution.append(random.randint(0,5))                            # tirage au sort de la solution

def correct(solution, trial):
    redP = 0
    whiteP = 0

    same = sameValueList(solution, trial)                               # les chiffres à la bonne place <=> point rouge
    redP = len(same)

    others = interList(diffList(solution,same), diffList(trial,same))   # diffList permet de récupérer toutes les couleurs qui ne
                                                                        # sont pas à la bonne place, interList récupère les couleurs
                                                                        # en communs <=> bonne couleur mauvaise place <=> point blanc

    whiteP = len(others)

    return (redP,whiteP)