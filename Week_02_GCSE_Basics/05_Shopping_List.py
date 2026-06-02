your_shopping_list = []

item = ""

while item != "finish":
    item = input("Enter an item (or finish to END): ")

    if item != "finish":
        your_shopping_list.append(item)

print("\nShopping List:")

for i in range(len(your_shopping_list)):
    print(i + 1, "-", your_shopping_list[i])
