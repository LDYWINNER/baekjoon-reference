def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

# 재귀 함수로 구현하면 n이 커지면 커질수록 수행 시간이 기하급수적으로 늘어남
