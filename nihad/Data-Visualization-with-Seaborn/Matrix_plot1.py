import seaborn as sns

flights = sns.load_dataset('flights')

tips = sns.load_dataset('tips')

tips.head()

flights.head()

## Heatmap

tips.head()

# Matrix form for correlation data
tips.corr()

sns.heatmap(tips.corr())
plt.show()
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
plt.show()
flights.pivot_table(values='passengers',index='month',columns='year')
plt.show()
pvflights = flights.pivot_table(values='passengers',index='month',columns='year')
sns.heatmap(pvflights)
plt.show()
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)
plt.show()
## clustermap

sns.clustermap(pvflights)
plt.show()
# More options to get the information a little clearer like normalization
sns.clustermap(pvflights,cmap='coolwarm',standard_scale=1)

plt.show()
