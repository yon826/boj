import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A = [1, 1, 1, 2, 2]
    N = int(input())
    if N <= 5:
        print(A[N-1])
    else:
        for j in range(6, N+1):
            A.append(A[-1] + A[j-6])
        print(A[-1])