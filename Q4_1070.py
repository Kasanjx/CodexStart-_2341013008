"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1070
"""

n=int(input(""))
if n==1:
    print(n)
elif n<=3:
    print("NO SOLUTION")
else:
    lst_even=[i for i in range(2,n+1,2)]
    lst_odd=[i for i in range(1,n+1,2)]
    a=lst_even+lst_odd
    for i in a:
        print(i,end=" ")


