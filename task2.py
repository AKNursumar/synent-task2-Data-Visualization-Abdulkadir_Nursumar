import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("iris.csv")

print(df.head())
print(df.columns)

sns.set_style("whitegrid")

# 1. Bar Chart
plt.figure(figsize=(8,5))
sns.countplot(x='species', data=df)
plt.title("Count of Iris Species")
plt.show()

# 2. Histogram
plt.figure(figsize=(8,5))
plt.hist(df['sepal_length'], bins=15)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(
    x='sepal_length',
    y='petal_length',
    hue='species',
    data=df
)
plt.title("Sepal Length vs Petal Length")
plt.show()

# 4. Feature Comparison
sns.pairplot(df, hue='species')
plt.show()