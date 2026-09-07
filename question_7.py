# Numbers segrating into positive numbers and their addition
numbers = [12, -5, 18, -7, 25, -30, 11, 40]
positive=[]
sum=0
for i in numbers:
    if i>0:
        positive.append(i)
        sum+=i
print(sum)