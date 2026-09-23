ages = [25, 31, -5, 42, 150, 28, 0, 35]
valid = []
invalid = []
for age in ages:
    if age>=1 and age<=100:
        valid.append(age)
    else:
        invalid.append(age)
print("Valid ages: ", valid)
print("Invalid ages: ", invalid)