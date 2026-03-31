//Step 1: Read Excel File
//df = pd.read_excel("employee.xlsx")

//(a) Employees in Automotive domain
emp_id = int(input("Enter Employee ID: "))

emp = df[df['Employee ID'] == emp_id]
print(emp)


//(b) Details using Employee ID
emp_id = int(input("Enter Employee ID: "))

emp = df[df['Employee ID'] == emp_id]
print(emp)

//(c) List of Developers
developers = df[df['Designation'] == 'Developer']
print(developers)
