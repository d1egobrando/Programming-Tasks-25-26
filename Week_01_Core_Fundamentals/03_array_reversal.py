import random

List = []

for i in range(5):
    List.append(random.randint(1,100))

print(List)

New_List = []

index = len(List) - 1

while index >= 0:
    New_List.append(List[index])
    index = index - 1

print(New_List)
