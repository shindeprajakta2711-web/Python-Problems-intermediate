logs = [
    "ERROR",
    "INFO",
    "ERROR",
    "WARNING",
    "INFO",
    "ERROR",
    "INFO",
    "WARNING",
    "ERROR"
]
count={}
for log in logs:
    if log in count:
        count[log]+=1
    else:
        count[log]=1
print(count)