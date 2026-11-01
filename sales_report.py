import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("sales.csv")

sales["total"] = sales["quantity"] * sales["price"]

print("Total sales:", sales["total"].sum())

by_product = sales.groupby("product")["total"].sum()
print(by_product)
print("Best product:", by_product.idxmax())

by_product.plot(kind="bar")
plt.title("Sales by product")
plt.savefig("chart.png")
print("Chart saved")
