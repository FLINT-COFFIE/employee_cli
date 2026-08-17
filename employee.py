# Employee class


class Employee:
    # class variables
    tax_percentage = 0.055

    # initialize the class
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
