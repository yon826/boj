import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
data = []

def Binary_search(i, A, start, end):
    mid = (start+end)//2
    if start > end:
        data.append(str(0))
    elif i == A[mid]:
        data.append(str(1))
    elif i > A[mid]:
        Binary_search(i, A, mid+1, end)
    else:
        Binary_search(i, A, start, mid-1)

for i in B:
    start = 0
    end = len(A)-1
    Binary_search(i, A, start, end)
print(' '.join(data))