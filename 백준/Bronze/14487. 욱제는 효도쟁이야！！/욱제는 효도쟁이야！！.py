import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
print(sum(A) - max(A))