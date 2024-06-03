import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
start = 1
end = A[-1]
mid = (start+end)//2

def binary_search(array, start, target, end):
    while (start <= end):
        count = 0
        target = (start+end)//2
        for i in array:
            count += i//target
        if count >= N:
            start = target + 1
        else:
            end = target -1
    return end

print(binary_search(A, start, mid, end))
