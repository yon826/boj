import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
A = list(map(int, input().split()))

sums = 0
for i in range(K%N):
    x = i
    try:
        sums += A[B%N-1 + x]
    except:
        x -= N
        sums += A[B%N-1 + x]
print(sum(A)*(K//N) + sums)