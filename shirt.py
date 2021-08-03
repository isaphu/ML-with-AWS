class Shirt:
    def __init__(self, shirt_color, shirt_price, shirt_style, shirt_size):
        self.color = shirt_color
        self.price = shirt_price
        self.size = shirt_size
        self.style = shirt_style

    def change_price(self, new_price):
        self.price = new_price
    
    def discount(self, discount):
        return self.price * (1 - discount)
