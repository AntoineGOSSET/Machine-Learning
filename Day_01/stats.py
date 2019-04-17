import numpy as np
import scipy as sp
import sklearn
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# MAIN
# =============================================================================

def main():
    # Lit le fichier csv Classeur1
    df = pd.read_csv('Classeur1.csv', delimiter= ';')

    # Affiche les différentes statistques générées par panda par commune
    print("Descritpion par commune")
    print(df.describe())

    # Regroupe les communes par région et tri par nombre de redevables
    print("Liste des regions par nombre de redevables")
    print(df.groupby('region').sum().sort_values(by = 'nombre_de_redevables', ascending = False))

    # Affiche les différentes statistques générées par panda par région
    print("Descritpion par regions")
    print(df.groupby('region').sum().sort_values(by = 'nombre_de_redevables', ascending = False).describe())


    region_list = df.groupby('region').sum().sort_values(by = 'nombre_de_redevables', ascending = False).index.values.tolist()

    # Initialise un graphique pyplot
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Créer un palmarès des régions ayant le plus de personnes redevables
    y_pos = np.arange(len(region_list))
    performance = df.groupby('region').sum().sort_values(by = 'nombre_de_redevables', ascending = False).nombre_de_redevables

    ax.barh(y_pos, performance, color='green')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(region_list)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Nombre de redevable')
    ax.set_title('Combien de redevable y a-t-il par région ?')

    # Affiche le graphique
    plt.show()

# =============================================================================
# SCRIPT INITIATE
# =============================================================================

if __name__ == '__main__':
    main()
