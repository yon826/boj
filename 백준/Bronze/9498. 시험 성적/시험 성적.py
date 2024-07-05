import sys
input = sys.stdin.readline

M = int(input())

if M >= 90:
    print("A")
elif M >= 80:
    print("B")
elif M >= 70:
    print("C")
elif M >= 60:
    print("D")
else:
    print("F")
