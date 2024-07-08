import sys
input = sys.stdin.readline
from collections import deque

A = deque()
count = 0
while(1):
    x = input()
    if x[:-1] == ".":
        break
    for i in x:
        if i == "(" or i == "{" or i == "[":
            A.append(i)
        elif i == ")" or i == "}" or i == "]":
            if A:
                if A[-1] == "(" and i == ")":
                    A.pop()
                elif A[-1] == "{" and i == "}":
                    A.pop()
                elif A[-1] == "[" and i == "]":
                    A.pop()
                else:
                    count += 1
            else:
                count += 1
            
        if i == ".":
            if A:
                print("no")
            elif count > 0:
                print("no")
            else:
                print("yes")
            count = 0
            A.clear()