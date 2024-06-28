import sys
input = sys.stdin.readline

C, K, P = map(int, input().split())

sum = 0
for i in range(1, C+1):
    sum += i*K + i*i*P

print(sum)