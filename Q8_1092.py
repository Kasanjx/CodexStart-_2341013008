"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1092
"""

n=int(input())
suma=(n*(n+1))//2
a=set()
b=set()
if suma%2==0:
    print("YES")
    q=suma//2
    for i in range(n,0,-1):
        if i<=q:
            a.add(i)
            q-=i
        else:
            b.add(i)
    print(len(b))
    print(*b)
    print(len(a))
    print(*a)
else:
    print("NO")

