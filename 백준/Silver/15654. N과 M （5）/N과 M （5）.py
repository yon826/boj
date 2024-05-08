import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
L1 = [0]

def Rec(m):
    if 1<=m:
        for i in A:
            if i not in L1:
                L1.append(i)
                Rec(m-1)
                L1.pop()
    else:
        print(*L1[1:])

Rec(M)