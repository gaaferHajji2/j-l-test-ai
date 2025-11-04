import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt

data = datasets.load_iris()

data = pd.DataFrame(
    np.c_[data['data'], data['target']], columns=data['feature_names'] + ['Species'] # type: ignore
)

data['Species'] = data['Species'].astype(int)

print(data.head())

# Settings the color of palette to Greys
sns.displot(
    data, x='Species', discrete = True, hue='Species', shrink =0.8, palette='Greys'
)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(7, 7))
sns.boxplot(ax=axes[0, 0], data=data, x='Species', y = 'sepal length (cm)', hue='Species', palette='Greys')
sns.boxplot(ax=axes[0, 1], data=data, x='Species', y = 'petal length (cm)', hue='Species', palette='Greys')
sns.boxplot(ax=axes[1, 0], data=data, x='Species', y = 'sepal width (cm)', palette='Greys', hue='Species')
sns.boxplot(ax=axes[1,1], data = data,x='Species', y = 'petal width (cm)', palette='Greys', hue='Species')
plt.show()

# define x-y plot (pairplot)
sns.set_theme(
    rc={
        "axes.facecolor":"efefef",
        "figure.facecolor":"efefef"
    }
)

graphxy = sns.pairplot(data=data, hue="Species", palette="Greys")
graphxy.add_legend()
plt.show()