from shirt import Shirt

shirt_first_branch = Shirt('red',20, 'long sleeve', 'XL')
shirt_second_branch = Shirt('black', 40, 'short sleeve', 'L')

print(shirt_first_branch.price)
print(shirt_second_branch.color)

shirt_second_branch.change_price(15)
print(shirt_second_branch.price)