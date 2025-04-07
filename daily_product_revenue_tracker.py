import pandas as pd
from monthly_sales_summary import create_csv
import matplotlib.pyplot as plt


def read_csv():
    df = pd.read_csv("sales_summary.csv")

    print(df.head(5))
    print(df.describe())

    df["Total Sales"] = df["Unit Sold"]*df["Unit Price"]
    daily_total_revenue = df.groupby("Date")["Total Sales"].sum().round(2)
    for date, total_sale in daily_total_revenue.items():

        print(f"{date}: ${total_sale:,.2f}")
    product_wise_total_revenue = df.groupby("Product")["Total Sales"].sum().round(2)
    print(f"\nProduct-wise Total revenue")
    for product, total_sale_product in product_wise_total_revenue.items():

        print(f"{product}: ${total_sale_product:,.2f}")
    print(f"\nDay with highest total revenue")
    best_day = daily_total_revenue.idxmax()
    print(f"{best_day}: ${daily_total_revenue[best_day]:,.2f}")
    print(f"\nProduct with least revenue")
    worst_product = product_wise_total_revenue.idxmin()
    print(f"{worst_product}: {product_wise_total_revenue[worst_product]:,.2f}")
    return daily_total_revenue, product_wise_total_revenue


def visualise(daily_revenue, product_wise_revenue):
    plt.figure(figsize=(10,5))

    daily_revenue.plot(kind= "bar", color="skyblue")
    plt.title("Daily total revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig("daily_revenue_bar_chart.png")
    plt.show()

    plt.figure(figsize=(8,6))
    product_wise_revenue.plot(kind='pie', autopct= '%1.1f%%', startangle= 140)
    plt.title("Product-wise Revenue share")
    plt.ylabel(None)
    plt.tight_layout()
    plt.savefig("product_wise_revenue_pie_chart.png")
    plt.show()



create_csv()
daily_total_revenue, product_wise_total_revenue = read_csv()
visualise(daily_total_revenue, product_wise_total_revenue)