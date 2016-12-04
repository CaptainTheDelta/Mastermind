#mastermind
# coding: utf-8

import random
from fctList import *
from fctMastermind import *


#---------------------Init--------------------
whitePoint = 0
redPoint = 0
nTrial = 0

solution = []

setSolution(solution)                                                       #définition de la solution

AiInput = [-1, -1, -1, -1]                                                  # valeur par défaut

combinaisons = []
getCombinaisons([0,1,2,3,4,5], [], 4, combinaisons)                         # def des combinaisons possibles
combId = list(range(len(combinaisons)))                                     # def des ID des combinaisons possibles
#---------------------------------------------


#-------------------solver--------------------
def getAiInput():
    """
    output : choix d'une combinaison
    """

    a = random.choice(combId)                                               #choix au hasard d'une des valeurs de combId
    trial = list(combinaisons[a])                                           # def de la combinaison à partie de l'id

    for t in trial:                                                         # on affiche la solution
        print(t, end=' ')
    return trial

def learn(trial, red, white):
    """
    élimination des id des combos invalides
    """

    for a in combId[:]:                                                     # pour tous les ids dans une COPIE de combId
        same = sameValueList(combinaisons[a], trial)
                                                                            # on détermine les couleurs ? la m?me position entre 
                                                                            # chaque combinaison (restante) et trial.
        if(not(combinaisons[a] != trial and len(same) == red
            and len(interList(diffList(combinaisons[a],same), diffList(trial,same))) == white)):
                                                                            #condition : la négation de l'assertion (qui valide une combinaison) :
                                                                            # si la combi est diff?rente de celle qui vient d'être testée
                                                                            # ET que le nombre de couleurs à la même place est égale à la correction "point rouge"
                                                                            # ET que parmi les couleurs restantes, le nombre des couleurs semblables
                                                                            #  est égale ? la correction "point blanc".
            combId.remove(a)
                                                                            # si tout le bazar d'au-dessus est faux, on supprime l'id 'a' de combId
                                                                            # comme cette combi ne correspond pas à la correction, on supprime 
                                                                            # le moyen d'y accéder.
#---------------------------------------------


#----------------game loop--------------------
input("start")
while(AiInput != solution):
    nTrial += 1                                                             # on incrémente le compteur de tentatives
    
    AiInput = getAiInput()                                                  # on demande au solver de déterminer une entrée

    (redPoint, whitePoint) = correct(solution, AiInput)                     # on corrige

    print("\tRed : "+str(redPoint)+", white : "+str(whitePoint))
                                                                            # on affiche la solution
    
    if(redPoint == 4):                                                      # 4 rouges => bonne combinaison                                                                 
        print("You find the solution in", nTrial, "trials")
    else:
        learn(AiInput, redPoint, whitePoint)                                 # le solver en tire ses conclusions
input()
#---------------------------------------------