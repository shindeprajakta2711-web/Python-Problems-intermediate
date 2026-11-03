numbers = [15, 22, 7, 40, 11, 18, 30, 5]
# new_num=[]
# for i in numbers:
#     if i>15:
#         new_num.append(i)
# print(new_num)

# Numbers which are divisible by 5 
# multi=[]
# for i in numbers:
#     if i%5==0:
#         multi.append(i)
# print(multi)

# Numbers which are divisible by 5 and then added up together
num_one=[]
add=0
for i in numbers:
    if i%5==0:
        num_one.append(i)
        add+=i
print(add)  