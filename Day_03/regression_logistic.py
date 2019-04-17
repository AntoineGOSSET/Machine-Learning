from PIL import Image
import sklearn as sk
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

""" Ce programme permet de faire un classifieur one vs one à partir des données digits filtrées uniquement sur les 0 et les 1"""

# =============================================================================
# MAIN
# =============================================================================

def main():
    # On stock les données de digits dans une var dataset
    digits_ds = datasets.load_digits()

    # Initialisation des variables
    compteur = len(digits_ds.data)
    myList = []

    myRes_X = []
    myRes_Y = []

    # On récupère les index des objets étant 0 ou 1
    while compteur > 0 :
        if(digits_ds.target[compteur-1]==0 or digits_ds.target[compteur-1]==1) :
            myList.append(compteur-1)
        compteur -= 1

    # A partir de cette liste d'index on boucle pour récuperer les data et les targets
    for i in myList :
        myRes_X.append(digits_ds.data[i])
        myRes_Y.append(digits_ds.target[i])


    # Pour chaques classes on affiche le nombre présent dans notre data
    for i in [0,1] :
        print("classe : %s, nb occurences : %s" % (i, len(digits_ds.target[digits_ds.target == i])))


    # Séparation en listes de test et de train
    x_train, x_test, y_train, y_test = train_test_split(myRes_X, myRes_Y, test_size = 0.33, random_state = 40)

    # Créer deux liste, une avec les 0 et l'une avec les 1
    class0 = [x_train[index] for index, value in enumerate(y_train) if value == 0]
    class1 = [x_train[index] for index, value in enumerate(y_train) if value == 1]

    # Créer une liste contenant des 0 ou des 1 en fonction de leur valeur
    value = [0] * len(class0) + [1] * len(class1)
    # Concatenation des deux listes, 0 et 1
    learn = class0 + class1
    # Créer un classifieur one versus one à partir d'une regression linéaire
    o_vs_o_classifiers = LogisticRegression(solver='lbfgs').fit(learn, value)

    # Créer un jeu de données test
    test_values = [(x_test[index],value) for index, value in enumerate(y_test)]

    # Boucle permettant de predire si la valeur est 0 ou 1 à partir du jeu de test
    for elem in test_values:
        # utilisation du classifieur
        result = o_vs_o_classifiers.predict([elem[0]])
        # Compare si la prédiction correspond au résultats réel
        print("Resultat : ", result)
        print("Attendu :", elem[1])
        if (elem[1]==result):
            print("OK")
        else:
            print("NOK")

# =============================================================================
# SCRIPT INITIATE
# =============================================================================

if __name__ == '__main__':
    main()