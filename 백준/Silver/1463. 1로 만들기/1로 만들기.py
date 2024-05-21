import sys
input = sys.stdin.readline

num = int(input())

count = [0] * 1000001

for i in range(2, num + 1):
    A = []
    if i%3 == 0:
        A.append(count[i//3] + 1)
    if i%2 == 0:
        A.append(count[i//2] + 1)
    A.append(count[i-1] + 1)

    count[i] = min(A)

print(count[num])