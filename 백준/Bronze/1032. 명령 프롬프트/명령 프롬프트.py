import sys
input = sys.stdin.readline

n = int(input())

A = []
B = ""
for i in range(n):
    x = input()
    A.append(x)

for i in range(len(A[0])):
    count = 0
    temp = A[0][i]
    for j in A:
        if j[i] == temp:
            pass
        else:
            count += 1
    if count == 0:
        B += temp
    else:
        B += "?"

print(B, end = '')