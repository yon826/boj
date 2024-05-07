import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = {}
B = {}

for i in range(N):
    x = input().rstrip()
    A[x] = i+1
    B[i+1] = x

for i in range(M):
    y = input().rstrip()
    if y.isnumeric():
        print(B[int(y)])
    else:
        print(A[y])