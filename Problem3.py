#Task 1
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temps = temperatures[7:14]
print(second_week_temps)  

#Task 2
hot_days = [i for i in temperatures if i > 100]
print(hot_days)

#Task 3
temperatures_reversed = sorted(temperatures,reverse=True)   
print(temperatures_reversed)
five_to_ten = temperatures_reversed[4:10]
print(five_to_ten)

