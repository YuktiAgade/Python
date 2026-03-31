//month,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,profit
//Jan,2500,1500,5200,9200,1200,1500,21100
//Feb,2600,1200,5100,9100,2100,1200,18300
//Mar,2800,1400,5300,9500,2300,1500,22400
//Apr,3000,1600,5500,9800,2500,1700,24000
//May,3200,1800,5700,10000,2700,1800,26000
//Jun,3500,2000,6000,10200,3000,2000,28000

//(a) Line Plot – Total Profit
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.plot(data['month'], data['profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

//(b) Multiline Plot – All Products
plt.plot(data['month'], data['facecream'], label='Face Cream')
plt.plot(data['month'], data['facewash'], label='Face Wash')
plt.plot(data['month'], data['toothpaste'], label='Toothpaste')

plt.title("Sales of Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

//(c) Bar Chart – Face Cream vs Face Wash
import numpy as np

x = np.arange(len(data['month']))

plt.bar(x-0.2, data['facecream'], width=0.4, label='Face Cream')
plt.bar(x+0.2, data['facewash'], width=0.4, label='Face Wash')

plt.xticks(x, data['month'])
plt.title("Face Cream vs Face Wash Sales")
plt.legend()
plt.show()

//(d) Pie Chart – Total Yearly Sales
products = ['Face Cream','Face Wash','Toothpaste','Bath Soap','Shampoo','Moisturizer']
sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Yearly Product Sales Distribution")
plt.show()
