import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# =============================================================================
# MAIN
# =============================================================================

def main():

    # Définition de 3 pointsavec pour (x,y) : (1,1) (5,2) et (10,6)
    x=[[1], [5], [10]]
    y=[[1], [2], [6]]

    #------ Linéaire -------

    #Initialise une regression lineaire avec les 3 points
    linearRegressor = LinearRegression()
    reg= linearRegressor.fit(x, y)

    # Affiche la refression lineaire dans un graphique
    plt.subplot(211)
    plt.scatter(x, y, color = 'red')
    plt.plot(x, linearRegressor.predict(x), color = 'blue')
    plt.title("Courbe de regression linéaire")

    # Affiche la courbe des résidus dans un graphique
    plt.subplot(212)
    # Détermine le Y comme étant la différence entre les coordées Y réelles et la prédiction de la régression linéaire
    plt.scatter(x, y - linearRegressor.predict(x), color = 'red')
    plt.axhline(0, color='blue')
    plt.title("Courbe des résidus")

    #Affiche le graphique
    plt.show()

# =============================================================================
# SCRIPT INITIATE
# =============================================================================

if __name__ == '__main__':
    main()