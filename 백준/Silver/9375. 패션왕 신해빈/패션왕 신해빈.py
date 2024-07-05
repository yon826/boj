import sys
import math as m
input = sys.stdin.readline

T = int(input())

A = {}
for _ in range(T):
    A.clear()
    N = int(input())
    for _ in range(N):
        a, b = map(str, input().split())
        if b not in A:
            A[b] = 1
        else:
            A[b] += 1
    sum = 1
    for i in A:
        sum *= A[i]+1

    print(sum-1)