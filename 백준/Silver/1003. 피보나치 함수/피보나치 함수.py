import sys
input = sys.stdin.readline

T = int(input())
A = []
    
for i in range(T):
    A.clear()
    n = int(input())
    A = [0, 1]
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        for j in range(2, n+1):
            A.append(A[j-1]+ A[j-2])
        print(A[n-1], A[n])