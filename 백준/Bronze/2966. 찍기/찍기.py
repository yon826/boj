import sys
input = sys.stdin.readline

n = int(input())
answer = input()

Adrian_ans = ""
Bruno_ans = ""
Goran_ans = ""

for i in range(n//3+1):
    Adrian_ans += "ABC"
    Bruno_ans += "BABC"
    Goran_ans += "CCAABB"

Adrian = 0
Bruno = 0
Goran = 0
for i in range(n):
    if answer[i] == Adrian_ans[i]:
        Adrian += 1
    if answer[i] == Bruno_ans[i]:
        Bruno += 1
    if answer[i] == Goran_ans[i]:
        Goran += 1

X = sorted([[Adrian, "Adrian"], [Bruno, "Bruno"], [Goran, "Goran"]])
print(max(X)[0])
if X[0][0] == X[1][0] == X[2][0]:
    print(X[0][1])
    print(X[1][1])
    print(X[2][1])
elif X[1][0] == X[2][0]:
    print(X[1][1])
    print(X[2][1])
else:
    print(X[2][1])
