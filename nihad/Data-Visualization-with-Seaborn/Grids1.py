import seaborn as sns
import matplotlib.pyplot as plt


iris = sns.load_dataset('iris')

iris.head()


## PairGrid
# Just the Grid
sns.PairGrid(iris)
plt.show()
# Then you map to the grid
g = sns.PairGrid(iris)
g.map(plt.scatter)
plt.show()
# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
plt.show()
## pairplot

sns.pairplot(iris)
plt.show()
sns.pairplot(iris,hue='species',palette='rainbow')
plt.show()
## Facet Grid

tips = sns.load_dataset('tips')

tips.head()

# Just the Grid
g = sns.FacetGrid(tips, col="time", row="smoker")
plt.show()
g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, "total_bill")
plt.show()
g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Notice hwo the arguments come after plt.scatter call
g = g.map(plt.scatter, "total_bill", "tip").add_legend()
plt.show()
## JointGrid

JointGrid is the general version for jointplot() type grids, for a quick example:

g = sns.JointGrid(x="total_bill", y="tip", data=tips)
plt.show()
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
g = g.plot(sns.regplot, sns.distplot)

plt.show()
