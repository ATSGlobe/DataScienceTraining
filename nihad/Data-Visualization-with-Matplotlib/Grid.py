import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
iris.head()

g = sns.PairGrid(iris)
g.map(plt.scatter)

tips = sns.load_dataset('tips')

tips.head()

g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(sns.distplot,'total_bill')

plt.show()
