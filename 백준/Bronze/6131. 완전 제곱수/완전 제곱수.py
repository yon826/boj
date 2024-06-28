import sys
input = sys.stdin.readline

N = int(input())

count = 0
for i in range(1, 501):
    for j in range(1, 501):
        if i>j:
            if i*i == j*j+N:
                count += 1
print(count)