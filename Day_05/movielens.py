from surprise import KNNWithMeans
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split
import matplotlib.pyplot as plt

# =============================================================================
# MAIN
# =============================================================================

def main():
    # Charge movielens-100k dataset
    data = Dataset.load_builtin('ml-100k')

    # Créer un jeu de test et de train ( 15%, 85%)
    trainset, testset = train_test_split(data, test_size=.15)

    # Détermine l'algorithme utilisé
    algo = KNNWithMeans()

    # Train sur le jeu de donnée trainset
    algo.fit(trainset)
    # Prediction sur le jeu de donnée testset
    predictions = algo.test(testset)

    # Affiche le RMSE
    accuracy.rmse(predictions)

    result =[]
    for prediction in predictions:
        # Calcul le delta entre la prediction et la réalité
        result.append(prediction.r_ui - prediction.est)

    # Affiche l'histogramme du delta entre les predictions et la réalité
    plt.hist(result, 100)

    plt.show()

# =============================================================================
# SCRIPT INITIATE
# =============================================================================

if __name__ == '__main__':
    main()
