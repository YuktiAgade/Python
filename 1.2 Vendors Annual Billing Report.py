# Vendor Billing Program

name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

total_purchase = 0

print("\nEnter Monthly Purchases:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    total_purchase += amount

print("\n----- Vendor Details -----")
print("Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)

print("\nTotal Annual Purchase:", total_purchase)
