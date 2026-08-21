# Occurenence of number the most of the time 
numbers = {10, 5, 10, 20, 5, 10, 30, 20}
highest_num = 0
most_freq_number = 0
for number , count in numbers.items():
    if count>highest_num:
        highest_num=count
        most_freq_number=numbers
print(most_freq_number)