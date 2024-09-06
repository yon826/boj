import sys
input = sys.stdin.readline

x, y = map(int, input().split())
a, b = map(int, input().split())

pt = 1

for i in range(x):
    for j in range(a):
        for k in range(y):
            for l in range(b):
                if pt == 1:
                    print("X", end = '')
                else:
                    print(".", end = '')
            pt *= -1
        print()
        if y%2 == 1:
            pt *= -1
    pt *= -1
    