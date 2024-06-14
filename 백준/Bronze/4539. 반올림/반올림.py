import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    x = 10
    M = int(input())
    while(True):
        if M > x:
            if M%x >= 5*x/10:
                M += x - M%x
            else:
                M -= M%x
            x *= 10
        else:
            break
    print(M)