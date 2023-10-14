"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1094
"""
#Increasing array
n=int(input())
lst=[int(x) for x in input().split(' ')]
c=0
incre=0
for i in range(1, n):
    if lst[i]<lst[i-1]:
        incre=lst[i-1]-lst[i]
        lst[i]=lst[i]+incre
        c=c+incre
print(c)
