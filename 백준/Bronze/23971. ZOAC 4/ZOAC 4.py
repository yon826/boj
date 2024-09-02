import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())

x = (b-1)//(d+1)
y = (a-1)//(c+1)
print((x+1)*(y+1))