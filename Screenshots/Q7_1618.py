"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1618
TRAILING ZEROS
"""

n=int(input())
i=0
while n>=5:
    i+=n//5
    n=n//5
print(i)
