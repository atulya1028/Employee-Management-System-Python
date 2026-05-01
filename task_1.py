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
    try:
        emp_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Employee ID must be a number")
        return

    if emp_id in employee_details:
        print("Employee already exists")
        return

    name = input("Enter employee name: ")

    try:
        age = int(input("Enter employee age: "))
    except ValueError:
        print("Employee age must be a number")
        return

    department = input("Enter employee department: ")

    try:
        salary = int(input("Enter employee salary: "))
    except ValueError:
        print("Employee salary must be a number")
        return

    employee_details[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print("Employee added successfully")

def view_employees(employee_details):
    if not employee_details:
        print("Employee not found")
        return

    print("\n{:>10} {:>15} {:>10} {:>15} {:>10}".format(
        "ID",
        "Name",
        "Age",
        "Department",
        "Salary"
    ))
    print("-" * 65)

    for emp_id, emp in employee_details.items():
        print("\n{:>10} {:>15} {:>10} {:>15} {:>10}".format(
            emp_id,
            emp['name'],
            emp['age'],
            emp['department'],
            emp['salary']
        ))
def search_employee(employee_details):

    try:
        emp_id = int(input("Enter employee ID: "))
    except ValueError:
        print("Invalid ID")
        return

    print("\n{:>10} {:>15} {:>10} {:>15} {:>10}".format(
        "ID",
        "Name",
        "Age",
        "Department",
        "Salary"
    ))
    print("-" * 65)

    if emp_id in employee_details:
        emp = employee_details[emp_id]

        print("\n{:>10} {:>15} {:>10} {:>15} {:>10}".format(
            'ID',
            'Name',
            'Age',
            'Department',
            'Salary'
        ))
        print("-" * 65)

        print("{:>10} {:>15} {:>10} {:>15} {:>10}".format(
            emp_id,
            emp['name'],
            emp['age'],
            emp['department'],
            emp['salary']
        ))


def main():

    while True:
        print("1. Add employee details")
        print("2. View all employees details")
        print("3. Search one employee details")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice")
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