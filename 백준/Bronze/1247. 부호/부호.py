import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    sum = 0
    for i in range(n):
        x = int(input())
        sum += x
    if sum == 0:
        print("0")
    elif sum < 0:
        print("-")
    else:
        print("+")