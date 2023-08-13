# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 구현
# 1. 원 모양이 나오면 길이를 두 배로 늘려서 선형으로 만들 생각 하기

# 기타
# 1. 임의의 큰수로 초기화하기
temp = 1e9 # 1 * 10 ^ 9
temp2 = 2e9
