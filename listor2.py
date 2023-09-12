name = input('Skriv in ditt namn: ').title().split()

# name = name.title()
# name = name.split()

# print(list(name))
temp = []
for i in name:
    temp.extend(list(i))

name = temp
print(list(name))