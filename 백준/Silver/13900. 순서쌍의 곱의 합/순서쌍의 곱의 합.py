import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
prefix = [0]*n

for i in range(n-1, 0, -1):
    prefix[n-i] = prefix[n-i-1] + A[i]

sum = 0
for i in range(n-1):
    sum += A[i] * prefix[len(prefix)-1-i]
print(sum)