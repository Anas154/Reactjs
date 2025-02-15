def get_employee_info():
    employee = {}
    
    employee['First Name'] = input("Enter First Name: ")
    employee['Last Name'] = input("Enter Last Name: ")
    employee['Age'] = input("Enter Age: ")
    employee['Gender'] = input("Enter Gender: ")
    employee['Phone Number'] = input("Enter Phone Number: ")
    employee['Department'] = input("Enter Department: ")
    employee['Salary'] = input("Enter Salary: ")
    employee['Date of Joining'] = input("Enter Date of Joining (YYYY-MM-DD): ")
    
    return employee

if __name__ == "__main__":
    print("Enter New Employee Details:")
    employee_info = get_employee_info()
    
    print("\nNew Employee Details:")
    for key, value in employee_info.items():
        print(f"{key}: {value}")

