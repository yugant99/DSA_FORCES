# Import necessary libraries
import matplotlib.pyplot as plt
# Scatter Plot - Base Plot
x = [6,7,8,7,2,3,9,4,10,15,9,7]
y = [98,85,87,88,112,104,87,94,78,78,85,86]
# Basic Scatter Plot
plt.figure(figsize=(5,3))
plt.scatter(x, y)
plt.title("Basic Scatter Plot")
plt.show()
# Scatter Plot with Blue Points
plt.figure(figsize=(5,3))
plt.scatter(x, y, color="blue")
plt.show()
plt.figure(figsize=(5,3))
plt.scatter(x, y, color="coral")
plt.show()
plt.figure(figsize=(5,3))
plt.scatter(x, y, edgecolors="blue", facecolors="gold", marker="s", s=100)
plt.show()
# Load sample datasets
import seaborn as sns
mtcars = sns.load_dataset('mpg').dropna()
iris = sns.load_dataset('iris')
# Scatter plot using seaborn
sns.scatterplot(data=mtcars, x="weight", y="mpg")
plt.show()
sns.scatterplot(data=mtcars, x="weight", y="mpg", color="gold", edgecolor="blue", s=100)
plt.show()
# Histogram of horsepower (using 'horsepower' in seaborn mpg)
plt.figure(figsize=(6,4))
plt.hist(mtcars["horsepower"], bins=12, color="coral")
plt.xlabel("Horsepower")
plt.ylabel("Frequency")
plt.show()
plt.hist(mtcars["horsepower"], bins=12, color="coral", edgecolor="red")
plt.xlabel("Horsepower")
plt.ylabel("Frequency")
plt.show()
# Using alpha (transparency)
plt.figure(figsize=(6,4))
plt.hist(mtcars["horsepower"], bins=12, color="blue", alpha=0.3)
plt.show()
plt.figure(figsize=(6,4))
plt.hist(mtcars["horsepower"], bins=12, color="blue", alpha=0.3, edgecolor="blue")
plt.show()
# Line Plot (with Color Coding for Iris Dataset)
# Line Plot - Sepal Length vs Sepal Width
plt.figure(figsize=(7,5))
sns.lineplot(data=iris, x="sepal_length", y="sepal_width", hue="species")
plt.show()
# Custom colors
custom_palette = {"setosa": "darkorange", "versicolor": "green", "virginica": "red"}
plt.figure(figsize=(7,5))
sns.lineplot(data=iris, x="sepal_length", y="sepal_width", hue="species", palette=custom_palette)
plt.show()