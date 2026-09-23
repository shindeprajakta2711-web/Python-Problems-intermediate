# # First repeated number
# numbers = [4, 7, 2, 9, 7, 5, 2]
# seen=set()
# for num in numbers:
#     if num in seen:
#         print("First repeated number is :", num)
#         break
#     else:
#         seen.add(num)


# First repeated words:
words = ["apple", "banana", "orange", "apple", "mango", "banana"]
new = set()
for word in words:
    if word in new:
        print("First repeated word is :", word)
        break
    else:
        new.add(word)

