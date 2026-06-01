your_sentence = input("Enter your sentence: ")

words = []
word = ""

for character in your_sentence:
    if character != " ":
        word = word + character
    else:
        words.append(word)
        word = ""

words.append(word)

print("Words:", words)
