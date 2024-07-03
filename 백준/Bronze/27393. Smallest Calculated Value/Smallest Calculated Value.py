import sys
import math as m
input = sys.stdin.readline

a, b, c = map(int, input().split())

A = []
B = [a + b,  a - b, a * b]
if a%b == 0:
    B.append(a//b)
def cal(a, b):
    A.append(a+b)
    A.append(a-b)
    A.append(a*b)
    if a%b == 0:
        A.append(a//b)

for j in B:
    cal(j, c)
A.sort()

for i in A:
    if i >= 0:
        print(int(i))
        break