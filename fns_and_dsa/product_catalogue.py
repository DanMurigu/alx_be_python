class   Product:
    def __init__(self, name="", price=0, quantity=0):
        self.name = name 
        self.price = price
        self.quantity = quantity

    def get_details(self):
        self.name = input("Name of the Item: ")
        self.price = int(input("Enter the price of the item: "))
        self.quantity = int(input("How many are in stock: "))

    def display_product(self):
        print(f"Name: {self.name},Price:  {self.price}, Quantity: {self.quantity}")
    
    def total_value(self):
        return self.price * self.quantity
    
products = []

while True:

    print("\nEnter item details:")
    p = Product()
    p.get_details()
    products.append(p)

    cont = input("Do you want to add another product? (yes/no): ").lower()
    if cont != 'yes':
        break
    
print("\n--- Product Catalogue ---")
total_inventory_value = 0

for product in products:
    product.display_product()
    total_inventory_value += product.total_value()

print(f"\nTotal value of all products in stock:{total_inventory_value} ")



