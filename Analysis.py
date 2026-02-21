import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("orders.csv")

print("Total Sales:", df["Total_Amount"].sum())
print("Total Orders:", len(df))

top_products = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)

city_sales = df.groupby("City")["Total_Amount"].sum().sort_values(ascending=False)
print("\nCity Sales:\n", city_sales)

top_products.head(5).plot(kind="bar")

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("Top_Selling_Products.png", dpi=300)

plt.show()