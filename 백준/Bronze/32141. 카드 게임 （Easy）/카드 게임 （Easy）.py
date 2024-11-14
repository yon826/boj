import sys
input = sys.stdin.readline

n, h = map(int, input().split())
A = list(map(int, input().split()))
total = 0

if sum(A) < h:
    print(-1)
else:
    for i in range(n):
        total += A[i]
        if total >= h:
            print(i+1)
            break