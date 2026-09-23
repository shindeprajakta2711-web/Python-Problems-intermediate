# Occurenence of number the most of the time 
numbers = [10, 5, 10, 20, 5, 10, 30, 20]
freq = {}
for i in numbers:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1

highest_num=0
most_frequent_num=0
for number, count in freq.items():
    if count>highest_num:
        highest_num=count
        most_frequent_num=number
print(most_frequent_num)