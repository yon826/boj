import sys
input = sys.stdin.readline

N = int(input())
S = input()
S = S[:-1]

count = 0

countlow = 0
countup = 0
countnum = 0

for i in S:
    if i.islower():
        countlow += 1
    if i.isupper():
        countup += 1
    if i.isdecimal():
        countnum += 1
if countlow == 0:
    count += 1
if countup == 0:
    count += 1
if countnum == 0:
    count += 1
if S.isalnum():
    count += 1

if count + len(S) < 6:
    print(6-len(S))
else:
    print(count)