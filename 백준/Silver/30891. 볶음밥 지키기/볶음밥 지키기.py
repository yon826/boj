import sys
import math as m
input = sys.stdin.readline

n, r = map(int, input().split())
A = []

for i in range(n):
    x, y = map(int, input().split())
    A.append([x, y])

xx, yy = 0, 0
count = 0
temp = 0
for i in range(-100, 101):
    for j in range(-100, 101):
        temp = 0
        for k in range(n):
            if (A[k][0]-i)**2 + (A[k][1]-j)**2 <= r*r:
                temp += 1
            if temp > count:
                count = temp
                xx, yy = i, j
print(xx, yy)