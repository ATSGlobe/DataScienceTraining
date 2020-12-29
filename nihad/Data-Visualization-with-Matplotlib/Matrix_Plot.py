import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head()

flights.head()

tc = tips.corr()

sns.heatmap(tc,annot=True,cmap='coolwarm')
plt.show()

fp = flights.pivot_table(index='month',columns='year',values='passengers')

sns.heatmap(fp)
plt.show()

sns.clustermap(fp,cmap='coolwarm')

plt.show()


