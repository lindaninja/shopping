list = []
print("This is a shopping list!")
add_item = raw_input("Do you want to add an item to your shopping list? (if, please type just: Yes or No) ")

while add_item == "Yes" or add_item == "yes" or add_item == "y" or add_item == "Y":
    list.append(raw_input("Please enter name of item. "))

    add_item = raw_input("Do you want to add another item? (Yes/No)")
    add_another_item = raw_input
    if add_another_item == "No" or add_another_item == "no" or add_another_item == "N" or add_another_item == "n":
        break
        print ("This is your shopping list:")
    print ("You didn't add any item - you need to type the name of the item you want.")
else:
    print("This are your ordered items:")
    print list

