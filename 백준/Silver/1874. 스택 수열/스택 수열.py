import sys
input = sys.stdin.readline

A = []
B = []
count = 1

n = int(input())
for i in range(n):
    if count > 0:
        x = int(input())
        while(1):
            if x >= count:
                A.append(count)
                B.append("+")
                count += 1
            else:
                if A[-1] == x:
                    B.append("-")
                    A.pop()
                    break
                else:
                    print("NO")
                    count = -1
                    break
if count == -1:
    pass
else:
    for i in B:
        print(i)