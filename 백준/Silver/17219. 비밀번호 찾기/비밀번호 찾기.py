import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = {}

for i in range(N):
    x, y = map(str, input().rsplit())
    A[x] = y

for i in range(M):
    y = input().rstrip()
    print(A[y])