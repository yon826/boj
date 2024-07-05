import sys
input = sys.stdin.readline

a, b = map(int, input().split())

A = list(map(int, input().split()))
for i in A:
    if i < b:
        print(i)
