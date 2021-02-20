# For importing pandas
import pandas as pd

# For importing the grocery data
sales_data = pd.read_csv("grocery_sales.csv")

# For filling the missing values in the sales column
avg_sales = sales_data["sales"].mean()
sales_data["sales"].fillna(value= avg_sales, inplace = True)

# Sum sales by day summary generation
sales_summary = sales_data.groupby("transaction_date")["sales"].sum()

# plotting sales data ovetime
sales_summary.plot(rot = 45)