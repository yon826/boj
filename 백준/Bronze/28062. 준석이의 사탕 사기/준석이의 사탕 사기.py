import sys
input = sys.stdin.readline

N = input()
A = list(map(int, input().split()))

A.sort()

if sum(A)%2==0:
    print(sum(A))
else:
    for i in A:
        if i%2==0:
            continue
        else:
            print(sum(A)-i)
            break
        print(0)