names = ['Maruf','Temirlan', 'Seyto']
print(names)
names.append('Sultan')
print(names)
names.remove('Sultan')
print(names)

for i in range(5): # add new names in our list named names
    name = input('Write ')
    names.append(name)
print(names)
for i in names: #be in new line all names
    print(i)