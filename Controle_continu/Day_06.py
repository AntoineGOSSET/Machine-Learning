import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

# Le résultat semble correct si l'on ajoute pas la dernière valeur (mois d'avril)
x=[[03.16], [03.18], [03.20], [03.24], [03.25], [03.26], [03.27], [03.28], [03.30]]
y=[[81682.0], [81720.0], [81760.0], [81826.0], [81844.0], [81864.0], [81881.0], [81900.0], [81933.0]]

#------ Linéaire -------
linearRegressor = LinearRegression()
reg= linearRegressor.fit(x, y)
print("linear regression done")
plt.subplot(211)
plt.scatter(x, y, color = 'red')
plt.plot(x, linearRegressor.predict(x), color = 'blue')
plt.title("Courbe de regression linéaire")

plt.subplot(212)
plt.scatter(x, y - linearRegressor.predict(x), color = 'red')
plt.axhline(0, color='blue')
plt.title("Courbe des résidus")

plt.show()