import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('breadprice.csv')

# Calculate the average price for each year
data['Average Price'] = data[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)

# Extract relevant columns
average_price_per_year = data[['Year', 'Average Price']]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(average_price_per_year['Year'], average_price_per_year['Average Price'], marker='o', linestyle='-')
plt.title('Average Bread Price per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.show()
