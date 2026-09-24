people = []

while True:
    print("\n1. Add name")
    print("2. Read Names")
    print("3. Delete Names")
    print("4. Exit")

    choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            age = input("Enter your age: ")

            people.append([name,age])

        elif choice == "2":
            for person in people:
                print("Name: ",person[0], ", Age: ",person[1])

        elif choice == "3":
            num = int(input("Enter the number of a name to deelete them "))
            people.pop(num)

        elif choice == "4":
            break
