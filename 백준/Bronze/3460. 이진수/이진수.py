import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A = []
    n = int(input())
    while n > 0:
        A.append(n%2)
        n = n//2
    for i in range(len(A)):
        if A[i] == 1:
            print(i, end = ' ')