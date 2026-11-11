numbers = [7, 12, 18, 24, 31, 36, 42]
target = 24

left=0
right=len(numbers)-1
while left<=right:
    mid=(left+right)//2
    if numbers[mid]==target:
        print("FOund at index :", mid)
        break
    elif numbers[mid]<target:
        left=mid-1
    else:
        right=mid-1
else:
    print("Not Found")
    #bro a issue has raised mid in my practice !!!!, while i was pushing and adjusting the files in the folders , i deleted one folder and later i got to know that it had my files ...but it was too late later and tried to make a new folder and a new file and then when i push it into the github . now the github is showing me only one file and that too the current one not the previous one , whereas i have my old files in my vs code but i had no idea why isn't showing me the previous files and folders . i tried to create new main branch too but the issue is same . should i create a new repo or not ...? suggest me solution >>>