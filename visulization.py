import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import datasets
from plotly import express

iris = datasets.load_iris()

# prepare dataframe
feature_name = iris['feature_names']
dataframe = pd.DataFrame(
    {
        'target': iris['target'],
        'target_name': [iris['target_names'][idx] for idx in iris['target']],
        feature_name[0]: iris['data'][:,0],
        feature_name[1]: iris['data'][:,1],
        feature_name[2]: iris['data'][:,2],
        feature_name[3]: iris['data'][:,3]
    }
)

# use matplotlib drawing 2d distribtion visualization
# reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
fig, axis = plt.subplots(1, 1)
axis.hist([
        dataframe[feature_name[0]], 
        dataframe[feature_name[1]],
        dataframe[feature_name[2]],
        dataframe[feature_name[3]]
    ], bins=20, rwidth=5, label=feature_name)
axis.legend()
plt.show()
plt.close()

# use seaborn drawing 2d distribtion visualization
# reference: https://seaborn.pydata.org/generated/seaborn.displot.html
sns.displot(dataframe, x=feature_name[0], hue='target_name', kind='hist', binwidth=0.3, multiple='dodge')
plt.show()

# 3d distribution visualzation
# reference: https://plotly.com/python/3d-scatter-plots/
fig = express.scatter_3d(dataframe, x=feature_name[0], y=feature_name[1], z=feature_name[2],
              color='target_name')
fig.show()

