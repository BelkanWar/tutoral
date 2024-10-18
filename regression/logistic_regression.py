import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from plotly import express
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

spector_data = pd.DataFrame(sm.datasets.spector.load().data)
sns.scatterplot(spector_data, x='GPA', y='GRADE')
plt.show()

fig = express.scatter_3d(spector_data, x='GPA', y='TUCE', z='GRADE')
fig.show()

# build a model using statsmodels
model = smf.glm(formula='GRADE ~ GPA', data=spector_data, family=sm.families.Binomial()).fit()
print(model.summary())

pred_prob = model.predict(spector_data)
spector_data['stats_prob'] = pred_prob

# build a model using sci-kit learn
model = LogisticRegression()
model.fit(spector_data[['GPA']], spector_data['GRADE'])
prediction = model.predict_proba(spector_data[['GPA']])
pred_prob = prediction[:, 1]
spector_data['ml_prob'] = pred_prob

# build a naive bayes model
model = GaussianNB()
model.fit(spector_data[['GPA']], spector_data['GRADE'])
prediction = model.predict_proba(spector_data[['GPA']])
pred_prob = prediction[:, 1]
spector_data['NB'] = pred_prob

# visulization
spector_data = spector_data.sort_values('GPA')
fig, axis = plt.subplots(1, 1)
axis.plot(spector_data['GPA'], spector_data['stats_prob'], color='r')
axis.plot(spector_data['GPA'], spector_data['ml_prob'], color='g')
axis.plot(spector_data['GPA'], spector_data['NB'], color='b')
axis.scatter(spector_data['GPA'], spector_data['GRADE'])
plt.show()
plt.close()