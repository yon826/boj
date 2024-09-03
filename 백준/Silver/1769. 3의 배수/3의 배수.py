import sys
input = sys.stdin.readline

N = int(input())
count = 0
sum = 0

while N >= 10:
    sum = 0
    count += 1
    for i in str(N):
        sum += int(i)
        N = sum
    
print(count)

if sum == 0:
    if N % 3 == 0:
        print("YES")
    else:
        print("NO")    
else:
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")