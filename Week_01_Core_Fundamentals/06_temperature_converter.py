print("\nTemperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Exit")

choice = input("Choose an option (1-3): ")
if choice == "3":
    print("Bye")

if choice != "1" and choice != "2":
    print("Choose a valid option")
    choice = input("Choose an option (1-3): ")

if choice == "1":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = 9 * celsius / 5 + 32
    print("The temperature in Fahrenheit is:", fahrenheit)

if choice == "2":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = 9 * fahrenheit / 5 - 32
    print("The temperature in Celsius is:", fahrenheit)
