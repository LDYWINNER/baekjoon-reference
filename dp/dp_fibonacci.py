import sys
input = sys.stdin.readline
print = sys.stdout.write


def fibonacci(n):
    f = [0 for x in range(n)]
    f[0] = 0
    f[1] = 1
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
    return f


T = int(input())
for t in range(T):
    num = int(input())
    print(str(fibonacci(num)))
