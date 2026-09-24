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
