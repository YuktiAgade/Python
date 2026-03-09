# Employee Salary Program

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

DA = 0.92 * basic
HRA = 0.58 * basic
TA = 0.30 * basic
LIC = 500

gross_salary = basic + DA + HRA + TA
net_salary = gross_salary - LIC

print("\n----- Employee Details -----")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", dept)

print("\n----- Salary Details -----")
print("Basic Salary:", basic)
print("DA:", DA)
print("HRA:", HRA)
print("TA:", TA)
print("LIC Deduction:", LIC)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
