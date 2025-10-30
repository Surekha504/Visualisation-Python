import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
    'Destination': ['Delhi', 'Jaipur', 'Agra', 'Goa', 'Mumbai'],
    'Food': [1200, 900, 1100, 1500, 1300],
    'Transport': [800, 1200, 1000, 1500, 1600],
    'Hotel': [3000, 2500, 2800, 3500, 4000],
    'Sightseeing': [500, 700, 800, 1000, 900],
}

df = pd.DataFrame(data)
df['Total'] = df[['Food', 'Transport', 'Hotel', 'Sightseeing']].sum(axis=1)

plt.figure(figsize=(7,4))
plt.plot(df['Day'], df['Total'], marker='o', color='teal')
plt.title("Day-wise Total Travel Expenses")
plt.xlabel("Day")
plt.ylabel("Total Expense (₹)")
plt.grid(True)
plt.show()


category_totals = df[['Food', 'Transport', 'Hotel', 'Sightseeing']].sum()
plt.figure(figsize=(7,4))
category_totals.plot(kind='bar', color=['orange', 'green', 'skyblue', 'violet'])
plt.title("Total Expense by Category")
plt.xlabel("Category")
plt.ylabel("Total Amount (₹)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(6,6))
plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title("Overall Expense Distribution")
plt.show()

plt.figure(figsize=(8,5))
plt.stackplot(df['Day'], df['Food'], df['Transport'], df['Hotel'], df['Sightseeing'],
              labels=['Food', 'Transport', 'Hotel', 'Sightseeing'], alpha=0.8)
plt.title("Expense Pattern Over Trip Days")
plt.xlabel("Day")
plt.ylabel("Amount (₹)")
plt.legend()
plt.show()


