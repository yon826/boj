import sys
input = sys.stdin.readline

a = int(input())

for i in range(9):
    print(a , end = ' ')
    print("*" , end = ' ')
    print(i+1 , end = ' ')
    print("=" , end = ' ')
    print(a*(i+1))