# 10989 메모리 초과뜸
import sys
input = sys.stdin.readline
# counting sort: O(N)
# N 은 input number 의 개수
N = int(input())
nums = []
for n in range(N):
    nums.append(int(input()))

# 0 때문에 + 1
max_num = max(nums)
count_nums = [0] * (max_num + 1)
for i in range(N):
    count_nums[nums[i]] += 1

for j in range(1, max_num + 1):
    count_nums[j] += count_nums[j - 1]
#print(count_nums)

res = [0] * N
for k in range(N - 1, -1, -1):
    res[count_nums[nums[k]] - 1] = nums[k]
    count_nums[nums[k]] -= 1

for r in res:
    print(r)