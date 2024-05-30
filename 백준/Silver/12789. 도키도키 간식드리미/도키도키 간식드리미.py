import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = []

count = 1
while(True):
    if A and B:
        if A[0] == count:
            count += 1
            del A[0]
        elif B[-1] == count:
            count += 1
            del B[-1]
        else:
            B.append(A.pop(0))
    elif A:
        if A[0] == count:
            count += 1
            del A[0]
        else:
            B.append(A.pop(0))
    else:
        if B[-1] != count:
            print("Sad")
            break
        else:
            count += 1
            del B[-1]
    if count == N+1:
        print("Nice")
        break