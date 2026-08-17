# import employee class
from employee import Employee

# store employees
employees = {}


# functions
def add_employee():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    pay = input("Enter pay amount: ")
    index = first
    first = Employee(first, last, pay)
    employees[index] = first
    return employees


def main():
    # Visuals
    print("==========================")
    print("===  Employee Manager  ===")
    print("==========================")

    # Inputs
    print("1. Add Employee\n")
    print("2. Erase Employee\n")
    print("3. Employee details\n")
    print("4. Total number of Employees\n")

    # adding employees
    while True:
        user_input = input("Enter your input: ")
        if not user_input in range(1:5):
            raise ValueError ("Incorrect Input")
    
        if user_input == 1:
            add_employee()


if __name__ == "__main__":
    main()
    # print(employees)
