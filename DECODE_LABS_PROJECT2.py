# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
BASE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(BASE, "charts")
os.makedirs(CHARTS, exist_ok=True)

# load clean Dataset
df= pd.read_csv(os.path.join(BASE, "Cleaned_Dataset1.csv"))

# check data
print(df.isnull().sum())
print(df.duplicated().sum())

# Change datatype of Date
df["Date"]=pd.to_datetime(df["Date"])

# Summarize data
df.info()

# Descriptive Statistics of Data
print("Descriptive Statistics of Data")
print(df.describe())
print(df[["Quantity","UnitPrice","ItemsInCart","TotalPrice"]].agg(["count","mean","median"]))

# Histogram of Quantity
print("Histogram of Quantity")
plt.figure(figsize=(8,6))
sns.histplot(df["Quantity"],discrete=True,color="seagreen",edgecolor="purple")
plt.title("distribution of Quantity")
plt.xlabel("Quantity")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"Quantity_distribution.png"),dpi=300,bbox_inches="tight")
plt.show()

# Histogram of UnitPrice
print("Histogram of UnitPrice")
plt.figure(figsize=(8,6))
sns.histplot(df["UnitPrice"],bins=20,color="orange",edgecolor="purple")
plt.title("distribution of UnitPrice")
plt.xlabel("UnitPrice")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"UnitPrice_distribution.png"),dpi=300,bbox_inches="tight")
plt.show()

# Histogram of ItemsInCart
print("Histogram of ItemsInCart")
plt.figure(figsize=(8,6))
sns.histplot(df["ItemsInCart"],discrete=True,color="lightblue",edgecolor="purple")
plt.title("distribution of ItemsInCart")
plt.xlabel("ItemsInCart")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"ItemsInCart_distribution.png"),dpi=300,bbox_inches="tight")
plt.show()

# Histogram of TotalPrice
print("Histogram of TotalPrice")
plt.figure(figsize=(8,6))
sns.histplot(df["TotalPrice"],bins=20,color="yellow",edgecolor="purple")
plt.title("distribution of TotalPrice")
plt.xlabel("TotalPrice")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"TotalPrice_distribution.png"),dpi=300,bbox_inches="tight")
plt.show()

# Boxplot of TotalPrice
plt.figure(figsize=(6,4))
sns.boxplot(df["TotalPrice"])
plt.title("Boxplot of TotalPrice")
plt.savefig(os.path.join(CHARTS,r"TotalPrice_Boxplot.png"),dpi=300,bbox_inches="tight")
plt.show()

# Outliers detection using IQR Method
Q1=df["TotalPrice"].quantile(0.25)
Q3=df["TotalPrice"].quantile(0.75)

IQR=Q3 - Q1

lower_fence=Q1- (1.5*IQR)
upper_fence=Q3 + (1.5*IQR)

Outliers=df[(df["TotalPrice"]<lower_fence) | (df["TotalPrice"]>upper_fence)]
print("Outliers Detection")
print(len(Outliers))
print(Outliers)
print("Outliers Share of sales (%):",Outliers["TotalPrice"].sum() / df["TotalPrice"].sum() * 100)

# Bar chart of OrderStatus
StatusCount=df["OrderStatus"].value_counts()
print(StatusCount)
print(StatusCount / len(df) * 100)

plt.figure(figsize=(8,6))
plt.bar(StatusCount.index,StatusCount.values,color="firebrick",width=0.5)
plt.title("OrderStatus analysis")
plt.xlabel("OrderStatus")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"OrderStatus_barchart.png"),dpi=300,bbox_inches="tight")
plt.show()

# Bar chart of Product
ProductCount=df["Product"].value_counts()
print(ProductCount)

plt.figure(figsize=(8,6))
plt.bar(ProductCount.index,ProductCount.values,color="teal",width=0.5)
plt.title("Product analysis")
plt.xlabel("Product")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"Product_barchart.png"),dpi=300,bbox_inches="tight")
plt.show()

# Bar chart of PaymentMethod
PaymentCount=df["PaymentMethod"].value_counts()
print(PaymentCount)

plt.figure(figsize=(8,6))
plt.bar(PaymentCount.index,PaymentCount.values,color="steelblue",width=0.5)
plt.title("PaymentMethod analysis")
plt.xlabel("PaymentMethod")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"PaymentMethod_barchart.png"),dpi=300,bbox_inches="tight")
plt.show()

# Bar chart of ReferralSource
ReferralCount=df["ReferralSource"].value_counts()
print(ReferralCount)

plt.figure(figsize=(8,6))
plt.bar(ReferralCount.index,ReferralCount.values,color="indigo",width=0.5)
plt.title("ReferralSource analysis")
plt.xlabel("ReferralSource")
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"ReferralSource_barchart.png"),dpi=300,bbox_inches="tight")
plt.show()


# Trend analysis: Monthly Sales

# Extract Month from Date
df["Month"]=df["Date"].dt.to_period("M")

# Calculate total sales per month
monthly_Sales=df.groupby("Month")["TotalPrice"].sum()

# Line chart of monthly_Sales trend
plt.figure(figsize=(8,6))
monthly_Sales.plot(kind="line")
plt.title("Monthly Sales Trend (2023-2025)")
plt.xlabel("Month")
plt.ylabel("Total sales")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"monthly_Sales_Trend.png"),dpi=300,bbox_inches="tight")
plt.show()

print("Best Month:",monthly_Sales.idxmax(),monthly_Sales.max())
print("Weakest Month:",monthly_Sales.idxmin(),monthly_Sales.min())
print(monthly_Sales.groupby(monthly_Sales.index.year).mean().rename_axis("Year"))
print("Total Sales:",df["TotalPrice"].sum())



# Extract Numerical columns from Data
num_Columns=df.select_dtypes(include="number")
print(num_Columns.corr())

# HeatMap
plt.figure(figsize=(6,5))
sns.heatmap(num_Columns.corr(),annot=True)
plt.title("Correlation HeatMap")
plt.tight_layout()
plt.savefig(os.path.join(CHARTS,r"Correlation_HeatMap.png"),dpi=300,bbox_inches="tight")
plt.show()




