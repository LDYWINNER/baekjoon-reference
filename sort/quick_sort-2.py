# 위의 구현은 간결하고 이해하기 쉽지만 매번 재귀 호출될 때 마다 새로운 리스트를 생성하여 리턴하기 때문에 메모리 사용 측면에서 비효율적입니다.
# 큰 사이즈의 입력 데이터를 다뤄야하는 상용 코드에서는 이러한 단점은 치명적으로 작용할 수 있기 때문에 추가 메모리 사용이 적은 in-place 정렬이 선호됩니다.
# 처음부터 스스로 in-place 정렬을 구현하는 코드를 작성하기는 생각했던 것보다 쉽지 않을 수도 있습니다.
# 기존과 동일하게 값의 대소 비교를 위해서는 pivot 값을 사용하지만, 분할은 기준점은 pivot 값이 아닐 수도 있기 때문입니다.
# 왜냐하면, pivot 값을 기준으로 대소 비교를 했을 때 좌측과 우측에 여유 공간이 딱 맞는 경우가 드물기 때문입니다.

# quick sort 최적화 버전

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)


# 이코테 Hoare Partition 최적화
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
