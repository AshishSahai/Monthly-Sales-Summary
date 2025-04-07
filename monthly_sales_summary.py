import random
import pandas as pd


def create_csv():
    dates = pd.date_range(start="2025-04-01", periods=30, freq="D")
    products = ["Laptop", "Smartphone", "Tablet", "Smartwatch"]

    sales_summary = []


    for date in dates:
        for _ in range(random.randint(3,6)):
            product = random.choice(products)
            unit_sold = random.randint(40,100)
            unit_price = random.randint(100,1000)

            sales_summary.append([date.strftime("%Y-%m-%d"), product, unit_sold, unit_price])


    df = pd.DataFrame(sales_summary, columns=["Date", "Product", "Unit Sold", "Unit Price"])


    df.to_csv("sales_summary.csv" , index= False)
    print("Sales summary is created and saved!")



def read_data():
    df =  pd.read_csv("sales_summary.csv")
    print(df.head(5))
    #print(df.describe())
    df["Total Sales"] = df["Unit Sold"]*df["Unit Price"]
    total_units = df.groupby("Product")["Unit Sold"].sum()
    print("\nTotal Units sold per Products")
    print(total_units)
    avg_price = df.groupby("Product")["Unit Price"].mean().round(2)
    print("\nAverage unit price per product")
    print(avg_price)
    total_revenue = df.groupby("Product")["Total Sales"].sum().round(2)
    print("\nTotal revenue per product")
    print(total_revenue)

    best_seller = total_units.idxmax()
    top_revenue_product = total_revenue.idxmax()
    print(f"\n Best selling product by units: {best_seller}")
    print(f"\nTop revenue product: {top_revenue_product}")


create_csv()
read_data()

