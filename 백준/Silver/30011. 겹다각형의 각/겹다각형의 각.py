import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sum = 0

if len(A) == 1:
    print(180*(A[0]-2))
else:
    for i in range(1, N):
        sum += 180*A[i]
    print(sum + 180*(A[0]-2))