import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

tips = sns.load_dataset('tips')

tips.head()

## distplot

sns.distplot(tips['total_bill'])
plt.show()
sns.distplot(tips['total_bill'],kde=False,bins=30)
plt.show()
## jointplot

sns.jointplot(x='total_bill',y='tip',data=tips,kind='scatter')
plt.show()
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
plt.show()
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
plt.show()
## pairplot

sns.pairplot(tips)
plt.show()
sns.pairplot(tips,hue='sex',palette='coolwarm')
plt.show()
## rugplot

sns.rugplot(tips['total_bill'])
plt.show()
## kdeplot

#Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min,x_max,100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    #Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)
plt.show()
# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")
plt.show()

sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])
plt.show()

sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])
plt.show()
