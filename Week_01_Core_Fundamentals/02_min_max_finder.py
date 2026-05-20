def find_min_max():
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    num3 = int(input("Enter a number:"))
    num4 = int(input("Enter a number:"))
    num5 = int(input("Enter a number:"))

    List = [num1,num2,num3,num4,num5]

    print(List)

    max_value=num5
    min_value=num1

    if num1 < min_value:
        min_value = num1

    if num2 < min_value:
        min_value = num2

    if num3 < min_value:
        min_value = num3

    if num4 < min_value:
        min_value = num4

    if num5 < min_value:
        min_value = num5

    print(min_value)

    if num1 > max_value:
        max_value = num1

    if num2 > max_value:
        max_value = num2

    if num3 > max_value:
        max_value = num3

    if num4 > max_value:
        max_value = num4

    if num5 > max_value:
        max_value = num5

    print(max_value)







find_min_max()
