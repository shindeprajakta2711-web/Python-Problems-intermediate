# First repeated number
numbers = [4, 7, 2, 9, 7, 5, 2]
seen=set()
for num in numbers:
    if num in seen:
        print("First repeated number is :", num)
        break
    else:
        seen.add(num)