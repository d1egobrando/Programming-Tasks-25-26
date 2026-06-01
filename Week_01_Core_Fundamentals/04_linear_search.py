numbers = [1, 3, 5, 7, 9,11,13]

target_number = int(input("Enter a number: "))

for number in numbers:
    if number == target_number:
        print("Target Found:", target_number)
        break
else:
    print("Target Not Found")
