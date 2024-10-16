class SuperMarket:
    def __init__(self,code ,name , address, date):
        self.name = name
        self.code = code
        self.address = address
        self.date = date
        self.productsInS = {}

    def get_name(self):
        return self.name

    # setter method
    def set_name(self, name):
        self.name = name

    def get_code(self):
        return self.code

    # setter method
    def set_code(self, code):
        self.code = code

    def get_address(self):
        return self.address

    # setter method
    def set_address(self, address):
        self.address = address

    def get_date(self):
        return self.date

    # setter method
    def set_date(self, date):
        self.date = date
