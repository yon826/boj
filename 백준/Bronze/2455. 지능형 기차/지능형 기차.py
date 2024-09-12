import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = [b]

for i in range(1, 4):
    a, b = map(int, input().split())
    A.append(A[i-1] - a + b)

print(max(A))