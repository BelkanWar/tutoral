import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 建立一個單變量資料集
x = np.random.randn(100)
y = x * 0.3 + 5.5 + np.random.randn(100)*0.1

sns.scatterplot(data={'x':x, 'y':y}, x='x', y='y')
plt.show()

# linear regression by sklearn
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x.reshape(-1,1), y)

print(f"slope: {model.coef_[0]} | intercept: {model.intercept_[0]}")

y_pred = model.predict(x.reshape(-1,1))
sns.scatterplot(
    data={
        'x':np.concat((x, x)), 
        'y':np.concat((y, y_pred)),
        'type':['raw data']*x.shape[0] + ['prediction']*x.shape[0]}, 
    x='x', y='y', hue='type')
plt.show()

# 建立一個有連續變量和類別變量的資料集
x = np.random.randn(100)
cat = np.array(['a'] * 50 + ['b'] * 50)
cat_dummy_b = (cat=='b').astype(float)
y = x * 0.3 + x * cat_dummy_b * -1 + 5.5 + cat_dummy_b * -0.5 + np.random.randn(100)*0.1

sns.scatterplot(data={'x':x, 'y':y}, x='x', y='y', hue=cat)
plt.show()