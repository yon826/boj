import sys
input = sys.stdin.readline

d1, d2, d3 = map(int, input().split())
sum = d1 + d2 + d3
a = sum*0.5 - d3
b = sum*0.5 - d2
c = sum*0.5 - d1

if a <= 0 or b <= 0 or c <= 0:
    print(-1)
else:
    print(1)
    print(round(a, 1), round(b, 1), round(c, 1))