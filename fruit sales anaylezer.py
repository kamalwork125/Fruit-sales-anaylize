import pandas as pd
import numpy as np

# Step 1: Data banana manually (no CSV needed initially)
data = {
    'Fruit': ['Apple', 'Banana', 'Mango', 'Orange', 'Banana', 'Apple'],
    'Quantity': [10, 20, 15, 12, 18, 25],
    'Price': [30, 10, 25, 20, 10, 30]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Calculate Total Sale = Quantity × Price
df['Total'] = df['Quantity'] * df['Price']

print("\n📦 Fruit Sale Data:")
print(df)

# Step 4: Overall Stats
print("\n💰 Total Sales Amount:", df['Total'].sum())
print("📊 Average Sale per Item:", np.round(df['Total'].mean(), 2))

# Step 5: Most Sold Fruit (based on total quantity)
most_sold = df.groupby('Fruit')['Quantity'].sum().idxmax()
print("🏆 Most Sold Fruit:", most_sold)

# Step 6: Save to CSV
df.to_csv("fruit_sales.csv", index=False)
print("\n📁 Data saved to fruit_sales.csv")
