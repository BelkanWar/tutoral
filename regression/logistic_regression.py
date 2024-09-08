import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from plotly import express

spector_data = pd.DataFrame(sm.datasets.spector.load().data)
sns.scatterplot(spector_data, x='TUCE', y='GRADE')
plt.show()

fig = express.scatter_3d(spector_data, x='GPA', y='TUCE', z='GRADE')
fig.show()