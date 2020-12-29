import seaborn as sns
import numpy as np
tips = sns.load_dataset('tips')
tips.head()

## barplot and countplot

sns.barplot(x='sex',y='total_bill',data=tips)
plt.show()

sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
plt.show()
### countplot

sns.countplot(x='sex',data=tips)
plt.show()
## boxplot and violinplot

sns.boxplot(x="day", y="total_bill", data=tips,palette='rainbow')
plt.show()
# Can do entire dataframe with orient='h'
sns.boxplot(data=tips,palette='rainbow',orient='h')
plt.show()

sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")
plt.show()
### violinplot

sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')
plt.show()
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')
plt.show()
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')
plt.show()
## stripplot and swarmplot

sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)
plt.show()
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')
plt.show()
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',split=True)
plt.show()
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()
sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)
plt.show()
### Combining Categorical Plots

sns.violinplot(x="tip", y="day", data=tips,palette='rainbow')
plt.show()
sns.swarmplot(x="tip", y="day", data=tips,color='black',size=3)
plt.show()
## factorplot

sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')
plt.show()

