class Pants:
    def __init__(self,pants_color, pants_waist_size, pants_length, pants_price):
        self.color = pants_color
        self.waist_size = pants_waist_size
        self.length = pants_length
        self.price = pants_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, percentage):
        return self.price * (1 - percentage)
        