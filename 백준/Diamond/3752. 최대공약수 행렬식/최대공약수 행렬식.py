MOD = int(1e9 + 7)
MAX_IDX = 1000

class IntPhi:
    def __init__(self, n, phi):
        self.n = n
        self.phi = phi

def cmp(a, b):
    return a - b


T = int(input())

for _ in range(T):
    arr = []
    n = int(input())
    numbers = list(map(int, input().split()))
        
    for x in numbers:
        arr.append(IntPhi(x, 0))

    arr.sort(key=lambda x: x.n)

    arr[0].phi = 1     # phi(1)
    retval = 1
    for i in range(1, n):
        temp = 0
        for j in range(i):
            if arr[i].n % arr[j].n == 0:
                temp += arr[j].phi
        arr[i].phi = arr[i].n - temp
        retval *= arr[i].phi
        retval %= MOD

    print(retval)