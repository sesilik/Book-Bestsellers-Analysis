# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Setup paths ---
data_path = os.path.join("data", "bestsellers_with_categories.csv")
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# --- Load dataset ---
books = pd.read_csv(data_path)

# --- Basic info ---
print("=== First 5 rows ===")
print(books.head(), "\n")

print("=== Dataset Info ===")
print(books.info(), "\n")

print("=== Top 10 Authors ===")
print(books['Author'].value_counts().head(10), "\n")

print("=== Bestseller Count by Genre ===")
print(books['Genre'].value_counts(), "\n")

print("=== Bestsellers per Year ===")
print(books.groupby('Year').size(), "\n")

print("=== Top 10 Books by Reviews ===")
print(books.sort_values('Reviews', ascending=False)[['Name','Author','Reviews','User Rating','Genre']].head(10), "\n")

# --- Visualizations ---
sns.set_style("whitegrid")

# 1️⃣ Top 10 Authors
plt.figure(figsize=(10,5))
sns.countplot(
    y='Author',
    data=books,
    order=books['Author'].value_counts().head(10).index,
    palette='viridis'
)
plt.title("Top 10 Authors by Bestseller Count")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_authors.png"))
plt.show()

# 2️⃣ Genre Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Genre', data=books, palette='pastel')
plt.title("Bestsellers by Genre")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "genre_distribution.png"))
plt.show()

# 3️⃣ Yearly Trend of Bestsellers
plt.figure(figsize=(10,5))
books.groupby('Year').size().plot(kind='line', marker='o', color='tomato')
plt.title("Number of Bestsellers per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "yearly_trends.png"))
plt.show()

# 4️⃣ User Rating vs Reviews
plt.figure(figsize=(8,6))
sns.scatterplot(x='Reviews', y='User Rating', hue='Genre', data=books, s=100, alpha=0.7)
plt.title("User Rating vs Reviews by Genre")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "rating_vs_reviews.png"))
plt.show()

# 5️⃣ Average Price by Genre
plt.figure(figsize=(6,4))
books.groupby('Genre')['Price'].mean().plot(kind='bar', color='skyblue')
plt.title("Average Price by Genre")
plt.ylabel("Average Price ($)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "avg_price_by_genre.png"))
plt.show()

print(f"\n✅ Analysis complete! Plots saved in: {output_dir}/")


