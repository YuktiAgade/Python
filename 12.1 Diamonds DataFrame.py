import pandas as pd

data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'color': ['E', 'E', 'E', 'I', 'J'],
    'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'],
    'depth': [61.5, 59.8, 56.9, 62.4, 63.3],
    'table': [55.0, 61.0, 65.0, 58.0, 58.0],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(data)
print(df)

//(i) Mean price for each cut
mean_price = df.groupby('cut')['price'].mean()
print("Mean price for each cut:\n", mean_price)

//ii) Count, Minimum, Maximum price for each cut
stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print("\nCount, Min, Max price:\n", stats)

//(iii) Average of x, y, z
avg_values = df[['x', 'y', 'z']].mean()
print("\nAverage of x, y, z:\n", avg_values)
          
