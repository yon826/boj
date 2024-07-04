import sys
import math as m
input = sys.stdin.readline

x = input()
n = int(input())

sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += a
print(x[sum:sum + b])
