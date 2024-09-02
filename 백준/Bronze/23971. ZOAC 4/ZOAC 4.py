a, b, c, d = map(int,input().split())

def sup(a, b):
    return a//b + int(bool(a % b))

print(sup(a, c+1) * sup(b, d+1))