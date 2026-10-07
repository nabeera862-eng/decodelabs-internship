# import library
import pandas as pd

# load dataset
df=pd.read_csv(r"D:\python\Dataset for Data Analytics.csv")

# check null values across each column
print("Missing Values:\n",df.isnull().sum())

"""
handle missing values
blank CouponCode= No Coupon used
"""
df["CouponCode"]=df["CouponCode"].fillna("No Coupon")

# check duplicate values
df_duplicates=df.duplicated().sum()
print("Duplicates:",df_duplicates)

# remove duplicates
df=df.drop_duplicates()

# change datatype of Date
df["Date"]=pd.to_datetime(df["Date"])

# clean text columns
text_cols=["OrderID","CustomerID","Product","PaymentMethod","ShippingAddress","OrderStatus","TrackingNumber","CouponCode","ReferralSource"]
for col in text_cols:
    df[col]=df[col].str.strip()

# check TotalPrice by using Quantity and UnitPrice
wrong=(df["Quantity"] * df["UnitPrice"]).round(2) != df["TotalPrice"].round(2)
print("INCORRECT TotalPrice Rows:",wrong.sum())

# check clean dataset
print(df.head())
print("Final shape:",df.shape)
print("Missing Values After Cleaning:\n",df.isnull().sum())
print("Data types:\n",df.dtypes)

# SAVE CLEAN DATASET
df.to_csv(r"D:\python\Cleaned_Dataset1.csv",index=False)