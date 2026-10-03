basket = [1, 2, 3, 4]

new_list = print(basket.append(100))

# append changes the list in place, does not create a new list
print("basket -->", basket)
# new_list will not be printed
print("new_list -->" , new_list)

#to create a new_list, you must reassign the original list
new_list = basket

print("new_list -->",new_list)

