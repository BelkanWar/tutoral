import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from plotly import express
from sklearn.linear_model import LogisticRegression

spector_data = pd.DataFrame(sm.datasets.spector.load().data)
sns.scatterplot(spector_data, x='TUCE', y='GRADE')
plt.show()

fig = express.scatter_3d(spector_data, x='GPA', y='TUCE', z='GRADE')
fig.show()

# data shuffling
spector_data = spector_data.sample(frac=1)

# build a model using statsmodels
model = smf.glm(formula='GRADE ~ GPA + TUCE + PSI', data=spector_data, family=sm.families.Binomial()).fit()
print(model.summary())
prediction = model.predict(spector_data)

# build a model using sci-kit learn
model = LogisticRegression()
model.fit(spector_data[['GPA', 'TUCE', 'PSI']], spector_data['GRADE'])
prediction = model.predict_proba(spector_data[['GPA', 'TUCE', 'PSI']])