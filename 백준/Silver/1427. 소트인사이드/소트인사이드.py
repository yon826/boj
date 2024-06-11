import sys
input = sys.stdin.readline

N = input()

A = []
for i in range(len(N)):
    A.append(N[i])

A.sort()
A.reverse()

for i in A:
    print(i, end = '')