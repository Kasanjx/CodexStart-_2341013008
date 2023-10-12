"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1083
"""

n=int(input(""))
summa=n*(n+1)//2
lst=sum([int(i) for i in input().split()])
print(summa-lst)



