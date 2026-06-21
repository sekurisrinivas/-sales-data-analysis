#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nBasic stats:")
print(df[["Quantity", "Price"]].describe())
print("\nCategories:", df["Category"].unique())
print("\nCities:", df["City"].unique())


# In[2]:


import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())

df["Revenue"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.month_name()
df["Month_Num"] = df["Date"].dt.month

print("\nNew columns added:")
print(df[["Date", "Quantity", "Price", "Revenue", "Month"]].head())

df.to_csv("sales_data_clean.csv", index=False)
print("\nClean data saved!")
print("Shape:", df.shape)


# In[3]:


import pandas as pd

df = pd.read_csv("sales_data_clean.csv")

print("=" * 45)
print("Q1: Revenue by Category")
print("=" * 45)
cat_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print(cat_revenue.round(2))

print("\n" + "=" * 45)
print("Q2: Revenue by Month")
print("=" * 45)
month_revenue = df.groupby(["Month_Num", "Month"])["Revenue"].sum().reset_index()
month_revenue = month_revenue.sort_values("Month_Num")
print(month_revenue[["Month", "Revenue"]].to_string(index=False))

print("\n" + "=" * 45)
print("Q3: Revenue by City")
print("=" * 45)
city_revenue = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
print(city_revenue.round(2))

print("\n" + "=" * 45)
print("Q4: Average Order Value")
print("=" * 45)
avg_order = df["Revenue"].mean()
print(f"Average order value: Rs {avg_order:.2f}")

print("\n" + "=" * 45)
print("Q5: Payment Method Usage")
print("=" * 45)
payment = df["Payment_Method"].value_counts()
print(payment)

print("\n" + "=" * 45)
print("Q6: Top 5 Products by Revenue")
print("=" * 45)
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
print(top_products.round(2))


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_csv("sales_data_clean.csv")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Sales Dashboard 2024", fontsize=18, fontweight="bold", y=1.01)

cat_rev = df.groupby("Category")["Revenue"].sum().sort_values()
axes[0, 0].barh(cat_rev.index, cat_rev.values, color="#378ADD")
axes[0, 0].set_title("Revenue by Category", fontweight="bold")
axes[0, 0].set_xlabel("Total Revenue (Rs)")
axes[0, 0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x/1000:.0f}K"))
for i, v in enumerate(cat_rev.values):
    axes[0, 0].text(v + 500, i, f"Rs {v/1000:.1f}K", va="center", fontsize=9)

month_rev = df.groupby(["Month_Num", "Month"])["Revenue"].sum().reset_index().sort_values("Month_Num")
axes[0, 1].plot(month_rev["Month"], month_rev["Revenue"], marker="o", color="#1D9E75", linewidth=2.5)
axes[0, 1].set_title("Monthly Revenue Trend", fontweight="bold")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Revenue (Rs)")
axes[0, 1].tick_params(axis="x", rotation=45)
axes[0, 1].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x/1000:.0f}K"))
axes[0, 1].grid(axis="y", linestyle="--", alpha=0.4)

city_rev = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)
axes[1, 0].bar(city_rev.index, city_rev.values, color="#7F77DD")
axes[1, 0].set_title("Revenue by City", fontweight="bold")
axes[1, 0].set_xlabel("City")
axes[1, 0].set_ylabel("Revenue (Rs)")
axes[1, 0].tick_params(axis="x", rotation=45)
axes[1, 0].yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"Rs {x/1000:.0f}K"))
axes[1, 0].grid(axis="y", linestyle="--", alpha=0.4)

payment = df["Payment_Method"].value_counts()
colors = ["#378ADD", "#1D9E75", "#7F77DD", "#EF9F27", "#D85A30"]
axes[1, 1].pie(payment.values, labels=payment.index, autopct="%1.1f%%",
               colors=colors, startangle=140, textprops={"fontsize": 10})
axes[1, 1].set_title("Payment Method Split", fontweight="bold")

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("Chart saved as sales_dashboard.png!")


# In[ ]:




