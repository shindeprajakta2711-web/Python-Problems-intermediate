numbers = [1, 2, 3, 2, 4, 1, 3, 2, 5, 4, 2]
freq = {}
for i in numbers:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1

highest_num=0
most_freq_num=0
for number, count in freq.items():
    if count>highest_num:
        highest_num=count
        most_freq_num=number
print("most occured number:", most_freq_num)
print("Freq of occurence:", highest_num)
# Occurence number