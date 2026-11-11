numbers = [3, 8, 2, 10, 5, 7, 9, 1]
k = 3
win_sum=sum(numbers[:k])
max_sum=win_sum

for i in range(k,len(numbers)):
    win_sum+=numbers[i]
    win_sum-=numbers[i-k]
    max_sum=max(max_sum, win_sum)
print(max_sum)