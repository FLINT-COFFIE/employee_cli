# Employee class


class Employee:
    # class variables
    number_of_emps = 0
    tax_percentage = 0.055

    # initialize the class
    def __init__(self, first: str, last: str, pay: int):
        if pay < 0:
            raise ValueError("Pay cannot be negative")
        self.first = first
        self.last = last
        self.pay = pay
        Employee.number_of_emps += 1

    # compute email
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    # compute fullname
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # assign tax_percent
    @classmethod
    def tax_percent(cls, percentage):
        cls.tax_percentage = percentage

    # compute net income
    def net_income(self):
        return self.pay * (1 - Employee.tax_percentage)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"


if __name__ == "__main__":
    f = Employee("flint", "coffie", 4000)
    print(f.email)
    print(f.number_of_emps)
    print(f.fullname)
    print(f.net_income())
    print(f)
