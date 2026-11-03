# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__=='__main__':
    students=[]
    for _ in range(int(input("Enter the name"))):
        name=input()
        score=float(input())
        students.append([name,score])
    grades=[]
    
    for student in students:
        grades.append(student[1])
    
    unique_grades=sorted(set(grades))
    second_lowest=unique_grades[1]
    
    names=[]
    
    for student in students:
        if student[1]==second_lowest:
            names.append(student[0])
    names.sort()
    for name in names:
        print(name)