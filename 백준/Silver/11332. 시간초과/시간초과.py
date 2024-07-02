import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    sum = 1
    a, b, c, d = map(str, input().split())
    b = int(b)
    c = int(c)
    d = int(d)
    if a == "O(N)":
        if b * c <= pow(10, 8)*d:
            print("May Pass.")
        else:
            print("TLE!")
    elif a == "O(2^N)":
        if pow(2, b) * c <= pow(10, 8)*d:
            print("May Pass.")
        else:
            print("TLE!")
    elif a == "O(N!)":
        if b > 12:
            print("TLE!")
        else:
            for i in range(1, b + 1):
                sum *= i
            if sum * c <= pow(10, 8)*d:
                print("May Pass.")
            else:
                print("TLE!")
    elif a == "O(N^3)":
        if pow(b, 3) <= pow(10, 8)*d/c:
            print("May Pass.")
        else:
            print("TLE!")
    else:
        if pow(b, 2) * c <= pow(10, 8)*d:
            print("May Pass.")
        else:
            print("TLE!")