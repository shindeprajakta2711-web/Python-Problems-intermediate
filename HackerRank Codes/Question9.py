#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.
def count_substring(string, sub_string):
    count =0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]:
            count+=1
    return count

if __name__=='__main__':
    string=input().strip()
    sub_string=input().strip()
    count=count_substring(string, sub_string)
    
    print(count)
    
if __name__ == '__main__':
    s = input()
    
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))