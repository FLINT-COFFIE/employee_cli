# Employee class


class Employee:
    # class variables
    tax_percentage = 0.055

    # initialize the class
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"


if __name__ == "__main__":
    f = Employee("flint", "coffie", 4000)
    print(f.email)
