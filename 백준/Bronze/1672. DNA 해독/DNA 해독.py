n = int(input())
A = input()
X = []
for i in A:
    X.append(i)

Y = [["A", "C", "A", "G"], 
     ["C", "G", "T", "A"], 
     ["A", "T", "C", "G"], 
     ["G", "A", "G", "T"]]

dic = {"A" : 0, "G" : 1, "C" : 2, "T" : 3}

for _ in range(n-1):
    X.append(Y[dic[X.pop()]][dic[X.pop()]])

print(X[0])