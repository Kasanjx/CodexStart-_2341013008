"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1069
"""
n=input("")
count,max=0,0
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count=count+1
        if count>=max:
            max=count
    elif n[i]!=n[i+1]:
            count=0
print(max+1)

