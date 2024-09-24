import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
X = [0] * N
for i in range(N):
    if (i+1)%10 == 1 or (i+1)%10 == 4 or (i+1)%10 == 7:
        X[i] = 1
for _ in range(Q):
    i = int(input())
    if X[i-1] == 0:
        X[i-1] = 1
    else:
        X[i-1] = 0
    print(X.count(1))