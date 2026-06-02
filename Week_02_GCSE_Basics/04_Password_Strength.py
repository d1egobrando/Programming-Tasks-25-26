your_password = input("Enter a password: ")

score = 0

if len(your_password) >= 8:
    score = score + 1

for character in your_password:
    if character >= "0" and character <= "9":
        score = score + 1
        break

for character in your_password:
    if character >= "A" and character <= "Z":
        score = score + 1
        break

for character in your_password:
    if character >= "a" and character <= "z":
        score = score + 1
        break


if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")
