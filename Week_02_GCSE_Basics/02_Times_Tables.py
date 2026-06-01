def times_table(number):
    for i in range(1, 13):
        print(number, "x", i, "=", number * i)

num = int(input("Enter a number: "))
times_table(num)
