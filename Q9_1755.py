"""
NAME: ANJANA MAHANTA
REG NO: 2341013008
PS LINK: https://cses.fi/problemset/task/1755
"""

n=input()
first,end=[],[]
for i in n:
    if i in first:
        first.remove(i)
        end.append(i)
    else:
        first.append(i)
pali = ''.join(end) + ''.join(first) + ''.join(end)[::-1]
if pali==pali[::-1]:
    print(pali)
else:
    print("NO SOLUTION")
