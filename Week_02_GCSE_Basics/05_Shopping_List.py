your_shopping_list = []

item = ""

while item != "finish":
    item = input("Enter an item (or finish to END): ")

    if item != "finish":
        your_shopping_list.append(item)

print("\nShopping List:")

for i in range(len(your_shopping_list)):
    print(i + 1, "-", your_shopping_list[i])

edit = input("\nDo you want to edit an item? (y/n): ")

if edit == "y":
    item_number = int(input("Enter the item you want  to edit: "))

    new_item = input("Enter the new item: ")

    your_shopping_list[item_number - 1] = new_item

    print("\nUpdated Shopping List:")

    for i in range(len(your_shopping_list)):
        print(i + 1, "-", your_shopping_list[i])
