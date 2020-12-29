# Style and Color

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

## Styles
sns.countplot(x='sex',data=tips)
plt.show()
sns.set_style('white')
sns.countplot(x='sex',data=tips)
plt.show()
sns.set_style('ticks')
sns.countplot(x='sex',data=tips,palette='deep')
plt.show()
## Spine Removal

sns.countplot(x='sex',data=tips)
sns.despine()
plt.show()
sns.countplot(x='sex',data=tips)
sns.despine(left=True)
plt.show()
## Size and Aspect
# Non Grid Plot
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)
plt.show()
# Grid Type Plot
sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips)
plt.show()
## Scale and Context

sns.set_context('poster',font_scale=4)
sns.countplot(x='sex',data=tips,palette='coolwarm')
plt.show()
sns.puppyplot()
plt.show()
