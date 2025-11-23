import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
books = pd.read_csv('bestsellers_with_categories.csv')

# Quick look
print("=== First 5 rows ===")
print(books.head())
print("\n=== Info ===")
print(books.info())

# Top 10 Authors
print("\n=== Top 10 Authors ===")
print(books['Author'].value_counts().head(10))

# Genre distribution
print("\n=== Bestseller Count by Genre ===")
print(books['Genre'].value_counts())

# Yearly trends
print("\n=== Bestsellers per Year ===")
print(books.groupby('Year').size())

# Top 10 books by Reviews
print("\n=== Top 10 Books by Reviews ===")
print(books.sort_values('Reviews', ascending=False).head(10)[['Name','Author','Reviews','User Rating','Genre']])

# Visualizations
sns.set_style("whitegrid")

# Top authors chart
plt.figure(figsize=(10,5))
sns.countplot(y='Author', data=books, order=books['Author'].value_counts().head(10).index)
plt.title("Top 10 Authors by Bestseller Count")
plt.show()

# Genre distribution chart
plt.figure(figsize=(6,4))
sns.countplot(x='Genre', data=books)
plt.title("Bestsellers by Genre")
plt.show()

# Yearly trend chart
plt.figure(figsize=(10,5))
books.groupby('Year').size().plot(kind='line', marker='o')
plt.title("Number of Bestsellers per Year")
plt.show()

