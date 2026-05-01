#Step1 and #Step2
employee_details = {
    101:{
        'name':'Satya',
        'age':27,
        'department':'HR',
        'salary': 50000
    },

}

def add_employee_details(employee_details):
    emp_id = int(input("Enter employee ID: "))
    if emp_id in employee_details:
        print("Employee already exists")
    else:
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        department = input("Enter employee department: ")
        salary = input("Enter employee salary: ")
        employee_details[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
    }
    print("Employee added successfully")

def view_employees(employee_details):
    print("List of all employees: ",employee_details)

def search_employee(employee_details):
    emp_id = int(input("Enter employee ID: "))
    if emp_id in employee_details:
        print("Name: ", employee_details[emp_id]['name'])
        print("Age: ", employee_details[emp_id]['age'])
        print("Department: ", employee_details[emp_id]['department'])
        print("Salary: ", employee_details[emp_id]['salary'])
    else:
        print("Employee not found")

def main():

    while True:
        print("1. Add employee details")
        print("2. View all employees details")
        print("3. Search one employee details")
        print("4. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:

            add_employee_details(employee_details)

        elif choice == 2:
          view_employees(employee_details)

        elif choice == 3:
            search_employee(employee_details)

        elif choice == 4:
            print("Exit")
            break

        else:
            print("Invalid choice")

main()