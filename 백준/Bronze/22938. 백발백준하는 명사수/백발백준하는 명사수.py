import sys
input = sys.stdin.readline

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

if (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2) >= (r1+r2)*(r1+r2):
    print("NO")
else:
    print("YES")