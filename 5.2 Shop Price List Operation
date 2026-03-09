# Lab Assignment-2: Shop Price List Operations

# Store prices of sold items in a tuple
print("Enter prices of sold items (press Enter without input to stop):")
prices = []

while True:
    user_input = input("Enter price (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        price = float(user_input)
        if price >= 0:
            prices.append(price)
        else:
            print("Price cannot be negative. Please enter a valid price.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Convert to tuple
price_tuple = tuple(prices)

print("\n" + "="*50)
print("SHOP SALES ANALYSIS")
print("="*50)

if len(price_tuple) > 0:
    # a) Print the total number of items sold
    print(f"a) Total number of items sold: {len(price_tuple)}")
    
    # b) Print the price of cheapest item sold
    cheapest = min(price_tuple)
    print(f"b) Price of cheapest item: ₹{cheapest:.2f}")
    
    # c) Print the price of costliest item sold
    costliest = max(price_tuple)
    print(f"c) Price of costliest item: ₹{costliest:.2f}")
    
    # d) Print the price list in ascending order
    sorted_prices = tuple(sorted(price_tuple))
    print("d) Price list in ascending order:")
    for i, price in enumerate(sorted_prices, 1):
        print(f"   {i}. ₹{price:.2f}")
    
    # e) Print the number of costliest items sold on the day
    costliest_count = price_tuple.count(costliest)
    print(f"e) Number of costliest items (₹{costliest:.2f}) sold: {costliest_count}")
    
    # Additional analysis
    print("\n" + "="*50)
    print("ADDITIONAL ANALYSIS")
    print("="*50)
    
    # Average price
    average_price = sum(price_tuple) / len(price_tuple)
    print(f"Average price: ₹{average_price:.2f}")
    
    # Total sales
    total_sales = sum(price_tuple)
    print(f"Total sales: ₹{total_sales:.2f}")
    
    # Price range
    price_range = costliest - cheapest
    print(f"Price range: ₹{price_range:.2f}")
    
    # Items above average
    above_avg = [p for p in price_tuple if p > average_price]
    print(f"Items above average price: {len(above_avg)}")
    
    # Items below average
    below_avg = [p for p in price_tuple if p < average_price]
    print(f"Items below average price: {len(below_avg)}")
    
else:
    print("No items were entered.")

# Display original price list
print("\n" + "="*50)
print("Original Price List:")
print(price_tuple)
