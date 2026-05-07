import pandas as pd
import matplotlib.pyplot as plt 

sales = pd.read_csv('sales.csv')

sales['order_date'] = pd.to_datetime(sales['order_date'])

sales[ 'month'] = sales['order_date'].dt.month

Monthly_sales.plot(kind='bar')

plt.title('monthly sales analysis')
plt.xlabel('month')
plt.ylabel('sales amount')

plt.show()