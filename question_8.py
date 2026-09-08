# Frequency of the letter in the word
word = "Lenovo"
freq = {}
for char in word:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)