file = open("meantemp_daily_totals.txt", "r") #read

temperatures = []

highest_temp = max(temperatures)
lowest_temp = min(temperatures)
average_temp = sum(temperatures) / len(temperatures)

print("The Highest temperature is:", highest_temp)
print("The Lowest temperature is:", lowest_temp)
print("The Average temperature is:", average_temp)
