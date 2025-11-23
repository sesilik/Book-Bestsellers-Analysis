# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output folder exists
output_dir = "outputs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load dataset
books = pd.read_csv("bestsellers_with_categories.csv")

# --- Print summaries ---
print("=== First 5 rows ===")
print(books.head())

print("\n=== Info ===")
print(books.info())

print("\n=== Top 10 Authors ===")
print(books['Author'].value_counts().head(10))

print("\n=== Bestseller Count by Genre ===")
print(books['Genre'].value_counts())

print("\n=== Bestsellers per Year ===")
print(books.groupby('Year').size())

print("\n=== Top 10 Books by Reviews ===")
print(books.sort_values('Reviews', ascending=False)[['Name','Author','Reviews','User Rating','Genre']].head(10))

# --- Visualizations ---
sns.set_style("whitegrid")

# Top 10 Authors
plt.figure(figsize=(10,5))
sns.countplot(
    y='Author',
    data=books,
    order=books['Author'].value_counts().head(10).index
)
plt.title("Top 10 Authors by Bestseller Count")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_authors.png"))
plt.show()

# Genre distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Genre', data=books)
plt.title("Bestsellers by Genre")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "genre_distribution.png"))
plt.show()

# Yearly trend of bestsellers
plt.figure(figsize=(10,5))
books.groupby('Year').size().plot(kind='line', marker='o')
plt.title("Number of Bestsellers per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "yearly_trends.png"))
plt.show()

# User Rating vs Reviews scatter
plt.figure(figsize=(8,6))
sns.scatterplot(x='Reviews', y='User Rating', hue='Genre', data=books)
plt.title("User Rating vs Reviews by Genre")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "rating_vs_reviews.png"))
plt.show()

# Average Price by Genre
plt.figure(figsize=(6,4))
books.groupby('Genre')['Price'].mean().plot(kind='bar')
plt.title("Average Price by Genre")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "avg_price_by_genre.png"))
plt.show()

