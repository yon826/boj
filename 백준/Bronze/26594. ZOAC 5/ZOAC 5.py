import sys
input = sys.stdin.readline

N = input()

count = 1
x = N[0]
for i in range(len(N)):
    try:
        if x == N[i+1]:
            count += 1
    except:
        break

print(count)