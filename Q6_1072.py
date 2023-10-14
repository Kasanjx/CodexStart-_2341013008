"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1072
"""
n=int(input())

for i in range(1,n+1):
    b=(i*i*(i*i-1)//2)-4*(i-2)*(i-1)
    print(b)
