import pandas as pd
import matplotlib.pyplot as plt

# Create a small dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [250, 300, 280, 350, 400, 420],
    'Profit': [50, 60, 55, 70, 80, 90],
    'Customers': [200, 240, 220, 300, 350, 380]
}

df = pd.DataFrame(data)

# 1️⃣ Line Plot - Sales over Months
plt.figure(figsize=(6,4))
plt.plot(df['Month'], df['Sales'], marker='o', label='Sales')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (in units)")
plt.legend()
plt.grid(True)
plt.show()

# 2️⃣ Bar Chart - Profit by Month
plt.figure(figsize=(6,4))
plt.bar(df['Month'], df['Profit'], color='orange')
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit (in $)")
plt.show()

# 3️⃣ Scatter Plot - Sales vs Customers
plt.figure(figsize=(6,4))
plt.scatter(df['Customers'], df['Sales'], color='green')
plt.title("Sales vs Customers")
plt.xlabel("Number of Customers")
plt.ylabel("Sales")
plt.show()

# 4️⃣ Histogram - Distribution of Profits
plt.figure(figsize=(6,4))
plt.hist(df['Profit'], bins=5, color='purple')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()
