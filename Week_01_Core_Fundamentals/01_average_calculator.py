def calculate_average():
    num1 = int(input("Input a number:"))
    num2 = int(input("Input a number:"))
    num3 = int(input("Input a number:"))
    num4 = int(input("Input a number:"))
    num5 = int(input("Input a number:"))

    List = [num1,num2,num3,num4,num5]
    print(List)
    sum = num1 + num2 + num3 + num4 + num5
    print(sum)
    average = sum / len(List)
    print(average)
    if average > 30:
        print("Valid Mean")
    else:
        print("Invalid Mean")

calculate_average()
