import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = [0]*100
B = []

for i in range(M):
    x, y = map(int, input().split())
    B.append([x, y])

cnt = 0
for i in B:
    if 1 in i:
        break
    cnt += 1
if cnt == len(B):
    pass
else:
    temp = B[0]
    B[0] = B[cnt]
    B[cnt] = temp
    A[B[0][0]-1] = A[B[0][1]-1] = 1

def X(B):
    global count
    count = 0
    for i in B:
        if A[i[0]-1] == 1 and A[i[1]-1] == 1:
            pass
        elif A[i[0]-1] == 1 or A[i[1]-1] == 1:
            A[i[0]-1] = A[i[1]-1] = 1
            count += 1

count = 1
while count > 0:
    X(B)

if cnt == len(B):
    print(0)
else:
    print(A.count(1)-1)