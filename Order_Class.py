class Order():
    
    def __init__(self,order_number,product_number,product_des,aisle,shelf,bins):
        self.aisle = aisle
        self.shelf = shelf
        self.bin = bins
        self.product_number = product_number
        self.product_description = product_des
        self.order_number = order_number
        self.head = None

    def __str__(self):
        return str("Aisle: " + self.aisle + "\n"
                "Shelf: " + self.shelf + "\n"
                "Bin: " + self.bin + "\n"
                "Product Number: " + self.product_number + "\n"
                "Product Description: " + self.product_description + "\n"
                "Order Number: " + self.order_number + "\n")
