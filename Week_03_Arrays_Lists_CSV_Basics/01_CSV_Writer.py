name = str(input("What is your name?:"))
age = int(input("How old are you?:"))
favcolour = str(input("What is your favourite colour?:"))
favfruit = str(input("What is your favourite fruit?:"))
favsubject = str(input("What is your favourite subject?:"))

file = open("csvwrite.csv", "a")
file.write("name,age,favcolour,favfruit,favsubject\n")
file.close()
