import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
if N == 1:
    if A[0] == 1:
        print("APPROVED")
    elif A[0] == -1:
        print("REJECTED")
    else:
        print("INVALID")
else:
    if A.count(0) >= N//2:
        print("INVALID")
    elif A.count(1) > A.count(-1):
        print("APPROVED")
    else:
        print("REJECTED")