import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import itertools
import operator



A = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5]]

B = [[1, 15], [2, 14], [2, 15], [3, 13], [3, 14], [3, 15], [4, 12], [4, 13], [4, 14], [4, 15], [5, 11], [5, 12], [5, 13], [5, 14], [5, 15], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [6, 15], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14], [7, 15], [8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14], [8, 15], [9, 7], [9, 8], [9, 9], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [9, 15], [10, 6], [10, 7], [10, 8], [10, 9], [10, 10], [10, 11], [10, 12], [10, 13], [10, 14], [10, 15], [11, 5], [11, 6], [11, 7], [11, 8], [11, 9], [11, 10], [11, 11], [11, 12], [11, 13], [11, 14], [11, 15], [12, 4], [12, 5], [12, 6], [12, 7], [12, 8], [12, 9], [12, 10], [12, 11], [12, 12], [12, 13], [12, 14], [12, 15], [13, 3], [13, 4], [13, 5], [13, 6], [13, 7], [13, 8], [13, 9], [13, 10], [13, 11], [13, 12], [13, 13], [13, 14], [13, 15], [14, 2], [14, 3], [14, 4], [14, 5], [14, 6], [14, 7], [14, 8], [14, 9], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [14, 15], [15, 1], [15, 2], [15, 3], [15, 4], [15, 5], [15, 6], [15, 7], [15, 8], [15, 9], [15, 10], [15, 11], [15, 12], [15, 13], [15, 14], [15, 15]]

data = A + B
print(data)
target = [0] * len(A) + [1] * len(B)
print(target)

def generateOvOClassifier(classes):
    o_vs_o_classifiers = {}
    for elem in itertools.combinations(classes,2):
        o_vs_o_classifiers['%d_%d'%elem] = LogisticRegression(solver='lbfgs').fit(data, target)
    return o_vs_o_classifiers

def predictOVO(test_values, o_vs_o_classifiers):
    """
    TO DO : STATS
    """
    results = {}
    i=0
    for elem in test_values:
        intern_result = {}
        for name,classifiers in o_vs_o_classifiers.items():
            result = classifiers.predict([elem[0]])
            members = name.split('_')
            if intern_result.get(members[result[0]]):
                intern_result[members[result[0]]] += 1
            else:
                intern_result[members[result[0]]] = 1
        results[i] = intern_result
        i+=1
    correct = 0
    for key,elem in results.items():
        predicted = max(elem.items(), key=operator.itemgetter(1))[0]
        value = test_values[key][1]
        if int(predicted) == value:
            correct += 1
        #print("Predicted %s and value was %s" %(predicted,value))
    prct = (correct/len(results)*100)
    print(f"The One versus One score a {prct} % precision score ")

if __name__ == "__main__":
    
    classes = set(target)
    #Splitting the data to get train and test sets
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)
    #Create the O v O classifiers
    o_vs_o_classifiers = generateOvOClassifier(classes)
    # We generate an array containing tuples (images,value)
    test_values = [(x_test[index],value) for index, value in enumerate(y_test)]
    # Launch the loop to predict elem in test values 
    predictOVO(test_values, o_vs_o_classifiers)

    # Je suis reparti du la regresssion logistic avec des classifieur OvO mais je n'ai pas réussi à adapter aux données
