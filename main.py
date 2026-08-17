# import employee class
from employee import Employee

# store employees
employees = {}


# functions
def add_employee():
    # take inputs
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    pay = int(input("Enter pay amount: "))

    # make index
    staff = Employee(first, last, pay)
    employees[staff.fullname] = staff
    print("added employees")
    print(employees)


# option 2
def erase_employee():
    fullname = input("Enter Fullname: ")
    removed = employees.pop(fullname, None)
    print(f"Erased {removed.fullname} from staff records")


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

        try:
            user_input = int(user_input)

        except ValueError:
            print("ValueError Incorrect Input")
            continue

        if not user_input in range(1, 5):
            continue

        elif user_input == 1:
            add_employee()

        elif user_input == 2:
            erase_employee()


if __name__ == "__main__":
    main()
    # print(employees)
