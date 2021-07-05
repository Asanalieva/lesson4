products = ['Fruits', 'Socks', 'Milk', 'Brain', 'Vegetables', 'Python 3']
print(products)
print(products[3])
print(products[4])
print(products[1])
print(products[5])
print(products[0:5])
print(products[1:])
print(products[:5]) #последний index не влючаетс
products[0] = 'Kefir'
print(products[0])
products[1] = 'Suharik'
print(products)
tuple = ('Bread', 'Milk', 'Vegetable')
print(tuple[0])
print(tuple[0:3])
for i in products:
    print(i)