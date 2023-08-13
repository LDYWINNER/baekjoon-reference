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


# 보텀업 bottom-up 방식: 단순하게 반복문을 이용하여 dp 코드를 작성한 경우는
# 작은 문제부터 차근차근 답을 도출한다고 하여 보텀업 방식으로 부름

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
