# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Setting seaborn style
sns.set(style="whitegrid")

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully!\n")
except Exception as e:
    print("An error occurred while loading the dataset:", e)
    exit()

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# Summary statistics
print("Summary statistics:")
print(df.describe(), "\n")

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum(), "\n")

# Correlation matrix
print("Correlation matrix:")
print(df.corr(), "\n")

# --- Data Visualization ---

# 1. Pairplot
sns.pairplot(df, hue='species')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

# 2. Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='species', y='sepal length (cm)')
plt.title('Sepal Length Distribution by Species')
plt.xlabel('Species')
plt.ylabel('Sepal Length (cm)')
plt.show()

# 3. Histogram
df.hist(figsize=(10, 8), bins=15, edgecolor='black')
plt.suptitle('Feature Distributions')
plt.tight_layout()
plt.show()

# 4. Heatmap of Correlation
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Features')
plt.show()

# --- Findings and Observations ---

print("Findings:")
print("- Sepal length and petal length have a positive correlation.")
print("- Petal measurements (length and width) help distinguish species clearly.")
print("- Setosa species is clearly separable from the others.")
print("- Some overlap between Versicolor and Virginica in petal features.")
