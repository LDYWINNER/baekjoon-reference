# bubble sort 최적화 버전
def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# 이전 패스에서 앞뒤 자리 비교(swap)이 한번도 일어나지 않았다면 정렬되지 않는 값이 하나도 없었다고 간주할 수 있습니다.
# 따라서 이럴 경우, 이후 패스를 수행하지 않아도 됩니다.
