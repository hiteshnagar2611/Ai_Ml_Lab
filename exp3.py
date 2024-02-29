import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Display basic information about the dataset
print("Head of the dataset:")
print(iris.head())

print("\nSummary statistics:")
print(iris.describe())

print("\nInformation about the dataset:")
print(iris.info())

# Visualize the distribution of each feature
sns.pairplot(iris, hue='species', height=2.5)
plt.show()

# Visualize the correlation between features
plt.figure(figsize=(8, 6))
sns.heatmap(iris.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Boxplot for each feature by species
plt.figure(figsize=(10, 6))
for i, column in enumerate(iris.columns[:-1]):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='species', y=column, data=iris)
    plt.title(column)
plt.tight_layout()
plt.show()
