class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Product Name: {self.name}, Price: EUR{self.price:.2f}, Quantity: {self.quantity}"

    def buy(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            return f"Successfully bought {amount} {self.name}(s)."
        else:
            return "Invalid purchase amount or insufficient quantity."

    def is_active(self):
        return self.quantity > 0

    def show(self):
        print(self.display_info())

    def set_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Invalid quantity. Please enter a non-negative value.")

