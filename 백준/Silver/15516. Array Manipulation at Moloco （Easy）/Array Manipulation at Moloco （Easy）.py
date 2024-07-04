import sys
import math as m
input = sys.stdin.readline

n = int(input())

A = []
for i in range(n):
    x = int(input())
    A.append(x)

count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if i > j:
            if A[i] >= A[j]:
                count += 1
    print(count)