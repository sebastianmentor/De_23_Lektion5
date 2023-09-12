lista = [i for i in range(1,11)]

print(lista)
print(id(lista))

# lista = sorted(lista, reverse=True)
new_list = sorted(lista, reverse=True)
lista.reverse()

print(id(lista))
print(lista)
print(id(new_list))
print(new_list)