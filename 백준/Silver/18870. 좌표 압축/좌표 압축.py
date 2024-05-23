import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = sorted(list(set(A)))
C = {}

for i in range(len(B)):
    C[B[i]] = i

for i in A:
    print(C[i], end = ' ')