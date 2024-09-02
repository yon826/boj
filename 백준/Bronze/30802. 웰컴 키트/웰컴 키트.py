import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
t, p = map(int, input().split())
for i in range(6):
    if A[i] % t == 0:
        A[i] = A[i]//t
    else:
        A[i] = A[i]//t + 1
print(sum(A))
print(N//p, N%p)