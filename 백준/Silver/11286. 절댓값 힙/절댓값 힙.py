import sys
input = sys.stdin.readline
import heapq

N = int(input())
A = []

for i in range(N):
    x = int(input())
    if x == 0:
        if A:
            print(heapq.heappop(A)[1])
        else:
            print(0)
    else:
        heapq.heappush(A, (abs(x), x))