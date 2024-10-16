class Products:

    def __init__(self, code, name, ex_date, wholesaleCost, saleCost, quantity):
        self.code = code
        self.name = name
        self.ex_date = ex_date
        self.wholesaleCost = wholesaleCost
        self.saleCost = saleCost
        self.quantity = quantity

    def get_code(self):
        return self.code

    # setter method
    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    # setter method
    def set_name(self, name):
        self.name = name

    def get_ex_date(self):
        return self.ex_date

    # setter method
    def set_ex_date(self, ex_date):
        self.ex_date = ex_date

    def get_wholesaleCost(self):
        return self.wholesaleCost

    # setter method
    def set_wholesaleCost(self, wholesaleCost):
        self.wholesaleCost = wholesaleCost

    def get_saleCost(self):
        return self.saleCost

    # setter method
    def set_saleCost(self, saleCost):
        self.saleCost = saleCost

    def get_quantity(self):
        return self.quantity

    # setter method
    def set_quantity(self, quantity):
        self.quantity = quantity
