import sys
input = sys.stdin.readline

X = {}
count = 0
count_time = 0
while(True):
    log = list(map(str, input().split()))
    if log == ["-1"]:
        break
    if log[2] == "right":
        count += 1
        if log[1] in X:
            count_time += X[log[1]]*20 + int(log[0])
        else:
            count_time += int(log[0])
    else:
        if log[1] in X:
            X[log[1]] += 1
        else:
            X[log[1]] = 1
print(count, count_time)