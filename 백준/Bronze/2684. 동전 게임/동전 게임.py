import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    B = [0, 0, 0, 0, 0, 0, 0, 0]
    A = input().strip()
    for j in range(38):
        if A[j:j+3] == "TTT":
            B[0] += 1
        elif A[j:j+3] == "TTH":
            B[1] += 1
        elif A[j:j+3] == "THT":
            B[2] += 1
        elif A[j:j+3] == "THH":
            B[3] += 1
        elif A[j:j+3] == "HTT":
            B[4] += 1
        elif A[j:j+3] == "HTH":
            B[5] += 1
        elif A[j:j+3] == "HHT":
            B[6] += 1
        elif A[j:j+3] == "HHH":
            B[7] += 1
    for j in B:
        print(j, end = ' ')
    print()