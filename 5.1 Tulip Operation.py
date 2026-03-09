# Lab Assignment-1: Tuple Operations

# Get input from user
print("Enter a series of integers (press Enter without input to stop):")
numbers = []

while True:
    user_input = input("Enter an integer (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Convert to tuple
num_tuple = tuple(numbers)

print("\n" + "="*50)
print("Tuple Operations")
print("="*50)

# a) Print the total number of items in the Tuple
print(f"a) Total number of items: {len(num_tuple)}")

# b) Print the last item in the Tuple
if len(num_tuple) > 0:
    print(f"b) Last item: {num_tuple[-1]}")
else:
    print("b) Tuple is empty")

# c) Print the Tuple elements in reverse order
print("c) Tuple in reverse order:", num_tuple[::-1])

# d) Print Yes if the Tuple contains an integer 5 and No otherwise
print("d) Contains 5:", "Yes" if 5 in num_tuple else "No")

# e) Remove first and last items, sort remaining, and print
if len(num_tuple) >= 2:
    # Remove first and last items
    remaining = num_tuple[1:-1]
    # Sort the remaining items
    sorted_remaining = tuple(sorted(remaining))
    print(f"e) After removing first and last, sorted result: {sorted_remaining}")
else:
    print("e) Not enough elements to remove first and last items")

# Additional demonstration
print("\n" + "="*50)
print("Tuple Information:")
print(f"Original tuple: {num_tuple}")
print(f"Type: {type(num_tuple)}")
print(f"First element: {num_tuple[0] if num_tuple else 'N/A'}")
print(f"Last element: {num_tuple[-1] if num_tuple else 'N/A'}")
