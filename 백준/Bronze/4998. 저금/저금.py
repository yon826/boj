import sys
input = sys.stdin.readline

while(True):
    try:
        N, B, M = map(float, input().split())
        count = 0
        while(N <= M):
            N += N*B/100
            count += 1

        print(count)
    except:
        break