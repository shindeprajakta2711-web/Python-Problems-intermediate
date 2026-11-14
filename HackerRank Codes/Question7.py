#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def split_hypen_case(line):
    words=line.split(" ")
    result="-".join(words)
    return result
if __name__=='__main__':
    line=input()
    result=split_hypen_case(line)
    print(result)