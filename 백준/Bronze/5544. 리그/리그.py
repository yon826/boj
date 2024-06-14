import sys
input = sys.stdin.readline

N = int(input())
B = []
for i in range(N):
    B.append([0, i+1])

for i in range(N*(N-1)//2):
    A = list(map(int, input().split()))
    if A[2] > A[3]:
        B[A[0]-1][0] += 3
        B[A[1]-1][0] += 0
    elif A[2] < A[3]:
        B[A[0]-1][0] += 0
        B[A[1]-1][0] += 3
    else:
        B[A[0]-1][0] += 1
        B[A[1]-1][0] += 1
B.sort()
B.reverse()

B[0].append(1)
for i in range(N-1):
    if B[i][0] == B[i+1][0]:
        B[i+1].append(B[i][2])
    else:
        B[i+1].append(i+2)

for i in range(N):
    for j in range(N):
        if B[j][1] == i+1:
            print(B[j][2])