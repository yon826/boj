import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
if N%2 == 1:
    if A.count(0) >= N/2:
        print("INVALID")
    elif A.count(1) > A.count(-1):
        print("APPROVED")
    else:
        print("REJECTED")
else:
    if A.count(0) >= N//2:
        print("INVALID")
    elif A.count(1) > A.count(-1):
        print("APPROVED")
    else:
        print("REJECTED")