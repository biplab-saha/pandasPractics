import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Avoid using Tkinter
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('sales_data.csv')
print(df)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by month and count unique customers
monthly_customers = df.groupby(df['Date'].dt.to_period('M'))['Customer Name'].nunique()

# Plot and save to a file instead of showing
monthly_customers.plot(kind='line', marker='o')
plt.title("Unique Customers per Month")
plt.ylabel("Number of Customers")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('monthly_customers_plot.png')  # Save the plot instead of showing
print("Plot saved as monthly_customers_plot.png")
