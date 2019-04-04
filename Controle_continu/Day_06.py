import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

def date_to_float(year, month, day) :
    x = datetime(year, month, day)
    return (datetime.timestamp(x))

x=[[date_to_float(2019, 3, 16)], [date_to_float(2019, 3, 18)], [date_to_float(2019, 3, 20)], [date_to_float(2019, 3, 24)], [date_to_float(2019, 3, 25)], [date_to_float(2019, 3, 26)], [date_to_float(2019, 3, 27)], [date_to_float(2019, 3, 28)], [date_to_float(2019, 3, 30)], [date_to_float(2019, 4, 3)]]
y=[[81682.0], [81720.0], [81760.0], [81826.0], [81844.0], [81864.0], [81881.0], [81900.0], [81933.0], [82003.0]]

#------ Linéaire -------
linearRegressor = LinearRegression()
reg= linearRegressor.fit(x, y)

print("Prédiction pour le 2019-04-04 : %s" % (linearRegressor.predict([[date_to_float(2019, 4, 4)]])[0][0]))

plt.subplot(211)
plt.scatter(x, y, color = 'red')
plt.plot(x, linearRegressor.predict(x), color = 'blue')
plt.title("Courbe de regression linéaire")

plt.subplot(212)
plt.scatter(x, y - linearRegressor.predict(x), color = 'red')
plt.axhline(0, color='blue')
plt.title("Courbe des résidus")

plt.show()