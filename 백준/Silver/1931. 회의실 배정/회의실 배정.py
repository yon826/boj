import sys
import math as m
input = sys.stdin.readline

n = int(input())

A = []
for i in range(n):
    a, b = map(int, input().split())
    A.append([b, a])

A.sort()
temp, tempx, tempy = 0, A[0][1], A[0][0]
count = 1
for j in range(n):
    if temp < j:
        if A[j][1] >= tempy:
            count += 1
            tempx = A[j][1]
            tempy = A[j][0]
            temp = j
print(count)