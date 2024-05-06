import sys
input = sys.stdin.readline

w = input()
x = input()
y = input()
z = input()
A = []
B = []
C = []
D = []
for i in range(8):
    A.append(w[i])
for i in range(8):
    B.append(x[i])
for i in range(8):
    C.append(y[i])
for i in range(8):
    D.append(z[i])

K = int(input())

def Turn(n, turn):
    if turn == -1:
        temp = n[0]
        for i in range(7):
            n[i] = n[i+1]
        n[7] = temp
    else:
        temp = n[7]
        for i in range(7):
            n[7-i] = n[6-i]
        n[0] = temp

for i in range(K):
    N, M = map(int, input().split())
    turn = M
    if N == 1:
        if A[2] != B[6]:
            if B[2] != C[6]:
                if C[2] != D[6]:
                    turn *= -1
                    Turn(D, turn)
                    turn *= -1
                Turn(C, turn)
            turn *= -1
            Turn(B, turn)
            turn *= -1
        Turn(A, turn)
    elif N == 2:
        if B[2] != C[6]:
            if C[2] != D[6]:
                Turn(D, turn)
            turn *= -1
            Turn(C, turn)   
            turn *= -1
        if B[6] != A[2]:
            turn *= -1
            Turn(A, turn) 
            turn *= -1
        Turn(B, turn)
    elif N == 3:
        if C[6] != B[2]:
            if B[6] != A[2]:
                Turn(A, turn)
            turn *= -1
            Turn(B, turn)   
            turn *= -1
        if C[2] != D[6]:
            turn *= -1
            Turn(D, turn)
            turn *= -1
        Turn(C, turn)
    elif N == 4:
        if D[6] != C[2]:
            if C[6] != B[2]:
                if B[6] != A[2]:
                    turn *= -1
                    Turn(A, turn)
                    turn *= -1
                Turn(B, turn)
            turn *= -1
            Turn(C, turn)
            turn *= -1
        Turn(D, turn)

score = 0
if A[0] == '1':
    score += 1
if B[0] == '1':
    score += 2
if C[0] == '1':
    score += 4
if D[0] == '1':
    score += 8

print(score)