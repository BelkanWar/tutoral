# reference: https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html

import pandas as pd
import random
from sklearn import datasets
from sklearn.svm import SVC
from sklearn import metrics

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

# random split data into training and validation dataset
# method 1
dataframe = dataframe.sample(frac=1)
train_data = dataframe.iloc[:120]
valid_data = dataframe.iloc[120:]

# method 2
shuffle_idx = [i for i in range(150)]
random.shuffle(shuffle_idx)
dataframe['shuffle'] = shuffle_idx
dataframe = dataframe.sort_values('shuffle')
train_data = dataframe.iloc[:120]
valid_data = dataframe.iloc[120:]

# modeling
model = SVC()
model.fit(train_data[feature_name], train_data['target'])

# model validation
prediction = model.predict(valid_data[feature_name])
truth = valid_data['target']

print('confusion matrix\n', metrics.confusion_matrix(truth, prediction), '\n')
print('precision: ', metrics.precision_score(truth, prediction, average='micro'))
print('recall: ', metrics.recall_score(truth, prediction, average='micro'))
