temperatures = []

highesttemp = max(temperatures)
lowesttemp = min(temperatures)
averagetemp = sum(temperatures) / len(temperatures)

print("The Highest temperature is:", highesttemp)
print("The Lowest temperature is:", lowesttemp)
print("The Average temperature is:", averagetemp)

file = open("meantemp_daily_totals.txt", "r") #read
